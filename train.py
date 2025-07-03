from tkinter import *
from PIL import Image
from tkinter import messagebox
import os
import numpy as np
import cv2

#  LBPH (Local Binary Patterns Histograms) algorithm openCV

class Train:
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
            command=self.home).place(x=1090, y=18)

        Button(header, text="Student Detail", font=menu_font, fg="white", bg="#121416", bd=0,
            command=self.student_details).place(x=1150, y=18)

        Button(header, text="Attendance", font=menu_font, fg="white", bg="#121416", bd=0,
            command=self.attendance_data).place(x=1260, y=18)

        Button(header, text="Face Recog", font=menu_font, fg="white", bg="#121416", bd=0,
            command=self.face_recog).place(x=1350, y=18)

        profile_icon = Label(header, text="👤", font=("Arial", 14), fg="white", bg="#121416")
        profile_icon.place(x=1450, y=16)


        # ========== TITLES & SUBHEADINGS ==========
        Label(self.root, text="Training Data", font=("Helvetica", 26, "bold"), bg="#0f0f0f", fg="white").place(x=50, y=70)

        Label(self.root, text="Manage the data used for face recognition training.",
              font=("Helvetica", 13), bg="#0f0f0f", fg="gray").place(x=50, y=120)


        self.status_frame = Frame(self.root, bg="#1e1e1e", bd=2, relief=RIDGE)
        self.status_frame.place(relx=0.5, y=415, anchor=CENTER, width=500, height=530)

        self.status_lbl = Label(self.status_frame, text="Training...", font=("Helvetica", 14, "bold"), bg="#1e1e1e", fg="white")
        self.status_lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

        # ========== TRAIN BUTTON ==========
        btn_train = Button(self.root, text="☞ Train Data ☜",
                           cursor="hand2", command=self.train_classifier,
                           font=("times new roman", 30, "bold"),
                           bg="#C1C1C1", fg="black")
        btn_train.place(relx=0.5, y=715, anchor=CENTER, width=400, height=60)



    def train_classifier(self):
        # Show status label
        self.status_lbl = Label(self.root, text="Training in progress...", font=("times new roman", 20, "bold"), 
                                bg="#C1C1C1", fg="blue")
        self.status_lbl.place(relx=0.5, y=130, anchor=CENTER)

        self.root.update()  # Force the GUI to refresh and show the label

        try:
            data_dir = r"C:\Users\NISHIT JAIN\OneDrive\Desktop\face recognition system\data"
            path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

            faces = []
            ids = []

            # Get screen dimensions
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()

            # Setup OpenCV window
            cv2.namedWindow("Training", cv2.WINDOW_NORMAL)
            win_width, win_height = 500, 500
            x = int((screen_width / 2) - (win_width / 2))
            y = int((screen_height / 2) - (win_height / 2))
            cv2.resizeWindow("Training", win_width, win_height)
            cv2.moveWindow("Training", x, y)

            for image in path:
                img = Image.open(image).convert('L')  # Grayscale
                imageNp = np.array(img, 'uint8')
                
                id = int(os.path.split(image)[1].split('.')[1])
            
            #[                         0                                        ][     1    ]
            # C:\Users\NISHIT JAIN\OneDrive\Desktop\face recognition system\data\user.1.1.jpg
            #                                                                    [0] [1] [2]

                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training", imageNp)
                cv2.waitKey(1)

            ids = np.array(ids)

            # Train the classifier and save
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write("classifier.xml")

            cv2.destroyAllWindows()

            # Update label to done
            self.status_lbl.config(text="Training Completed!", bg="#C1C1C1", fg="green")
            self.root.update()
            messagebox.showinfo("Result", "Training datasets Completed!!")

        except Exception as e:
            cv2.destroyAllWindows()
            self.status_lbl.config(text="Training Failed!", fg="red")
            self.root.update()
            messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")


    def student_details(self):
        self.root.destroy()
        os.system("student.py")

    def attendance_data(self):
        self.root.destroy()
        os.system("attendance.py")

    def face_recog(self):
        self.root.destroy()
        os.system("face_recognition.py")

    def home(self):
        self.root.destroy()
        os.system("main.py") 



if __name__ == "__main__":
    root = Tk()
    OBJ = Train(root)
    root.mainloop()


