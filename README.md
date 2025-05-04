  # Diff Drive Robot

Đây là một dự án mô phỏng robot điều khiển vi sai (differential drive robot) sử dụng **ROS Noetic** và **Gazebo**.  
Dự án bao gồm nhiều gói con (*sub-packages*) để mô phỏng robot trong các tình huống khác nhau như điều hướng, lập bản đồ SLAM và theo dõi con người. Robot có thể được điều khiển thông qua bàn phím hoặc các lệnh ROS, hỗ trợ các tác vụ như điều hướng và lập bản đồ.

---

## Yêu cầu phiên bản

- Ubuntu 20.04
- ROS Noetic

---

## Cài đặt và chạy dự án

1. Tạo và cấu hình không gian làm việc Catkin:
    ```bash
    mkdir -p ~/catkin_ws/src
    cd ~/catkin_ws/src
    ```

2. Sao chép repository:
    ```bash
    git clone https://github.com/23hoangkt/Diff_drive_robot.git
    ```

3. Cài đặt các gói phụ thuộc:
    ```bash
    cd ~/catkin_ws
    rosdep install --from-paths src --ignore-src -r -y
    ```

4. Biên dịch không gian làm việc:
    ```bash
    catkin_make
    source devel/setup.bash
    ```

5. Cài đặt các gói ROS bổ sung (nếu cần):
    ```bash
    sudo apt-get install ros-noetic-gazebo-ros ros-noetic-teleop-twist-keyboard \
    ros-noetic-rviz ros-noetic-slam-gmapping ros-noetic-move-base ros-noetic-hector-slam
    ```

---

## Khởi chạy dự án

1. Khởi động Gazebo với robot (gói `boe_bot`):
    ```bash
    roslaunch boe_bot gazebo.launch
    ```

    ![Gazebo with robot](path_to_gazebo_image)  <!-- Thêm ảnh chụp màn hình Gazebo tại đây -->

2. Khởi động RViz để trực quan hóa:
    ```bash
    roslaunch boe_bot rviz.launch
    ```

    ![RViz visualization](path_to_rviz_image)  <!-- Thêm ảnh chụp màn hình RViz tại đây -->

3. Khởi động SLAM với Hector SLAM (gói `boe_bot_slam`):
    ```bash
    roslaunch boe_bot_slam boe_bot_hector_slam.launch world_name:="turtlebot3_world.world"
    ```

    ![Gazebo with world](path_to_world_image)  <!-- Thêm ảnh chụp màn hình Gazebo với turtlebot3_world tại đây -->

4. Khởi động RViz để xem bản đồ đang tạo (gói `boe_bot_slam`):
    ```bash
    roslaunch boe_bot_slam rviz.launch
    ```

    ![RViz map](path_to_map_image)  <!-- Thêm ảnh chụp màn hình RViz hiển thị bản đồ tại đây -->

5. Điều khiển robot để quét bản đồ:
    ```bash
    rosrun teleop_twist_keyboard teleop_twist_keyboard.py
    ```

    ![Robot scanning](path_to_robot_image)  <!-- Thêm ảnh robot di chuyển và bản đồ được cập nhật tại đây -->

6. Lưu bản đồ:
    ```bash
    rosrun map_server map_saver -f my_map
    ```

    ![Saved map](path_to_saved_map_image)  <!-- Thêm ảnh chụp màn hình file bản đồ đã lưu tại đây -->

7. Điều hướng (gói `boe_bot_navigation`):
    ```bash
    roslaunch boe_bot_navigation navigation.launch
    ```

    ![Navigation](path_to_navigation_image)  <!-- Thêm ảnh chụp màn hình điều hướng tại đây -->

8. Theo dõi con người (gói `boe_bot_human_tracking`):
    ```bash
    roslaunch boe_bot_human_tracking human_tracker.launch
    ```

    ![Human tracking](path_to_tracking_image)  <!-- Thêm ảnh chụp màn hình theo dõi con người tại đây -->

---

## Giấy phép

Dự án này sử dụng giấy phép **MIT**.  
Xem file [LICENSE](LICENSE) để biết thêm chi tiết.

---

## Đóng góp

Mọi đóng góp đều được hoan nghênh! Bạn có thể:

- Tạo pull request
- Báo lỗi (issues)
- Cải tiến tài liệu hoặc tính năng mới

---

## Liên hệ

Nếu bạn có câu hỏi, vui lòng liên hệ qua GitHub hoặc email trong phần thông tin tài khoản.
