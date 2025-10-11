from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os

class AboutPage:
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

        # ========== Content Frame ==========
        content = Frame(self.root, width=1550, bg="#0f0f0f")
        content.place(x=100, y=90, width=1550, height=930)  


        Label(content, text="About Face Attendance System", font=("Helvetica", 20, "bold"), bg="#0f0f0f", fg="white").pack(anchor=W, pady=(0, 15))

        # -------- Purpose Section --------
        Label(content, text="Purpose", font=("Helvetica", 16, "bold"), bg="#0f0f0f", fg="white").pack(anchor=W)
        Label(content, text="FaceTrack is a smart attendance management system that leverages real-time facial recognition"
                            "to automate the process of marking and tracking student attendance.\n" "It provides institutions with an efficient, secure, and user-friendly solution to eliminate manual errors and save time.",
              font=("Helvetica", 13), bg="#0f0f0f", fg="#FFFFFF", justify=LEFT).pack(anchor=W, pady=5)

        # -------- Features Section --------
        Label(content, text="\nKey Features", font=("Helvetica", 16, "bold"), bg="#0f0f0f", fg="white").pack(anchor=W)

        features = [
            ("🧠       Face Recognition", "       Detects and recognizes student faces using computer vision for seamless attendance logging."),
            ("⚡     Automated Logging", "       Attendance is marked instantly once the face is verified, no need for manual input."),
            ("📂      CSV Import & Export", "      Easily import past records or export daily logs to CSV files for analysis."),
            ("📆      Daily Logs", "      View and manage daily attendance records with photo references."),
            ("🖼️ Photo Mapping", "      Links attendance records to stored face images for better validation."),
            
        ]

        for icon, text in features:
            Label(content, text=icon, font=("Helvetica", 13), bg="#0f0f0f", fg="white").pack(anchor=W, padx=10, pady=(10, 0))
            Label(content, text=text, font=("Helvetica", 11), bg="#0f0f0f", fg="#FFFFFF").pack(anchor=W, padx=30)

        # -------- Development Team --------
        Label(content, text="\nDeveloped By", font=("Helvetica", 16, "bold"), bg="#0f0f0f", fg="white").pack(anchor=W)
        Label(content, text="This system, designed and developed by Nishit Jain, serves as a practical demonstration of Python's core concepts, coupled with real-world applications of Tkinter,\n" "OpenCV, and efficient CSV data handling.",
              font=("Helvetica", 13), bg="#0f0f0f", fg="#FFFFFF", justify=LEFT).pack(anchor=W, pady=5)

        # -------- Legal Section --------
        Label(content, text="\nLegal and Policy Notice", font=("Helvetica", 16, "bold"), bg="#0f0f0f", fg="white").pack(anchor=W)
        Label(content, text="FaceTrack is a project developed for academic and educational purposes. Users are responsible"
                            "for handling data in compliance with their institutional privacy policies.\nThis system does not"
                            "transmit or store any data externally.",
              font=("Helvetica", 13), bg="#0f0f0f", fg="#FFFFFF", justify=LEFT).pack(anchor=W, pady=5)

   
   
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
    app = AboutPage(root)
    root.mainloop()
