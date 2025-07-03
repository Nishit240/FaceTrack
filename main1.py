from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from train import Train 
from face_recognition import Face_Recognition
from attendance import Attendance
import os

class face_recognition_system:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x1000+0+0")
        self.root.title("FaceTrack")

        # Background image
        img3 = Image.open(r"C:\Users\NISHIT JAIN\OneDrive\Desktop\face recognition system\image\bg.jpg")
        img3 = img3.resize((1550, 1000), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1550, height=1000)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM",
                          font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1550, height=45)

        # ========== Student button ==========
        img4 = Image.open(r"C:\Users\NISHIT JAIN\OneDrive\Desktop\face recognition system\image\student.jpeg")
        img4 = img4.resize((220, 220), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        btn_student = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        btn_student.place(x=200, y=100, width=220, height=220)

        btn_student_text = Button(bg_img, text="STUDENT DETAILS", command=self.student_details,
                                  cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="black")
        btn_student_text.place(x=200, y=315, width=220, height=40)

        # ========== Face Recognition button ==========
        img5 = Image.open(r"C:\Users\NISHIT JAIN\OneDrive\Desktop\face recognition system\image\Face-Detection.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        btn_face = Button(bg_img, image=self.photoimg5, command=self.face_recognition, cursor="hand2")
        btn_face.place(x=650, y=100, width=220, height=220)

        btn_face_text = Button(bg_img, text="FACE RECOGNITION", command=self.face_recognition, cursor="hand2",
                               font=("times new roman", 15, "bold"), bg="white", fg="black")
        btn_face_text.place(x=650, y=315, width=220, height=40)

        # ========== Attendance button ==========
        img6 = Image.open(r"C:\Users\NISHIT JAIN\OneDrive\Desktop\face recognition system\image\attendance.png")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        btn_attendance = Button(bg_img, image=self.photoimg6, command=self.attendance_data, cursor="hand2" )
        btn_attendance.place(x=1100, y=100, width=220, height=220)

        btn_attendance_text = Button(bg_img, text="ATTENDANCE", cursor="hand2", command=self.attendance_data,
                                     font=("times new roman", 15, "bold"), bg="white", fg="black")
        btn_attendance_text.place(x=1100, y=315, width=220, height=40)

        # ========== Train Data button ==========
        img7 = Image.open(r"C:\Users\NISHIT JAIN\OneDrive\Desktop\face recognition system\image\TRAIN DATA.png")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        btn_train = Button(bg_img, image=self.photoimg7,command=self.train_data,  cursor="hand2")
        btn_train.place(x=200, y=500, width=220, height=220)

        btn_train_text = Button(bg_img, command=self.train_data,  text="TRAIN DATA", cursor="hand2",
                                font=("times new roman", 15, "bold"), bg="white", fg="black")
        btn_train_text.place(x=200, y=715, width=220, height=40)

        # ========== Photos button ==========
        img8 = Image.open(r"C:\Users\NISHIT JAIN\OneDrive\Desktop\face recognition system\image\PHOTO.jpeg")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        btn_photos = Button(bg_img, image=self.photoimg8, command=self.open_img, cursor="hand2")

        btn_photos.place(x=650, y=500, width=220, height=220)

        btn_photos_text = Button(bg_img, text="PHOTOS", command=self.open_img, cursor="hand2",
                                 font=("times new roman", 15, "bold"), bg="white", fg="black")
        btn_photos_text.place(x=650, y=715, width=220, height=40)

        # ========== Developer button ==========
        img9 = Image.open(r"C:\Users\NISHIT JAIN\OneDrive\Desktop\face recognition system\image\Developer.jpg")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        btn_developer = Button(bg_img, image=self.photoimg9, cursor="hand2")
        btn_developer.place(x=1100, y=500, width=220, height=220)

        btn_developer_text = Button(bg_img, text="DEVELOPER", cursor="hand2",
                                    font=("times new roman", 15, "bold"), bg="white", fg="black")
        btn_developer_text.place(x=1100, y=715, width=220, height=40)



    def open_img(self):
        os.startfile(r"C:\Users\NISHIT JAIN\OneDrive\Desktop\face recognition system\data")


    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)


    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)


    def face_recognition(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)



if __name__ == "__main__":
    root = Tk()
    OBJ = face_recognition_system(root)
    root.mainloop()
