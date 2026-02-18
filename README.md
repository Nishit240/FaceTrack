# FaceTrack
# 🎯 Face Recognition-Based Attendance System (FaceTrack)

An AI-powered attendance system that uses real-time face detection and recognition to automatically mark and record attendance. Built using Python, OpenCV, and Tkinter.

---

## 📌 Features

- 🎥 Live face detection using OpenCV
- 🧠 Face recognition using LBPH algorithm
- 📂 Image dataset collection with webcam
- 🏷️ Automatic attendance marking with date & time
- 💾 Attendance logging in Mysql
- 🖥️ Graphical User Interface with Tkinter
- 📸 Face training module
- 👨‍💻 Easy to use and extend

---

## 🖼️ Screenshots
- Below are screenshots from each key module of the system:

### 🏠 1. Main Window (Dashboard)
Home screen with navigation to all functionalities <br />
<br />
<img width="1919" height="1052" alt="image" src="https://github.com/user-attachments/assets/86a59653-beda-49f3-a11a-1cfad36e9938" />

---

### 👨‍🎓 2. Student Registration Page
Form to register student details and capture face images <br />
<br />
<img width="1919" height="1050" alt="image" src="https://github.com/user-attachments/assets/c108ad7e-7005-469a-9e41-516b8e3f1cd7" />

---

### 👁️ 3. Face Recognition Page
Live webcam feed that detects, recognizes faces, and marks attendance <br />
<br />
<img width="1919" height="1054" alt="image" src="https://github.com/user-attachments/assets/ae492fad-e9f3-47a8-8c65-5b05eef4039c" />

---

### 📅 4. Attendance Records Page
Displays attendance saved in attendance.csv with timestamp <br />
<br />
<img width="1919" height="1050" alt="image" src="https://github.com/user-attachments/assets/dacf88fe-030d-4b8d-8977-7e0a5e464a89" />

---

### 🧠 5. Face Training Page
Trains the LBPH model using captured face images <br />
<br />
<img width="1878" height="963" alt="image" src="https://github.com/user-attachments/assets/04ed9cd4-45de-43f3-bf23-18e75811e56e" />

---

### 📄 About Page
Its core purpose is to minimize manual work <br />
<br />
<img width="1919" height="1046" alt="image" src="https://github.com/user-attachments/assets/effaf794-8ae9-410f-82fb-f8fcf75b40b2" />

---

### 📧 Help Desk Page
<img width="1919" height="1051" alt="image" src="https://github.com/user-attachments/assets/b5b4ba2a-24f0-4fcd-848e-b53cdb808bc6" />

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
├── data/                      # Folder to store face images for training<br />
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

- Admin login system

- Email/SMS alerts on attendance

- Detailed analytics dashboard

---

## 📧 Contact
- Developer: Nishit Jain

---
