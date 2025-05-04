# 🤖 Diff Drive Robot

Đây là một dự án mô phỏng robot điều khiển vi sai (differential drive robot) sử dụng **ROS Noetic** và **Gazebo**.  
Dự án bao gồm nhiều gói con (*sub-packages*) để mô phỏng robot trong các tình huống khác nhau như điều hướng, lập bản đồ SLAM và theo dõi con người. Robot có thể được điều khiển thông qua bàn phím hoặc các lệnh ROS, hỗ trợ các tác vụ như điều hướng và lập bản đồ.

---

## 🧰 Hướng dẫn cài đặt và chạy dự án

### ✅ 1. Cài đặt ROS Noetic

Làm theo hướng dẫn chính thức tại:  
👉 [http://wiki.ros.org/noetic/Installation/Ubuntu](http://wiki.ros.org/noetic/Installation/Ubuntu)

---

### 🗂️ 2. Tạo và cấu hình không gian làm việc Catkin

```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
```

---

### 🔄 3. Sao chép repository

```bash
git clone https://github.com/23hoangkt/Diff_drive_robot.git
```

---

### 📦 4. Cài đặt các gói phụ thuộc

```bash
cd ~/catkin_ws
rosdep install --from-paths src --ignore-src -r -y
```

---

### 🛠️ 5. Biên dịch không gian làm việc

```bash
catkin_make
source devel/setup.bash
```

---

### ➕ 6. Cài đặt các gói ROS bổ sung (nếu cần)

```bash
sudo apt-get install ros-noetic-gazebo-ros ros-noetic-teleop-twist-keyboard \
ros-noetic-rviz ros-noetic-slam-gmapping ros-noetic-move-base ros-noetic-hector-slam
```

---

## 🚀 Khởi chạy dự án

### 🔧 Bước 1: Khởi động Gazebo với robot (gói `boe_bot`)

```bash
roslaunch boe_bot gazebo.launch
```

📷 *(Thêm ảnh chụp màn hình Gazebo tại đây)*

---

### 👁️ Bước 2: Khởi động RViz để trực quan hóa

```bash
roslaunch boe_bot rviz.launch
```

📷 *(Thêm ảnh chụp màn hình RViz tại đây)*

---

### 🗺️ Bước 3: Khởi động SLAM với Hector SLAM (gói `boe_bot_slam`)

```bash
roslaunch boe_bot_slam boe_bot_hector_slam.launch world_name:="turtlebot3_world.world"
```

Lệnh này sẽ khởi động Gazebo với thế giới `turtlebot3_world.world` và chạy Hector SLAM để bắt đầu lập bản đồ.

📷 *(Thêm ảnh chụp màn hình Gazebo với turtlebot3_world tại đây)*

---

### 🖼️ Bước 4: Khởi động RViz để xem bản đồ đang tạo (gói `boe_bot_slam`)

```bash
roslaunch boe_bot_slam rviz.launch
```

RViz sẽ hiển thị bản đồ 2D được tạo bởi Hector SLAM và trạng thái robot.

📷 *(Thêm ảnh chụp màn hình RViz hiển thị bản đồ tại đây)*

---

### ⌨️ Bước 5: Điều khiển robot để quét bản đồ

Mở một terminal mới và chạy:

```bash
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```

Sử dụng các phím (mặc định: `i`, `j`, `k`, `l`, `,`) để điều khiển robot. Robot sẽ quét môi trường và cập nhật bản đồ trong RViz.

📷 *(Thêm ảnh robot di chuyển và bản đồ được cập nhật tại đây)*

---

### 💾 Bước 6: Lưu bản đồ

Sau khi quét xong, lưu bản đồ bằng công cụ `map_server`. Mở terminal mới và chạy:

```bash
rosrun map_server map_saver -f my_map
```

Bản đồ sẽ được lưu dưới dạng file `my_map.pgm` và `my_map.yaml` trong thư mục hiện hành.

📷 *(Thêm ảnh chụp màn hình file bản đồ đã lưu tại đây)*

---

### 🧭 Bước 7: Điều hướng (gói `boe_bot_navigation`)

```bash
roslaunch boe_bot_navigation navigation.launch
```

📷 *(Thêm ảnh chụp màn hình điều hướng tại đây)*

---

### 👣 Bước 8: Theo dõi con người (gói `boe_bot_human_tracking`)

```bash
roslaunch boe_bot_human_tracking human_tracker.launch
```

📷 *(Thêm ảnh chụp màn hình theo dõi con người tại đây)*

---

## 📁 Cấu trúc thư mục (gợi ý)

```
Diff_drive_robot/
├── boe_bot/                # Mô phỏng robot
├── boe_bot_slam/           # SLAM với Hector SLAM
├── boe_bot_navigation/     # Điều hướng robot
├── boe_bot_human_tracking/ # Theo dõi con người
├── README.md               # Hướng dẫn này
└── ...
```

---

## 📜 Giấy phép

Dự án này sử dụng giấy phép **MIT**. Xem file [LICENSE](LICENSE) để biết thêm chi tiết.

---

## 🙌 Đóng góp

Mọi đóng góp đều được hoan nghênh! Bạn có thể:

- Tạo pull request
- Báo lỗi (issues)
- Cải tiến tài liệu hoặc tính năng mới

---

## 📬 Liên hệ

Nếu bạn có câu hỏi, vui lòng liên hệ qua GitHub hoặc email trong phần thông tin tài khoản.

---
