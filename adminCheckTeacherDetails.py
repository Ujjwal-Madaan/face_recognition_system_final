import numpy as np
import cv2

from tkinter import *
from tkinter import ttk  # ttk is used for styling
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os


class adminCheckTeacherDetails:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recognition Attendance System")

        # ======= Variables ============
        self.var_dep = StringVar()  # department
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_rollNum = StringVar()
        self.var_std_name = StringVar()
        self.var_batch = StringVar()
        self.var_batchNum = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_fatherNum = StringVar()
        self.var_motherNum = StringVar()

        self.var_stdIdforImage = ""

        # img1 = main background
        img1 = Image.open("Images/bg_Student.jpeg")
        img1 = img1.resize((1550, 900), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=0, width=1550, height=900)

        # title
        title_lbl = Label(
            bg_img,
            text="TEACHER MANAGEMENT SYSTEM",
            font=("times new roman", 35, "bold"),
            bg="black",
            fg="white",
        )
        title_lbl.place(x=0, y=0, width=1550, height=45)

        ##########################################################

        # main frame
        main_frame = Frame(bg_img, bd=2, bg="black")
        main_frame.place(x=34, y=70, width=1480, height=800)
        # divide into label frame in main frame .... # label frame m ham title daal skte hai

        #########################################################

        # left label frame
        Left_frame = LabelFrame(
            main_frame,
            bd=5,
            bg="white",
            relief=RAISED,
            text="Teacher Details",
            font=("times new roman", 12, "bold"),
        )
        Left_frame.place(x=10, y=10, width=700, height=777)

        img_left = Image.open("Images/db2.png")
        img_left = img_left.resize((680, 257), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=3, y=0, width=680, height=257)

        ###########################################################################

        # Teacher information
        teacher_frame = LabelFrame(
            Left_frame,
            bd=3,
            bg="white",
            relief=SUNKEN,
            text="Teacher Details",
            font=("times new roman", 12, "bold"),
        )
        teacher_frame.place(x=5, y=270, width=680, height=480)

        # teacher ID
        teacherID_label = Label(
            teacher_frame,
            text="Teacher ID",
            font=("times new roman", 17),
            bg="white",
        )
        teacherID_label.place(x=10, y=30, anchor=NW)

        teacherID_entry = ttk.Entry(
            teacher_frame,
            # textvariable=self.var_rollNum,
            width=22,
            font=("times new roman", 13),
        )
        teacherID_entry.place(x=180, y=30, anchor=NW)

        # Name
        name_label = Label(
            teacher_frame,
            text="Name",
            font=("times new roman", 17),
            bg="white",
        )
        name_label.place(x=10, y=130, anchor=NW)

        name_entry = ttk.Entry(
            teacher_frame,
            # textvariable=self.var_name,
            width=22,
            font=("times new roman", 13),
        )
        name_entry.place(x=180, y=130, anchor=NW)

        # Phone no.
        phone_label = Label(
            teacher_frame,
            text="Phone No.",
            font=("times new roman", 17),
            bg="white",
        )
        phone_label.place(x=10, y=230, anchor=NW)

        phone_entry = ttk.Entry(
            teacher_frame,
            # textvariable=self.var_rollNum,
            width=22,
            font=("times new roman", 13),
        )
        phone_entry.place(x=180, y=230, anchor=NW)

        # Email
        email_label = Label(
            teacher_frame,
            text="Email (thapar.edu)",
            font=("times new roman", 17),
            bg="white",
        )
        email_label.place(x=10, y=350, anchor=NW)

        email_entry = ttk.Entry(
            teacher_frame,
            # textvariable=self.var_rollNum,
            width=22,
            font=("times new roman", 13),
        )
        email_entry.place(x=180, y=350, anchor=NW)

        # course_1 label
        course_1_label = Label(
            teacher_frame,
            text="Course - 1",
            font=("times new roman", 17),
            bg="white",
        )
        course_1_label.place(x=380, y=30, anchor=NW)

        # combo is used for dropdown like entering text
        course_1_combo = ttk.Combobox(
            teacher_frame,
            # textvariable=self.var_memType,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        course_1_combo["values"] = (
            "",
            "UCS411 - AI",
            "UCS414 - CN",
            "UCS310 - DBMS",
            "UMA035 - OT",
            "UCS503 - SE",
        )
        course_1_combo.current(0)  # to give the bydeafault index

        course_1_combo.place(x=480, y=30, anchor=NW)

        # course_2 label
        course_2_label = Label(
            teacher_frame,
            text="Course - 2",
            font=("times new roman", 17),
            bg="white",
        )
        course_2_label.place(x=380, y=130, anchor=NW)

        # combo is used for dropdown like entering text
        course_2_combo = ttk.Combobox(
            teacher_frame,
            # textvariable=self.var_memType,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        course_2_combo["values"] = (
            "",
            "UCS411 - AI",
            "UCS414 - CN",
            "UCS310 - DBMS",
            "UMA035 - OT",
            "UCS503 - SE",
        )
        course_2_combo.current(0)  # to give the bydeafault index

        course_2_combo.place(x=480, y=130, anchor=NW)

        # course_3 label
        course_3_label = Label(
            teacher_frame,
            text="Course - 3",
            font=("times new roman", 17),
            bg="white",
        )
        course_3_label.place(x=380, y=230, anchor=NW)

        # combo is used for dropdown like entering text
        course_3_combo = ttk.Combobox(
            teacher_frame,
            # textvariable=self.var_memType,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        course_3_combo["values"] = (
            "",
            "UCS411 - AI",
            "UCS414 - CN",
            "UCS310 - DBMS",
            "UMA035 - OT",
            "UCS503 - SE",
        )
        course_3_combo.current(0)  # to give the bydeafault index

        course_3_combo.place(x=480, y=230, anchor=NW)

        # gender label
        gender_label = Label(
            teacher_frame,
            text="Gender",
            font=("times new roman", 17),
            bg="white",
        )
        gender_label.place(x=380, y=350, anchor=NW)

        # combo is used for dropdown like entering text
        gender_combo = ttk.Combobox(
            teacher_frame,
            # textvariable=self.var_memType,
            font=("times new roman", 15),
            state="readonly",
            width=18,
        )
        gender_combo["values"] = ("", "Male", "Female", "Others", "Prefer not to say")
        gender_combo.current(0)  # to give the bydeafault index

        gender_combo.place(x=480, y=350, anchor=NW)

        #########################################################################

        # Button Frame
        btn_frame = Frame(teacher_frame, bd=2, relief=RAISED, bg="black")
        btn_frame.place(x=0, y=420, width=675, height=40)

        # Save button in button frame
        save_btn = Button(
            btn_frame,
            command=self.add_data,
            width=23,
            height=2,
            text="Save",
            font=("times new roman", 13, "bold"),
            bg="white",
            fg="black",
        )
        save_btn.grid(row=0, column=0)

        # update button
        update_btn = Button(
            btn_frame,
            command=self.update_data,
            width=23,
            height=2,
            text="Update",
            font=("times new roman", 13, "bold"),
            bg="white",
            fg="black",
        )
        update_btn.grid(row=0, column=1)

        # delete button
        delete_btn = Button(
            btn_frame,
            command=self.delete_data,
            width=24,
            height=2,
            text="Delete",
            font=("times new roman", 13, "bold"),
            bg="white",
            fg="black",
        )
        delete_btn.grid(row=0, column=2)

        # reset button
        reset_btn = Button(
            btn_frame,
            command=self.reset_data,
            width=24,
            height=2,
            text="Reset",
            font=("times new roman", 13, "bold"),
            bg="white",
            fg="black",
        )
        reset_btn.grid(row=0, column=3)

        ###########################################################################################

        # right label
        Right_frame = LabelFrame(
            main_frame,
            bd=5,
            bg="white",
            relief=RAISED,
            text="",
            font=("times new roman", 12, "bold"),
        )
        Right_frame.place(x=720, y=10, width=745, height=777)

        img_right = Image.open("Images/thapar2.jpeg")
        img_right = img_right.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=720, height=130)

        # ========Search System=============
        Search_frame = LabelFrame(
            Right_frame,
            bd=3,
            bg="white",
            relief=SUNKEN,
            text="Search System",
            font=("times new roman", 12, "bold"),
        )
        Search_frame.place(x=5, y=155, width=710, height=115)

        # Label
        search_label = Label(
            Search_frame,
            text="Search By : ",
            font=("times new roman", 20, "bold"),
            height=1,
            width=12,
            relief=SUNKEN,
            bg="red",
            fg="white",
        )
        search_label.grid(row=0, column=0, padx=10, pady=20, sticky=W)

        search_combo = ttk.Combobox(
            Search_frame,
            font=("times new roman", 13, "bold"),
            state="readonly",
            width=12,
        )
        search_combo["values"] = ("Select", "Roll No", "Phone No")
        search_combo.current(0)  # to give the bydeafault index
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(
            Search_frame, width=15, font=("times new roman", 13, "bold")
        )
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        # Buttons
        search_btn = Button(
            Search_frame,
            width=14,
            text="Search",
            font=("time new roman", 15, "bold"),
            bg="white",
            fg="black",
        )
        search_btn.grid(
            row=0,
            column=3,
            padx=4,
        )

        showAll_btn = Button(
            Search_frame,
            width=14,
            text="Show All",
            font=("time new roman", 15, "bold"),
            bg="grey",
            fg="black",
        )
        showAll_btn.grid(row=0, column=4, padx=4)

        # =========Table frame=================
        table_frame = Frame(Right_frame, bd=3, bg="white", relief=SUNKEN)
        table_frame.place(x=5, y=250, width=710, height=480)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            column=(
                "dep",
                "course",
                "year",
                "sem",
                "roll_no",
                "name",
                "batch",
                "batch_no",
                "gender",
                "DOB",
                "email",
                "phone_no",
                "Father_contact",
                "Mother_contact",
                "photo",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)

        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)

        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("roll_no", text="Roll No")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("batch", text="Batch")
        self.student_table.heading("batch_no", text="Batch No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("DOB", text="DOB(DD-MM-YYYY")
        self.student_table.heading("email", text="Email (thapar.edu)")
        self.student_table.heading("phone_no", text="Phone Number")
        self.student_table.heading("Father_contact", text="Father's Ph.No")
        self.student_table.heading("Mother_contact", text="Mother's Ph.No")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("roll_no", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("batch", width=100)
        self.student_table.column("batch_no", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("email", width=200)
        self.student_table.column("phone_no", width=100)
        self.student_table.column("Father_contact", width=100)
        self.student_table.column("Mother_contact", width=100)
        self.student_table.column("photo", width=200)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ============================== Function Declaration ===================================#

    def add_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_course.get() == "Select Course"
            or self.var_year.get() == "Select Year"
            or self.var_semester.get() == "Select Semester"
            or self.var_rollNum.get() == ""
            or self.var_std_name.get() == ""
            or self.var_batch.get() == ""
            or self.var_batchNum.get() == ""
            or self.var_dob.get() == ""
            or self.var_email.get() == ""
            or self.var_phone.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="ShadowWalker77",
                    database="Face_Recognition_db",
                    auth_plugin="mysql_native_password",
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into student_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_rollNum.get(),
                        self.var_std_name.get(),
                        self.var_batch.get(),
                        self.var_batchNum.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_fatherNum.get(),
                        self.var_motherNum.get(),
                        self.var_radioButton1.get(),
                    ),
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success",
                    "Student details have been added successfully",
                    parent=self.root,
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

    # =======================fetch data =================== #
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="ShadowWalker77",
            database="Face_Recognition_db",
            auth_plugin="mysql_native_password",
        )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student_table")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)

        else:
            self.student_table.delete(*self.student_table.get_children())

        conn.commit()
        conn.close()

    # ======================= get cursor =================#

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_rollNum.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_batch.set(data[6]),
        self.var_batchNum.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_fatherNum.set(data[12]),
        self.var_motherNum.set(data[13]),
        self.var_radioButton1.set(data[14]),

        self.var_stdIdforImage = str(data[4])

    # ======= update function ======= #
    def update_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_course.get() == "Select Course"
            or self.var_year.get() == "Select Year"
            or self.var_semester.get() == "Select Semester"
            or self.var_rollNum.get() == ""
            or self.var_std_name.get() == ""
            or self.var_batch.get() == ""
            or self.var_batchNum.get() == ""
            or self.var_dob.get() == ""
            or self.var_email.get() == ""
            or self.var_phone.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update",
                    "Do you want to update the student details",
                    parent=self.root,
                )
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="ShadowWalker77",
                        database="Face_Recognition_db",
                        auth_plugin="mysql_native_password",
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student_table set dep=%s, course=%s,year=%s,semester=%s,std_name=%s,batch=%s,batch_num=%s,gender=%s,dob=%s,email=%s,phone=%s,father_num=%s,mother_num=%s,photoSample=%s where rollNum=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_batch.get(),
                            self.var_batchNum.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_fatherNum.get(),
                            self.var_motherNum.get(),
                            self.var_radioButton1.get(),
                            self.var_rollNum.get(),
                        ),
                    )
                else:
                    if not Update:
                        return
                messagebox.showinfo(
                    "Success", "Student details successfully updated", parent=self.root
                )
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # ======== delete function ======= #
    def delete_data(self):
        if self.var_rollNum.get() == "":
            messagebox.showerror(
                "Error", "Student ID must be required", parent=self.root
            )
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Page",
                    "Do you want to delete this student ?",
                    parent=self.root,
                )
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="ShadowWalker77",
                        database="Face_Recognition_db",
                        auth_plugin="mysql_native_password",
                    )
                    my_cursor = conn.cursor()
                    sql = "delete from student_table where rollNum=%s"
                    val = (self.var_rollNum.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Successfully deleted student details", parent=self.root
                )
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # ======== reset function ======== #
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_rollNum.set("")
        self.var_std_name.set("")
        self.var_batch.set("Batch")
        self.var_batchNum.set("Batch Num")
        self.var_gender.set("Select gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_fatherNum.set("")
        self.var_motherNum.set("")
        self.var_radioButton1.set("")

    # ==== generate data set and take photo sample and also train the data set  ==== #
    def generate_dataset(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_course.get() == "Select Course"
            or self.var_year.get() == "Select Year"
            or self.var_semester.get() == "Select Semester"
            or self.var_rollNum.get() == ""
            or self.var_std_name.get() == ""
            or self.var_batch.get() == ""
            or self.var_batchNum.get() == ""
            or self.var_dob.get() == ""
            or self.var_email.get() == ""
            or self.var_phone.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update",
                    "Do you want to update the student details",
                    parent=self.root,
                )
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="ShadowWalker77",
                        database="Face_Recognition_db",
                        auth_plugin="mysql_native_password",
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute("select * from student_table")
                    myresult = my_cursor.fetchall()
                    id = 0
                    for x in myresult:
                        id += 1
                    my_cursor.execute(
                        "update student_table set dep=%s, course=%s,year=%s,semester=%s,std_name=%s,batch=%s,batch_num=%s,gender=%s,dob=%s,email=%s,phone=%s,father_num=%s,mother_num=%s,photoSample=%s where rollNum=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_batch.get(),
                            self.var_batchNum.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_fatherNum.get(),
                            self.var_motherNum.get(),
                            self.var_radioButton1.get(),
                            self.var_rollNum.get(),
                        ),
                    )
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # == load predefined data on face frontals from opencv

                cam = cv2.VideoCapture(0)
                cam.set(3, 640)  # set video width
                cam.set(4, 480)  # set video height

                face_detector = cv2.CascadeClassifier(
                    "haarcascade_frontalface_default.xml"
                )

                count = 0

                while True:

                    ret, img = cam.read()
                    # img = cv2.flip(img, -1) # flip video image vertically
                    if ret == False:
                        continue

                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_detector.detectMultiScale(gray, 1.3, 5)

                    for (x, y, w, h) in faces:

                        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                        count += 1

                        # Save the captured image into the datasets folder
                        cv2.imwrite(
                            "dataset/"
                            + str(self.var_stdIdforImage)
                            + "."
                            + str(count)
                            + ".jpg",
                            gray[y : y + h, x : x + w],
                        )
                        cv2.putText(
                            img,
                            str(count),
                            (50, 50),
                            cv2.FONT_HERSHEY_COMPLEX,
                            2,
                            (0, 255, 0),
                            2,
                        )

                        cv2.imshow("image", img)

                    k = cv2.waitKey(100) & 0xFF  # Press 'ESC' for exiting video
                    if k == 27:  # escape key ASCII Value
                        break
                    elif count >= 5:  # Take 100 face sample and stop video
                        break

                cam.release()
                cv2.destroyAllWindows()

                # messagebox.showinfo("Training","Please wait while we are training the images")

                # ======== Training Data ========== #

                # Path for face image database
                path = "dataset"

                recognizer = cv2.face.LBPHFaceRecognizer_create()
                detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                # function to get the images and label data
                def getImagesAndLabels(path):

                    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

                    if "dataset/" + ".DS_Store" in imagePaths:
                        imagePaths.remove("dataset/" + ".DS_Store")

                    faceSamples = []
                    ids = []

                    for imagePath in imagePaths:

                        PIL_img = Image.open(imagePath).convert(
                            "L"
                        )  # convert it to grayscale
                        img_numpy = np.array(PIL_img, "uint8")

                        id = int(os.path.split(imagePath)[-1].split(".")[0])
                        faces = detector.detectMultiScale(img_numpy)

                        for (x, y, w, h) in faces:
                            faceSamples.append(img_numpy[y : y + h, x : x + w])
                            ids.append(id)

                    return faceSamples, ids

                print("\n [INFO] Training faces. It will take a few seconds. Wait ...")
                faces, ids = getImagesAndLabels(path)
                recognizer.train(faces, np.array(ids))

                # Save the model into trainer/trainer.yml
                recognizer.write(
                    "trainer/trainer.yml"
                )  # recognizer.save() worked on Mac, but not on Pi

                # Print the numer of faces trained and end program
                print(
                    "\n [INFO] {0} faces trained. Exiting Program".format(
                        len(np.unique(ids))
                    )
                )

                # ======================================================================================#

                messagebox.showinfo(
                    "Result", "Successfully generated the dataset and trained the model"
                )

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = adminCheckTeacherDetails(root)
    root.mainloop()
