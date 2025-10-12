from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import mysql.connector


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x1000+0+0")
        self.root.title("FaceTrack")
        self.root.configure(bg="#0f0f0f")


        #=============variables===================

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


         # Background image
        img3 = Image.new("RGB", (1550, 1000), color="#0f0f0f")
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1550, height=1000)

        #Title
        Label(self.root, text="Student Detail", font=("Helvetica", 26, "bold"), bg="#0f0f0f", fg="white").place(x=50, y=4)


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





        #frame
        main_frame=Frame(bg_img,bd=2, bg="#0f0f0f")
        main_frame.place(x=10,y=50,width=1500,height=770)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("TLabel", background="#C1C1C1", foreground="white")
        style.configure("TFrame", background="#C1C1C1")
        style.configure("TLabelFrame", background="#C1C1C1", foreground="white")
        style.configure("TCombobox", fieldbackground="#C1C1C1", background="#C1C1C1", foreground="Black", arrowcolor="black")
        style.configure("TEntry", fieldbackground="#C1C1C1", background="#0f0f0f39", foreground="Black")

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2, bg="#0f0f0f", relief=RIDGE, text="STUDENT ATTENDENCE DETAILS", font=("times new roman", 12, "bold"), fg="white")
        Left_frame.place(x=30,y=30,width=700,height=730)

        # Student image in left frame
        img_left = Image.open(r"C:\Users\NISHIT JAIN\OneDrive\Desktop\face recognition system\image\studentdetail.jpg")
        img_left = img_left.resize((670, 190), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left, bg="#0f0f0f")
        f_lbl.place(x=10, y=0, width=670, height=190)

        #current Course
        current_course_frame=LabelFrame(Left_frame,bd=2, bg="#0f0f0f", relief=RIDGE, text=" CURRENT COURSE INFORMATION", font=("times new roman", 12, "bold"), fg="white")
        current_course_frame.place(x=10,y=200,width=670,height=150)

        #Department
        dept_lable = Label(current_course_frame,  text="Department:", font=("times new roman", 12, "bold"), bg="#0f0f0f", fg="white")
        dept_lable.grid(row=0, column=0, padx=10, pady=20, sticky=W)

        dept_combo=ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"),state="readonly", width=20)
        dept_combo["values"]=("Select Department", "CS", "IT", "CIVIL", "MECHANICAL")
        dept_combo.current(0)
        dept_combo.grid(row=0,column=1,  padx=10, pady=20, sticky=W)

        #Course
        course_lable = Label(current_course_frame,  text="Course:", font=("times new roman", 12, "bold"), bg="#0f0f0f", fg="white")
        course_lable.grid(row=0, column=2, padx=10, pady=20, sticky=W)

        course_combo=ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 12, "bold"),state="readonly", width=20)
        course_combo["values"]=("Select Course", "BE", "B.TECH", "M.TECH")
        course_combo.current(0)
        course_combo.grid(row=0,column=3, padx=10, pady=20, sticky=W)

        #Year
        year_lable = Label(current_course_frame,  text="Year:", font=("times new roman", 12, "bold"), bg="#0f0f0f", fg="white")
        year_lable.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        year_combo=ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"),state="readonly", width=20)
        year_combo["values"]=("Select Year", "2022-23", "2023-24","2024-25","2025-26")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,  padx=10, pady=10, sticky=W)

        #Semester
        semester_lable = Label(current_course_frame,  text="Semester:", font=("times new roman", 12, "bold"), bg="#0f0f0f", fg="white")
        semester_lable.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        semester_combo=ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("times new roman", 12, "bold"),state="readonly", width=20)
        semester_combo["values"]=("Select Semester", "Sem-1", "Sem-2", "Sem-3", "Sem-4")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,  padx=10, pady=10, sticky=W)



        #Class student information
        class_Student_frame = LabelFrame(Left_frame, bd=2, bg="#0f0f0f", relief=RIDGE, text=" CLASS STUDENT INFORMATION", font=("times new roman", 12, "bold"), fg="white")
        class_Student_frame.place(x=10, y=370, width=670, height=320)

        # Uniform field width
        field_font = ("times new roman", 12, "bold")

        # Student ID
        studentId_lable = Label(class_Student_frame, text="Student ID:", font=field_font, bg="#0f0f0f", fg="white")
        studentId_lable.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        
        studentId_entry = ttk.Entry(class_Student_frame, width=20, font=field_font, textvariable=self.var_std_id)
        studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        studentName_lable = Label(class_Student_frame, text="Student Name:", font=field_font, bg="#0f0f0f", fg="white")
        studentName_lable.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        
        studentName_entry = ttk.Entry(class_Student_frame, width=20, font=field_font, textvariable=self.var_std_name)
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division
        class_div_lable = Label(class_Student_frame, text="Class Division:", font=field_font, bg="#0f0f0f", fg="white")
        class_div_lable.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        
        class_div_combo = ttk.Combobox(class_Student_frame, width=18, font=field_font, state="readonly", textvariable=self.var_div, style="Black.TCombobox")
        class_div_combo["values"] = ("Select Division", "A", "B", "C", "D")
        class_div_combo.current(0)
        class_div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll No
        roll_no_lable = Label(class_Student_frame, text="Roll No:", font=field_font, bg="#0f0f0f", fg="white")
        roll_no_lable.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        
        roll_no_entry = ttk.Entry(class_Student_frame, width=20,font=field_font, textvariable=self.var_roll)
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_lable = Label(class_Student_frame, text="Gender:", font=field_font, bg="#0f0f0f", fg="white")
        gender_lable.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        
        gender_combo = ttk.Combobox(class_Student_frame, width=18, font=field_font, state="readonly", textvariable=self.var_gender, style="Black.TCombobox")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB
        dob_label = Label(class_Student_frame, text="DOB:", font=field_font, bg="#0f0f0f", fg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        
        dob_entry = DateEntry(class_Student_frame, width=18, font=field_font, background="#0f0f0f", foreground="white", borderwidth=2, date_pattern="yyyy-mm-dd", textvariable=self.var_dob)
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
        dob_entry.delete(0, 'end')

        # Email
        email_label = Label(class_Student_frame, text="Email:", font=field_font, bg="#0f0f0f", fg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        
        email_entry = ttk.Entry(class_Student_frame, width=20, font=field_font, textvariable=self.var_email)
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone No
        phone_label = Label(class_Student_frame, text="Phone No:", font=field_font, bg="#0f0f0f", fg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        
        phone_entry = ttk.Entry(class_Student_frame, width=20, font=field_font, textvariable=self.var_phone)
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(class_Student_frame, text="Address:", font=field_font, bg="#0f0f0f", fg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        
        address_entry = ttk.Entry(class_Student_frame, width=20, font=field_font, textvariable=self.var_address)
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name
        teacher_label = Label(class_Student_frame, text="Teacher Name:", font=field_font, bg="#0f0f0f", fg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        
        teacher_entry = ttk.Entry(class_Student_frame, width=20, font=field_font, textvariable=self.var_teacher)
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)




        # Shared variable for selection
        self.var_radio1 = StringVar()
        self.var_radio1.set("")

        # Radio Buttons
        # Define TRadiobutton style
        style.configure("Custom.TRadiobutton", background="#0f0f0f", foreground="white")

        # On hover (active), change foreground to black
        style.map("Custom.TRadiobutton",
                foreground=[("active", "black")],
                background=[("active", "#ffffff")])  # keep background same or modify if needed

        # Use the custom style in your Radiobuttons
        radiobtn1 = ttk.Radiobutton(class_Student_frame, text="Take Photo Sample", variable=self.var_radio1, value="Yes", style="Custom.TRadiobutton")
        radiobtn1.grid(row=6, column=0, padx=10, pady=5, sticky=W)

        radiobtn2 = ttk.Radiobutton(class_Student_frame, text="No Photo Sample", variable=self.var_radio1, value="No", style="Custom.TRadiobutton")
        radiobtn2.grid(row=6, column=1, padx=10, pady=5, sticky=W)





        # Button Frame 1: Save, Update, Delete, Reset
        btn_frame = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="#0f0f0f") 
        btn_frame.place(x=0, y=200, width=660, height=35)  # width=660 to avoid slight overflow

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=17, font=field_font, bg="#C1C1C1", fg="black")
        save_btn.grid(row=0, column=0, padx=2)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=17, font=field_font, bg="#C1C1C1", fg="black")
        update_btn.grid(row=0, column=1, padx=2)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=17, font=field_font, bg="#C1C1C1", fg="black")
        delete_btn.grid(row=0, column=2, padx=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data ,width=17, font=field_font, bg="#C1C1C1", fg="black")
        reset_btn.grid(row=0, column=3, padx=2)

        # Button Frame 2: Take Photo / Update Photo
        btn_frame1 = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="#0f0f0f") 
        btn_frame1.place(x=0, y=240, width=660, height=35)

        take_photo_btn = Button(btn_frame1, command=self.generate_dataset, text="Take Photo Sample", width=35, font=field_font, bg="#C1C1C1", fg="black")
        take_photo_btn.grid(row=0, column=0, padx=2)

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=35, font=field_font, bg="#C1C1C1", fg="black")
        update_photo_btn.grid(row=0, column=1, padx=2)



        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2, bg="#0f0f0f", relief=RIDGE, text="STUDENT DETAILS", fg="white", font=field_font)
        Right_frame.place(x=760,y=30,width=700,height=730)

        

        # Student image in right frame
        img_right = Image.open(r"C:\Users\NISHIT JAIN\OneDrive\Desktop\face recognition system\image\studentdetail.jpg")
        img_right = img_right.resize((670, 190), Image.LANCZOS)  # Resize to button size
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=10, y=0, width=670, height=190)


        #=============Search System===================

        Search_frame=LabelFrame(Right_frame,bd=2, bg="#0f0f0f", fg="white", relief=RIDGE, text="SEARCH SYSTEM", font=field_font)
        Search_frame.place(x=10,y=200,width=670,height=70)

        search_label = Label(Search_frame, text="Search By:", font=field_font, bg="#0f0f0f", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=field_font,state="readonly", width=15)
        search_combo["values"]=("Select", "Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,  padx=10, pady=5, sticky=W)

        search_entry = ttk.Entry(Search_frame, width=20, font=field_font)
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(Search_frame, text="Search", width=10, font=field_font, bg="#C1C1C1", fg="black")
        search_btn.grid(row=0, column=3, padx=2)

        showAll_btn = Button(Search_frame, text="Show All", width=10, font=field_font, bg="#C1C1C1", fg="black")
        showAll_btn.grid(row=0, column=4, padx=2)

        
        #=============Table Frame ===================

        table_frame=Frame(Right_frame,bd=2, bg="#0f0f0f", relief=RIDGE,)
        table_frame.place(x=10,y=290,width=670,height=400)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        style.configure("Treeview",
                        background="#0f0f0f",
                        foreground="white",
                        fieldbackground="#0f0f0f",
                        bordercolor="#C1C1C1",
                        borderwidth=1)

        style.configure("Treeview.Heading",
                        background="#C1C1C1",
                        foreground="black",
                        font=("times new roman", 12, "bold"))

        self.student_table = ttk.Treeview(table_frame,
            columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone", "address","teacher","photo"),
            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set, style="Treeview")

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.pack(fill=BOTH, expand=1)

        for col in ("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone", "address","teacher","photo"):
            self.student_table.heading(col, text=col.capitalize())
            self.student_table["show"]="headings"
            self.student_table.column(col, width=100)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No.")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.featch_data()


    #=============Function declaration===================

    def add_data(self):
        if self.var_dep.get() == "Select Department":
            messagebox.showerror("ERROR", "Please select a department.", parent=self.root)

        elif self.var_course.get() == "Select Course":
            messagebox.showerror("ERROR", "Please select a course.", parent=self.root)

        elif self.var_year.get() == "Select Year":
            messagebox.showerror("ERROR", "Please select an academic year.", parent=self.root)

        elif self.var_semester.get() == "Select Semester":
            messagebox.showerror("ERROR", "Please select a semester.", parent=self.root)

        elif self.var_std_id.get() == "":
            messagebox.showerror("ERROR", "Student ID is required.", parent=self.root)

        elif not self.var_std_id.get().isdigit():
            messagebox.showerror("ERROR", "Student ID must be numeric.", parent=self.root)

        elif self.var_std_name.get() == "":
            messagebox.showerror("ERROR", "Student name is required.", parent=self.root)

        elif self.var_div.get() == "":
            messagebox.showerror("ERROR", "Class division is required.", parent=self.root)

        elif self.var_roll.get() == "":
            messagebox.showerror("ERROR", "Roll number is required.", parent=self.root)

        elif self.var_gender.get() == "Select Gender":
            messagebox.showerror("ERROR", "Please select gender.", parent=self.root)

        elif self.var_dob.get() == "":
            messagebox.showerror("ERROR", "Date of birth is required.", parent=self.root)

        elif self.var_email.get() == "":
            messagebox.showerror("ERROR", "Email is required.", parent=self.root)

        elif self.var_phone.get() == "":
            messagebox.showerror("ERROR", "Phone number is required.", parent=self.root)

        elif not self.var_phone.get().isdigit() or len(self.var_phone.get()) != 10:
            messagebox.showerror("ERROR", "Enter a valid 10-digit phone number.", parent=self.root)

        elif self.var_address.get() == "":
            messagebox.showerror("ERROR", "Address is required.", parent=self.root)

        elif self.var_teacher.get() == "":
            messagebox.showerror("ERROR", "Teacher name is required.", parent=self.root)


        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.featch_data()
                conn.close()
                messagebox.showinfo("SUCCESS", "DATA IS ADDED")
            except Exception as es:
                messagebox.showerror("Database Error", f"Error: {str(es)}", parent=self.root)


    #=============Fetch Data===================
    def featch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student")
        data=my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #============get Cursor===================
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])


    #============Update data===================

    def update_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Please select a student record to update", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student's record?", parent=self.root)
                if update:
                    conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
                    my_cursor = conn.cursor()

                    query = """
                        UPDATE student SET 
                            dep = %s,
                            course = %s,
                            year = %s,
                            semester = %s,
                            name = %s,
                            division = %s,
                            roll = %s,
                            gender = %s,
                            dob = %s,
                            email = %s,
                            phone = %s,
                            address = %s,
                            teacher = %s,
                            photoSample = %s
                        WHERE student_id = %s
                    """

                    values = (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    )

                    my_cursor.execute(query, values)
                    conn.commit()
                    self.featch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student record updated successfully", parent=self.root)
                else:
                    return
            except Exception as es:
                messagebox.showerror("Database Error", f"Error: {str(es)}", parent=self.root)

    #============Delete Data===================
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Please select a student record to delete", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you really want to delete this student?", parent=self.root)
                if delete:
                    conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("DELETE FROM student WHERE student_id = %s", (self.var_std_id.get(),))
                    conn.commit()
                    self.featch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student record deleted successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Database Error", f"Error: {str(es)}", parent=self.root)

    #============Reset Data===================

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    #===========Generate data set or Take photo sample===================

    def generate_dataset(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Please select a student record to update", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face_recognizer")
                my_cursor = conn.cursor()

                id = self.var_std_id.get()


                my_cursor.execute(
                        """UPDATE student SET 
                            dep = %s,
                            course = %s,
                            year = %s,
                            semester = %s,
                            name = %s,
                            division = %s,
                            roll = %s,
                            gender = %s,
                            dob = %s,
                            email = %s,
                            phone = %s,
                            address = %s,
                            teacher = %s,
                            photoSample = %s
                        WHERE student_id = %s
                    """, (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                conn.commit()
                self.featch_data()
                
                conn.close()

            
        
#============load predifined data on face ===================

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor=1.3 minimum Neighbour=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+= 1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)                    
                        # file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        file_name_path = "data/user." + str(self.var_std_id.get()) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                self.reset_data()
                messagebox.showinfo("Result","Generating Data sets Completed!!!")

            except Exception as es:
                messagebox.showerror("Database Error", f"Error: {str(es)}", parent=self.root)


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
    OBJ = Student(root)
    root.mainloop()
