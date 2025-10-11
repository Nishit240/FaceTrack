from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import csv
from tkinter import filedialog
import os
import numpy as np
from datetime import datetime

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x1000+0+0")
        self.root.title("FaceTrack")
        self.root.configure(bg="#0f0f0f")
        self.session_attendance_set = set()
        self.mydata = []

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

        # =============Title============
        title_lbl = Label(self.root, text="Attendance Record", font=("Helvetica", 26, "bold"), bg="#0f0f0f", fg="white")
        title_lbl.place(x=50, y=70)

        # ==============Frame=============
        main_frame = Frame(self.root, bd=2, bg="#0f0f0f")
        main_frame.place(x=10, y=120, width=1500, height=700)

        field_font = ("times new roman", 12, "bold")

        # ========Left label frame=========
        Left_frame = LabelFrame(main_frame, bd=2, bg="#0f0f0f", fg="white", relief=RIDGE, text="STUDENT ATTENDANCE DETAILS", font=field_font)
        Left_frame.place(x=30, y=10, width=700, height=680)

        style = ttk.Style()
        style.theme_use("default")
        style.configure("TEntry", fieldbackground="#C1C1C1", background="#0f0f0f39", foreground="Black")

        #=========== Student image in left frame===============
        img_left = Image.open(r"image/studentdetail.jpg").resize((670, 190), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=10, y=0, width=670, height=190)

        # ===============Current Course================
        left_inside_frame = LabelFrame(Left_frame, bd=2, bg="#0f0f0f", fg="white", relief=RIDGE, text=" Attendance Details", font=field_font)
        left_inside_frame.place(x=10, y=200, width=670, height=440)

        

        #===========Define StringVars============
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # ================Fields=================
        labels = ["Attendance ID:", "Roll:", "Name:", "Department:", "Time:", "Date:", "Attendance Status:"]
        variables = [
            self.var_atten_id, self.var_atten_roll, self.var_atten_name,
            self.var_atten_dep, self.var_atten_time, self.var_atten_date,
            self.var_atten_attendance
        ]
        entries = []

        for i, (label, var) in enumerate(zip(labels, variables)):
            row, col = divmod(i, 2)
            label_widget = Label(left_inside_frame, text=label, font=field_font, bg="#0f0f0f", fg="white")
            label_widget.grid(row=row, column=col * 2, padx=10, pady=10, sticky=W)

            if label == "Attendance Status:":
                entry = ttk.Combobox(left_inside_frame, width=18, font=field_font, state="readonly", textvariable=var)
                entry["values"] = ("Status", "Present", "Absent")
                entry.current(0)
            else:
                entry = ttk.Entry(left_inside_frame, width=20, font=field_font, textvariable=var)

            entry.grid(row=row, column=col * 2 + 1, padx=10, pady=10, sticky=W)
            entries.append(entry)


        #============= Buttons Frame 1==============
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="#0f0f0f")
        btn_frame.place(x=0, y=200, width=660, height=70)

        Button(btn_frame, text="Import csv", width=35, font=field_font, bg="#C1C1C1", fg="Black", command=self.import_csv).grid(row=0, column=0, padx=2)
        Button(btn_frame, text="Export csv", width=35, font=field_font, command=self.export_csv, bg="#C1C1C1", fg="Black").grid(row=0, column=1, padx=2)
        Button(btn_frame, text="Update", width=35, font=field_font, command=self.update_data, bg="#C1C1C1", fg="Black").grid(row=1, column=0, padx=2)
        Button(btn_frame, text="Reset", width=35, font=field_font, command=self.reset_data,bg="#C1C1C1", fg="Black").grid(row=1, column=1, padx=2)

        #============== Button Frame 2===============
        btn_frame1 = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="#0f0f0f")
        btn_frame1.place(x=0, y=270, width=660, height=35)

        Button(btn_frame1, text="View Today's Log", width=73, font=field_font, bg="#C1C1C1", fg="Black", command=self.view_today_attendance).grid(row=0, column=0, padx=2)

        # ===============Right label frame==========
        Right_frame = LabelFrame(main_frame, bd=2, bg="#0f0f0f", fg="white", relief=RIDGE, text="Attendance Detail", font=field_font)
        Right_frame.place(x=760, y=10, width=700, height=680)

        #=============Table frame==============
        table_frame=Frame(Right_frame,bd=2, bg="#0f0f0f", relief=RIDGE,)
        table_frame.place(x=15, y=5, width=670, height=630)

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

        self.attendance_Report_table = ttk.Treeview(table_frame,
            columns=("id", "roll", "name", "department", "time", "date", "attendance", "photo"),
            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_Report_table.xview)
        scroll_y.config(command=self.attendance_Report_table.yview)
        self.attendance_Report_table.pack(fill=BOTH, expand=1)

        for col in ("id", "roll", "name", "department", "time", "date", "attendance", "photo"):
            self.attendance_Report_table.heading(col, text=col.capitalize())
            self.attendance_Report_table["show"]="headings"
            self.attendance_Report_table.column(col, width=100)

            self.attendance_Report_table.bind("<ButtonRelease>", self.get_cursor)



