# FaceTrack
# 🎯 Face Recognition-Based Attendance System (FaceTrack)

An AI-powered attendance system that uses real-time face detection and recognition to automatically mark and record attendance. Built using Python, OpenCV, and Tkinter.

---

## 📌 Features

- 🎥 Live face detection using OpenCV
- 🧠 Face recognition using LBPH algorithm
- 📂 Image dataset collection with webcam
- 🏷️ Automatic attendance marking with date & time
- 💾 Attendance logging in CSV file
- 🖥️ Graphical User Interface with Tkinter
- 📸 Face training module
- 👨‍💻 Easy to use and extend

---

## 🛠️ Tech Stack

- **Frontend/UI**: Tkinter (Python GUI)
- **Image Processing**: OpenCV, PIL (Pillow)
- **Machine Learning Model**: OpenCV's LBPH Face Recognizer
- **Data Storage**: CSV (for attendance logs)
- **Language**: Python

---

## 🚀 Setup Instructions

### 1. Clone the Repository

git clone https://github.com/yourusername/face-recognition-attendance-system.git
cd face-recognition-attendance-system

### 2. Create a Virtual Environment (Optional but Recommended)
python -m venv .venv
source .venv/Scripts/activate  # On Windows


### 3. Install Dependencies

pip install -r requirements.txt

### If requirements.txt doesn't exist, manually install:
pip install opencv-python opencv-contrib-python pillow numpy tk

### 4. Project Folder Structure

face-recognition-attendance-system/
├── data/                      # Folder to store face images for training
├── image/                     # UI background images
├── attendance.csv             # Output attendance log
├── classifier.xml             # Trained model (generated after training)
├── main.py                    # Main app launcher
├── train.py                   # Train the model
├── face_recognition.py        # Recognize and mark attendance
├── student.py                 # Register students and collect data
├── README.md    
