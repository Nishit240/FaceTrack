from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from tkinter import messagebox

class HelpDesk:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x1000+0+0")
        self.root.title("FaceTrack")
        self.root.configure(bg="#0f0f0f")

        # ========== HEADER ==========
        header = Frame(self.root, bg="#121416", height=60)
        header.place(x=0, y=0, width=1550, height=60)

        logo_lbl = Label(header, text="FaceTrack", font=("Helvetica", 16, "bold"), fg="white", bg="#121416")
        logo_lbl.place(x=30, y=15)

        menu_font = ("Helvetica", 11)
        Button(header, text="Home", font=menu_font, fg="white", bg="#121416", bd=0,
            command=self.home).place(x=1240, y=18)
        Button(header, text="About", font=menu_font, fg="white", bg="#121416", bd=0, command=self.about).place(x=1310, y=18)
        Button(header, text="Help", font=menu_font, fg="white", bg="#121416", bd=0).place(x=1380, y=18)
        profile_icon = Label(header, text="👤", font=("Arial", 14), fg="white", bg="#121416")
        profile_icon.place(x=1450, y=16)

        # ========== SCROLLABLE MAIN FRAME ==========
        canvas = Canvas(self.root, bg="#0f0f0f", highlightthickness=0)
        scrollbar = Scrollbar(self.root, orient=VERTICAL, command=canvas.yview)
        self.scrollable_frame = Frame(canvas, bg="#0f0f0f")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.place(x=0, y=60, width=1535, height=940)
        scrollbar.place(x=1535, y=60, height=940)

        # ========== Page Content ==========
        Label(self.scrollable_frame, text="Help Desk", font=("Helvetica", 24, "bold"), bg="#0f0f0f", fg="white").pack(anchor=W, padx=100, pady=(20, 10))
        Label(self.scrollable_frame, text="Find answers to common questions or contact our support team for assistance.",
              font=("Helvetica", 13), bg="#0f0f0f", fg="white").pack(anchor=W, padx=100, pady=(0, 30))

        # ========== FAQs ==========
        faq_frame = Frame(self.scrollable_frame, bg="#0f0f0f")
        faq_frame.pack(fill=X, padx=100, pady=(0, 40))

        Label(faq_frame, text="Frequently Asked Questions", font=("Segoe UI", 20, "bold"), bg="#0f0f0f", fg="white").pack(anchor=W)

        faqs = [
            ("How do I enroll students in the system?",
             "Navigate to the 'Student Detail' page, fill out the form, and click Save. Use the camera to capture a face sample."),
            ("What if the system fails to recognize a face?",
             "Make sure the face sample was captured properly and in good lighting. Re-enroll the student if needed."),
            ("How can I export attendance reports?",
             "Go to the 'Attendance' section and click 'Export CSV' to download the current record as a file.")
        ]

        for q, a in faqs:
            frame = Frame(faq_frame, bg="#1e1e1e", bd=1, relief=SOLID)
            frame.pack(fill=X, pady=8)
            Label(frame, text=q, font=("Helvetica", 12, "bold"), bg="#1e1e1e", fg="white").pack(anchor=W, padx=10, pady=5)
            Label(frame, text=a, font=("Helvetica", 11), bg="#1e1e1e", fg="white").pack(anchor=W, padx=10, pady=(0, 5))

        # ========== Contact Support ==========
        contact_frame = Frame(self.scrollable_frame, bg="#0f0f0f")
        contact_frame.pack(fill=X, padx=100)

        Label(contact_frame, text="Contact Support", font=("Helvetica", 20, "bold"), bg="#0f0f0f", fg="white").pack(anchor=W)
        Label(contact_frame, text="If you need further help, please reach out below.",
              font=("Helvetica", 12), bg="#0f0f0f", fg="white").pack(anchor=W)

        # Email Label and Entry
        Label(contact_frame, text="Enter your email:", font=("Helvetica", 13, "bold"), bg="#0f0f0f", fg="white").pack(anchor=W, pady=(10, 0))
        self.email_entry = Entry(contact_frame, font=("Helvetica", 12), bg="#2a2a2a", fg="white", insertbackground='white')
        self.email_entry.pack(fill=X, pady=(5, 10))
        self.email_entry.insert(0, "")

        # Description Label and Text Box
        Label(contact_frame, text="Describe your issue:", font=("Helvetica", 13, "bold"), bg="#0f0f0f", fg="white").pack(anchor=W, pady=(5, 0))
        self.message_entry = Text(contact_frame, height=5, font=("Helvetica", 12), bg="#2a2a2a", fg="white", insertbackground='white')
        self.message_entry.pack(fill=X, pady=(5, 10))
        self.message_entry.insert(1.0, "")


        submit_btn = Button(contact_frame, text="Submit", font=("Helvetica", 12, "bold"), bg="#C1C1C1", fg="black",
                            command=self.submit_form)
        submit_btn.pack(pady=(0, 30))

    def submit_form(self):
        email = self.email_entry.get()
        message = self.message_entry.get("1.0", END).strip()
        if not email or email == "Enter your email" or not message or message == "Describe your issue":
            messagebox.showwarning("Missing Information", "Please fill out both fields.", parent=self.root)
        else:
            messagebox.showinfo("Submitted", "Your message has been sent! We will contact you soon.", parent=self.root)
            self.email_entry.delete(0, END)
            self.message_entry.delete("1.0", END)

    
    
    def home(self):
        self.root.destroy()
        os.system("main.py")

    def about(self):
        self.root.destroy()
        os.system("about.py")


if __name__ == "__main__":
    root = Tk()
    app = HelpDesk(root)
    root.mainloop()