#====================function ===================
    def view_today_attendance(self):
        now = datetime.now()
        d1 = now.strftime("%d-%m-%Y")
        filename = os.path.join("logs", f"attendance_{d1}.csv")

        if not os.path.exists(filename):
            messagebox.showinfo("No Log", "No attendance marked yet for today.")
            return

        for item in self.attendance_Report_table.get_children():
            self.attendance_Report_table.delete(item)

        with open(filename, "r") as f:
            lines = f.readlines()[1:]
            for line in lines:
                row = line.strip().split(",")
                if len(row) == 7:
                    name_folder = row[2].replace(" ", "_")
                    photo_path = os.path.join(name_folder, f"user.{row[0]}.1")
                    self.attendance_Report_table.insert("", "end", values=row + [photo_path])

    #==================Import csv==================
    def import_csv(self):
        file_path = filedialog.askopenfilename(
            initialdir=r"C:\Users\NISHIT JAIN\OneDrive\Desktop\face recognition system\logs",
            title="Open CSV File",
            filetypes=(("CSV File", "*.csv"), ("All Files", "*.*"))
        )
        if not file_path:
            return

        self.mydata = []  # Reset before loading new data

        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header if present
            self.attendance_Report_table.delete(*self.attendance_Report_table.get_children())  # Clear table
            for row in reader:
                if len(row) == 7:
                    photo_path = os.path.join("dataset", f"user.{row[0]}.1.jpg")
                    self.attendance_Report_table.insert("", "end", values=row + [photo_path])
                    self.mydata.append(row)


    # ===============export csv=================

    def export_csv(self):
        try:
            if len(self.mydata) < 1:
                messagebox.showerror("No Data", "No Data found to export", parent=self.root)
                return False

            file_path = filedialog.asksaveasfilename(
                initialdir=r"C:\Users\NISHIT JAIN\OneDrive\Desktop\face recognition system\logs",
                title="Save CSV File",
                defaultextension=".csv",
                filetypes=(("CSV File", "*.csv"), ("All Files", "*.*"))
            )

            if file_path == "":
                return False

            with open(file_path, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in self.mydata:
                    exp_write.writerow(i)

            messagebox.showinfo("Data Export", f"Your data has been exported to '{os.path.basename(file_path)}' successfully.")

        except Exception as es:
            messagebox.showerror("Error", f"Something went wrong:\n{str(es)}")

    #============get Cursor===================

    def get_cursor(self, event=""):
        cursor_row = self.attendance_Report_table.focus()
        content = self.attendance_Report_table.item(cursor_row)
        rows = content["values"]

        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

# ========== update data ==============
    def update_data(self):
        selected = self.attendance_Report_table.focus()
        if not selected:
            messagebox.showerror("Error", "Please select a record from the table to update", parent=self.root)
            return

        try:
            update = messagebox.askyesno("Update", "Do you want to update this attendance record?", parent=self.root)
            if update:
                updated_values = [
                    self.var_atten_id.get(),
                    self.var_atten_roll.get(),
                    self.var_atten_name.get(),
                    self.var_atten_dep.get(),
                    self.var_atten_time.get(),
                    self.var_atten_date.get(),
                    self.var_atten_attendance.get()
                ]

                # Update in the table
                self.attendance_Report_table.item(selected, values=updated_values + ["dummy_photo.jpg"])

                # Update in self.mydata (match by ID or Roll)
                for i, row in enumerate(self.mydata):
                    if row[0] == self.var_atten_id.get():  # Assuming ID is unique
                        self.mydata[i] = updated_values
                        break

                messagebox.showinfo("Success", "Attendance record updated successfully", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Failed to update record:\n{str(es)}", parent=self.root)


# =============== reset ===================
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


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
    obj = Attendance(root)
    root.mainloop()