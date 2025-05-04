# 🤖 Diff Drive Robot

Dự án mô phỏng robot điều khiển vi sai (Differential Drive Robot) sử dụng **ROS Noetic** và **Gazebo**. Dự án bao gồm nhiều gói con (sub-packages) hỗ trợ mô phỏng các chức năng như:

- Điều hướng (Navigation)  
- Lập bản đồ (SLAM)  
- Theo dõi con người (Human Tracking)

Robot có thể được điều khiển thông qua bàn phím hoặc các lệnh ROS, hỗ trợ các tác vụ lập bản đồ, điều hướng trong môi trường ảo.

## 🚀 Hướng dẫn cài đặt và chạy dự án

### 1. Cài đặt ROS Noetic  
Làm theo hướng dẫn chính thức tại:  
👉 [http://wiki.ros.org/noetic/Installation/Ubuntu](http://wiki.ros.org/noetic/Installation/Ubuntu)

### 2. Tạo và cấu hình không gian làm việc Catkin  
```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src

