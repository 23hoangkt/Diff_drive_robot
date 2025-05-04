#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import numpy as np
from ultralytics import YOLO

class PersonFollower:
    def __init__(self):
        # Khởi tạo node ROS
        rospy.init_node('person_follower', anonymous=True)
        
        # Publisher và Subscriber
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.image_sub = rospy.Subscriber('/camera/depth/image_raw', Image, self.image_callback)
        self.depth_sub = rospy.Subscriber('/camera/depth/depth/image_raw', Image, self.depth_callback)
        
        # Khởi tạo CvBridge
        self.bridge = CvBridge()
        
        # Tải mô hình YOLOv8
        self.model = YOLO('yolov8n.pt')  # Sử dụng mô hình YOLOv8 nano
        
        # Biến lưu trữ
        self.depth_image = None
        self.target_distance = 4  # Khoảng cách mong muốn tới người (mét)
        self.linear_speed = 0.3  # Tốc độ tuyến tính tối đa (m/s)
        self.angular_speed = 0.5  # Tốc độ góc tối đa (rad/s)
        self.spin_duration = 5.0  # Thời gian xoay tròn khi không thấy người (giây)
        self.spin_speed = 2  # Tốc độ xoay tròn (rad/s)
        self.is_spinning = False  # Trạng thái xoay tròn
        self.spin_start_time = None  # Thời điểm bắt đầu xoay
        
    def image_callback(self, data):
        try:
            # Chuyển ROS Image message sang OpenCV image
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            
            # Chạy YOLOv8 để phát hiện người
            results = self.model(cv_image)
            
            # Lấy kết quả phát hiện
            person_detected = False
            target_center_x = 0
            target_width = 0
            depth_value = float('nan')
            
            for result in results:
                boxes = result.boxes
                for box in boxes:
                    if box.cls == 0:  # Class 0 là 'person' trong YOLOv8
                        person_detected = True
                        # Lấy tọa độ bounding box
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        target_center_x = (x1 + x2) // 2
                        target_width = x2 - x1
                        
                        # Vẽ bounding box
                        cv2.rectangle(cv_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        
                        # Thêm nhãn "Person" lên bounding box
                        label = "Person"
                        cv2.putText(cv_image, label, (x1, y1 - 10), 
                                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                        
                        # Tính khoảng cách tới người (nếu có depth image)
                        if self.depth_image is not None:
                            center_y = (y1 + y2) // 2
                            depth_value = self.depth_image[center_y, target_center_x]
                            if not np.isnan(depth_value):
                                # Thêm khoảng cách lên hình ảnh
                                distance_text = f"Distance: {depth_value:.2f}m"
                                cv2.putText(cv_image, distance_text, (x1, y2 + 20), 
                                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            # Hiển thị hình ảnh với bounding box và văn bản
            cv2.imshow("Person Follower", cv_image)
            cv2.waitKey(1)
            
            # Điều khiển robot
            cmd = Twist()
            if person_detected and self.depth_image is not None and not np.isnan(depth_value):
                # Nếu phát hiện người, dừng xoay và bám theo
                self.is_spinning = False
                # Điều chỉnh tốc độ tuyến tính dựa trên khoảng cách
                distance_error = depth_value - self.target_distance
                cmd.linear.x = max(min(distance_error * 0.5, self.linear_speed), -self.linear_speed)
                
                # Điều chỉnh tốc độ góc dựa trên vị trí ngang
                image_center_x = cv_image.shape[1] // 2
                angular_error = (image_center_x - target_center_x) / float(image_center_x)
                cmd.angular.z = max(min(angular_error * 2.0, self.angular_speed), -self.angular_speed)
            else:
                # Nếu không thấy người, kiểm tra trạng thái xoay
                if not self.is_spinning:
                    # Bắt đầu xoay
                    self.is_spinning = True
                    self.spin_start_time = rospy.get_time()
                
                # Kiểm tra thời gian xoay
                if self.is_spinning and (rospy.get_time() - self.spin_start_time < self.spin_duration):
                    # Xoay tròn
                    cmd.angular.z = self.spin_speed
                else:
                    # Hết thời gian xoay, dừng lại và reset trạng thái
                    self.is_spinning = False
                    cmd.angular.z = 0.0
            
            # Xuất bản lệnh điều khiển
            self.cmd_vel_pub.publish(cmd)
            
        except CvBridgeError as e:
            rospy.logerr("CvBridge Error: {0}".format(e))
    
    def depth_callback(self, data):
        try:
            # Chuyển ROS Image message sang OpenCV image (depth)
            self.depth_image = self.bridge.imgmsg_to_cv2(data, desired_encoding="32FC1")
        except CvBridgeError as e:
            rospy.logerr("CvBridge Error: {0}".format(e))
    
    def run(self):
        rospy.spin()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        follower = PersonFollower()
        follower.run()
    except rospy.ROSInterruptException:
        pass