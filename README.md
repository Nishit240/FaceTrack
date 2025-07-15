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

## 🖼️ Screenshots
- Below are screenshots from each key module of the system:

###🏠 1. Main Window (Dashboard)
Home screen with navigation to all functionalities
<img width="1919" height="1052" alt="image" src="https://github.com/user-attachments/assets/86a59653-beda-49f3-a11a-1cfad36e9938" />


## 🛠️ Tech Stack

- **Frontend/UI**: Tkinter (Python GUI)
- **Image Processing**: OpenCV, PIL (Pillow)
- **Machine Learning Model**: OpenCV's LBPH Face Recognizer
- **Data Storage**: CSV (for attendance logs)
- **Language**: Python

---

## 🚀 Setup Instructions

### 1. Clone the Repository

git clone https://github.com/Nishit240/FaceTrack.git <br />
cd `` face-recognition-attendance-system`` 

### 2. Create a Virtual Environment (Optional but Recommended)
python -m venv .venv <br />
source .venv/Scripts/activate  # On Windows

---

### 3. Install Dependencies

``pip install -r requirements.txt`` 

### If requirements.txt doesn't exist, manually install:
``pip install opencv-python opencv-contrib-python pillow numpy tk``

---

### 4. Project Folder Structure
<pre>
face-recognition-attendance-system/ <br />
├── data/                      .# Folder to store face images for training<br />
├── image/                     # UI background images<br />
├── attendance.csv             # Output attendance log<br />
├── classifier.xml             # Trained model (generated after training)<br />
├── main.py                    # Main app launcher<br />
├── train.py                   # Train the model<br />
├── face_recognition.py        # Recognize and mark attendance<br />
├── student.py                 # Register students and collect data<br />
├── README.md
</pre>pre>
---

## ✅ How It Works
#### Capture Faces:

- Add student and capture multiple face images via webcam.

#### Train the Model:

- Use ``train.py`` to process and train the data using LBPH algorithm.

#### Face Recognition:

- Launch face recognition, match faces, and auto-log attendance.

#### Attendance Logs:

- Attendance is saved in ``attendance.csv`` with student ID, name, date, and time.

---

## 🧠 LBPH Algorithm
This project uses the Local Binary Pattern Histogram (LBPH) face recognizer from ``opencv-contrib``. It's fast, lightweight, and works well for real-time face recognition on small datasets.

---

## 📦 Requirements
- All required libraries are listed in ``requirements.txt``, but core ones include:

- ``opencv-python``

- ``Pillow``

- ``tkinter``

- ``numpy``

- ``tkcalendar`` (if used for student entry forms)

---

## 🎯 Objectives
- Reduce human error in attendance marking

- Save time with a fully automated system

- Ensure a hygienic, touchless method post-COVID

- Make the system low-cost and scalable

---

## 🛡️ Future Improvements
- Database integration (MySQL or SQLite)

- Admin login system

- Email/SMS alerts on attendance

- Detailed analytics dashboard

---

## 📧 Contact
- Developer: Nishit Jain

---
