from tkinter import *
from PIL import Image, ImageTk
import tkinter
from student import Student
import os

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x1000+0+0")
        self.root.title("FaceTrack")
        self.root.configure(bg="#0f0f0f")  # dark background

        self.session_attendance_set = set()

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

        # ===== TITLE =====
        Label(self.root, text="DASHBOARD", font=("Helvetica", 28, "bold"), bg="#0f0f0f", fg="white").place(x=100, y=90)

        # ===== GRID BUTTONS =====
        button_data = [
            {
                "image": "student.jpeg",
                "text": "STUDENT DETAILS",
                "command": self.student_details,
                "x": 250, "y": 160
            },
            {
                "image": "Face-Detection.jpg",
                "text": "FACE RECOGNITION",
                "command": self.face_recognition,
                "x": 540, "y": 160
            },
            {
                "image": "attendance.jpg",
                "text": "ATTENDANCE",
                "command": self.attendance_data,
                "x": 830, "y": 160
            },
            {
                "image": "TRAIN DATA.png",
                "text": "TRAIN DATA",
                "command": self.train_data,
                "x": 1120, "y": 160
            },
            {
                "image": "PHOTO.jpeg",
                "text": "PHOTOS",
                "command": self.open_img,
                "x": 395, "y": 430
            },
            {
                "image": "Developer.jpg",
                "text": "HELP DESK",
                "command": self.help_desk1,
                "x": 685, "y": 430
            },
            {
                "image": "exit.jpg",
                "text": "EXIT",
                "command": self.iExit,
                "x": 975, "y": 430
            }
        ]

        for btn in button_data:
            img_path = os.path.join("image", btn["image"])
            image = Image.open(img_path).resize((200, 200), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            img_lbl = Label(self.root, image=photo, bg="#0f0f0f")
            img_lbl.image = photo
            img_lbl.place(x=btn["x"], y=btn["y"], width=200, height=200)

            Button(self.root, image=photo, command=btn["command"] if btn["command"] else lambda: None,
                   cursor="hand2", bd=0, bg="#0f0f0f", activebackground="#0f0f0f").place(x=btn["x"], y=btn["y"], width=200, height=200)

            Label(self.root, text=btn["text"], font=("Helvetica", 12, "bold"),
                  bg="#0f0f0f", fg="white").place(x=btn["x"] + 10, y=btn["y"] + 210, width=180)

    # ===== Button Commands =====
    def open_img(self):
        os.startfile(r"C:\Users\NISHIT JAIN\OneDrive\Desktop\face recognition system\data")

    def student_details(self):
        self.root.destroy()
        os.system("student.py")

    def train_data(self):
        self.root.destroy()
        os.system("train.py")

    def face_recognition(self):
        self.root.destroy()
        os.system("face_recognition.py")

    def attendance_data(self):
        self.root.destroy()
        os.system("attendance.py")

    
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno ("Face Recognition", "Are you sure exit this project", parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return

# header function

    def home(self):
        self.root.destroy()
        os.system("main.py") 

    def help_desk1(self):
        self.root.destroy()
        os.system("help_desk.py")
        
    def about(self):
        self.root.destroy()
        os.system("about.py")
if __name__ == "__main__":
    root = Tk()
    app = FaceRecognitionSystem(root)
    root.mainloop()

