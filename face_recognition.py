# face_recognition.py
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import mysql.connector
from datetime import datetime


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x1000+0+0")
        self.root.title("FaceTrack")
        self.root.configure(bg="#0f0f0f")  # dark background

        self.session_attendance_set = set()
        self.video_cap = None  # camera variable

        # ========== HEADER (Navbar Style) ==========

        header = Frame(self.root, bg="#121416", height=60)
        header.place(x=0, y=0, width=1550, height=60)

        logo_lbl = Label(header, text="FaceTrack", font=("Helvetica", 16, "bold"), fg="white", bg="#121416")
        logo_lbl.place(x=30, y=15)

        menu_font = ("Helvetica", 11)
        Button(header, text="Home", font=menu_font, fg="white", bg="#121416", bd=0,
            command=self.home).place(x=1240, y=18)
        Button(header, text="About", font=menu_font, fg="white", bg="#121416", bd=0, command=self.about).place(x=1310, y=18)
        Button(header, text="Help", font=menu_font, fg="white", bg="#121416", bd=0, command=self.help_desk1).place(x=1380, y=18)
        profile_icon = Label(header, text="👤", font=("Arial", 14), fg="white", bg="#121416")
        profile_icon.place(x=1450, y=16)


                # ========== TITLES & SUBHEADINGS ==========
        Label(self.root, text="Face Recognition", font=("Helvetica", 26, "bold"), bg="#0f0f0f", fg="white").place(x=50, y=70)

        Label(self.root, text="Capture an image to recognize faces and log attendance.",
              font=("Helvetica", 13), bg="#0f0f0f", fg="gray").place(x=50, y=120)

        # ========== LIVE CAMERA FEED ==========
        Label(self.root, text="Live Camera Feed", font=("Helvetica", 16, "bold"), bg="#0f0f0f", fg="white").place(x=50, y=160)

        # Left frame (Monitor Image)
        left_img = Image.open(r"C:\Users\NISHIT JAIN\OneDrive\Desktop\face recognition system\image\Live Camera.png").resize((720, 500), Image.LANCZOS)
        self.left_photo = ImageTk.PhotoImage(left_img)
        self.frame_bg = Label(self.root, image=self.left_photo, bg="#0f0f0f")
        self.frame_bg.place(x=50, y=200, width=720, height=500)

        # Camera feed (inside the monitor)
        self.cam_label = Label(self.root, bg="black")
        self.cam_label.place(x=180, y=280, width=480, height=350)  # Adjusted to be centered inside monitor

        # ========== RIGHT SIDE INFO / IMAGE ==========
        img_size = (700, 500)
        img_right = Image.open("image/FR2.jpg").resize(img_size, Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl_right = Label(self.root, image=self.photoimg_right, bg="#0f0f0f")
        f_lbl_right.place(x=800, y=200, width=700, height=500)

        Button(f_lbl_right, text="Face Recognition", font=("Helvetica", 13, "bold"),
               bg="#969F9E", fg="white", bd=0, cursor="hand2", command=self.face_recog).place(x=95, y=367, width=140, height=25)


    def mark_attendence(self, i, r, n, d):
        now = datetime.now()
        d1 = now.strftime("%d-%m-%Y")
        dtString = now.strftime("%H:%M:%S")
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        filename = os.path.join(log_dir, f"attendance_{d1}.csv")

        if not os.path.exists(filename):
            with open(filename, "w", newline="\n") as f:
                f.write("ID,Roll,Name,Department,Time,Date,Status\n")

        key = f"{i}_{d1}"
        if key not in self.session_attendance_set:
            with open(filename, "r+") as f:
                lines = f.readlines()
                for line in lines:
                    entry = line.strip().split(",")
                    if len(entry) > 5 and entry[0] == i and entry[5] == d1:
                        self.session_attendance_set.add(key)
                        messagebox.showinfo("Attendance", f"ℹ️ Attendance already marked for {n} ({r})")
                        return
            with open(filename, "a") as f:
                f.write(f"{i},{r},{n},{d},{dtString},{d1},Present\n")
            self.session_attendance_set.add(key)
            messagebox.showinfo("Attendance", f"✅ Attendance marked for {n} ({r})")

    def face_recog(self):
            # Stop camera if already running
        if self.video_cap and self.video_cap.isOpened():
            self.video_cap.release()
            self.cam_label.config(image='', text="🔄 Restarting camera...", fg="white", bg="black")
            self.root.unbind("<Return>")

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
                cursor = conn.cursor()
                cursor.execute("SELECT student_id, roll, Name, dep FROM student WHERE student_id=%s", (id,))
                result = cursor.fetchone()
                conn.close()

                if result and confidence > 77:
                    i, r, n, d = map(str, result)
                    cv2.putText(img, f"Student ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)
                    cv2.putText(img, f"Dept:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)
                    self.mark_attendence(i, r, n, d)
                else:
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 2)

        def recognize(img, clf, faceCascade):
            draw_boundary(img, faceCascade, 1.1, 10, (0, 255, 0), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        self.video_cap = cv2.VideoCapture(0)
        self.root.bind("<Return>", self.stop_camera)  # Enter key

        def update_frame():
            ret, frame = self.video_cap.read() 
            # if not ret:
            #     messagebox.showerror("Camera Error", "Unable to read from camera.")
            #     return
            if ret:
                frame = recognize(frame, clf, faceCascade)
                rgb_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(rgb_img)
                imgtk = ImageTk.PhotoImage(image=img)
                self.cam_label.imgtk = imgtk
                self.cam_label.configure(image=imgtk)
            self.cam_label.after(10, update_frame)

        update_frame()

    def stop_camera(self, event=None):
        if self.video_cap and self.video_cap.isOpened():
            self.video_cap.release()
            self.cam_label.config(image='')  # Clear image
            self.root.unbind("<Return>")
            messagebox.showinfo("Camera", "📷 Camera stopped.")



# header function

    def home(self):
        if self.video_cap and self.video_cap.isOpened():
            self.video_cap.release()
        self.root.destroy()
        os.system("main.py") 

    def help_desk1(self):
        if self.video_cap and self.video_cap.isOpened():
            self.video_cap.release()
        self.root.destroy()
        os.system("help_desk.py")

    def about(self):
        if self.video_cap and self.video_cap.isOpened():
            self.video_cap.release()
        self.root.destroy()
        os.system("about.py")




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()

