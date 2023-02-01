from sklearn.model_selection import train_test_split, StratifiedShuffleSplit
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import PIL.Image
import numpy as np
import random
from tkinter import messagebox
import mysql.connector
from tkcalendar import Calendar, DateEntry
from time import strftime
import cv2
import csv
import os
import re
import time
import aug
from XemAnh import student_id
from XemAnh import StdImage

import matplotlib.pyplot as plt

predictions = []

mydata=[]
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.state('zoomed')
        self.root.configure(bg='#7fe5ea')
        self.root.title("Hệ thống điểm danh (Khoa Phát triển Nông thôn - Đại học Cần Thơ)")
        today = strftime("%Y-%m-%d")
        #======================variables================
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()

        #==================classvariables================
        self.var_class=StringVar()
        self.var_nameclass=StringVar()
        #Lay thông tin lớp học
        class_array=[]
        conn = mysql.connector.connect(host='localhost', user='root', password='',
                                       database='diemdanhsv', port='3306')
        my_cursor = conn.cursor()
        my_cursor.execute("Select lop_id from lop")
        data_class = my_cursor.fetchall()
        for i in data_class:
            class_array.append(i)

        img3 = PIL.Image.open(r"ImageFaceDetect\bg2.png")
        img3 = img3.resize((1350, 700), PIL.Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1350, height=700)

        # ==================================heading====================================
        # ====time====        
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(self.root,font=("times new roman", 11, "bold"),bg="#7fe5ea", fg="#000000")
        lbl.place(x=80,y=35,width=100,height=18)
        time()
        lbl1 = Label(self.root,text=today, font=("times new roman", 11, "bold"), bg="#7fe5ea", fg="#000000")
        lbl1.place(x=80, y=60, width=100, height=18)
        
        # ====title=========
        self.txt = "QUẢN LÝ THÔNG TIN SINH VIÊN"
        self.count = 0
        self.text = ''
        self.heading = Label(self.root, text=self.txt, font=("times new roman", 20, "bold"), bg="#7fe5ea", fg="#0000CC",
                             bd=5, relief=FLAT)
        self.heading.place(x=400, y=30, width=650)

        main_frame = Frame(bg_img, bd=2, bg="#7fe5ea")
        main_frame.place(x=23, y=102, width=1482, height=671)

        #left_label
        Left_frame=LabelFrame(main_frame,bd=2,bg="#6EC3C9",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=655, height=580)

        label_Update_att = Label(Left_frame, bg="#6EC3C9", fg="#990000", text="THÔNG TIN SINH VIÊN",
                                 font=("times new roman", 14, "bold"))
        label_Update_att.place(x=0, y=1, width=640, height=35)

        #course
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="#6EC3C9",fg="#FF0000", relief=RIDGE, text="Thông tin khoá học",
                                font=("times new roman", 13, "bold"))
        current_course_frame.place(x=5, y=35, width=640, height=100)

        #year
        year_label = Label(current_course_frame, text="Năm học", font=("times new roman", 12, "bold"), bg="#6EC3C9")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("times new roman", 12, "bold"), state="readonly",
                                    width=20)
        year_combo["values"] = ("Chọn năm học", "2021-22", "2022-23", "2023-24", "2024-25")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=10, pady=20, sticky=W)

        #semester
        semester_label = Label(current_course_frame, text="Học kì", font=("times new roman", 12, "bold"), bg="#6EC3C9")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester ,font=("times new roman", 11, "bold"), state="readonly",
                                  width=20)
        semester_combo["values"] = ("Chọn học kì", "Học kì I", "Học kì II")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        #Class_student
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="#6EC3C9", fg="#FF0000",relief=RIDGE, text="Thông tin Sinh viên",
                                          font=("times new roman", 13, "bold"))
        class_student_frame.place(x=5, y=160, width=640, height=405)

        #student_id
        studentID_label = Label(class_student_frame, text="ID Sinh viên:", font=("times new roman", 11, "bold"), bg="#6EC3C9")
        studentID_label.grid(row=0, column=0, padx=10,pady=10, sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_std_id,font=("times new roman", 12, "bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #studentName
        studentName_label = Label(class_student_frame, text="Tên Sinh viên:", font=("times new roman", 12, "bold"),
                                bg="#6EC3C9")
        studentName_label.grid(row=0, column=2, padx=10,pady=10, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, width=20,textvariable=self.var_std_name, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10,pady=10, sticky=W)
        
        #gender
        gender_label = Label(class_student_frame, text="Giới tính:", font=("times new roman", 12, "bold"),
                                bg="#6EC3C9")
        gender_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender,
                                  font=("times new roman", 12, "bold"), state="readonly",
                                  width=18)
        gender_combo["values"] = ("Nam", "Nữ", "Khác")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        #DOB
        dob_label = Label(class_student_frame, text="Ngày sinh:", font=("times new roman", 12, "bold"),
                              bg="#6EC3C9")
        dob_label.grid(row=1, column=2, padx=10, pady=10, sticky=W)

        self.dob_entry = DateEntry(class_student_frame, width=18, bd=3,selectmode='day',
                       year=2021, month=5,font=("times new roman", 12),
                       day=22,date_pattern='yyyy-mm-dd')
        self.dob_entry.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        #class
        class_div_label = Label(class_student_frame, text="Lớp học:", font=("times new roman", 12, "bold"),
                                  bg="#6EC3C9")
        class_div_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        class_div_entry = ttk.Combobox(class_student_frame, width=18,textvariable=self.var_div, font=("times new roman", 12, "bold"))
        class_div_entry["values"] = class_array
        class_div_entry.current()
        class_div_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        #email
        email_label = Label(class_student_frame, text="Email:", font=("times new roman", 12, "bold"),
                             bg="#6EC3C9")
        email_label.grid(row=2, column=2, padx=10, pady=10, sticky=W)

        email_entry = ttk.Entry(class_student_frame, width=20,textvariable=self.var_email, font=("times new roman", 12, "bold"),)
        email_entry.grid(row=2, column=3, padx=10, pady=10, sticky=W)
        
        #radioBtn
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Có ảnh",value="Yes")
        radionbtn1.grid(row=3,column=1, padx=10, pady=10, sticky=W)

        radionbtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1, text="Không ảnh", value="No")
        radionbtn2.grid(row=3, column=2, padx=10, pady=10, sticky=W)

        #btn_frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="#6EC3C9")
        btn_frame.place(x=0,y=280,width=635,height=35)

        save_btn=Button(btn_frame,text="Lưu",command=self.add_data,font=("times new roman",11,"bold"),bg="#3300FF", fg="white",width=17)
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame, text="Sửa",command=self.update_data, font=("times new roman", 11, "bold"), bg="#3300FF", fg="white", width=17)
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Xóa",command=self.delete_data, font=("times new roman", 11, "bold"), bg="#FF0000", fg="white", width=17)
        delete_btn.grid(row=0, column=3)

        reset_btn = Button(btn_frame, text="Làm mới",command=self.reset_data, font=("times new roman", 11, "bold"), bg="#3300FF", fg="white", width=17)
        reset_btn.grid(row=0, column=2)

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="#6EC3C9")
        btn_frame1.place(x=0, y=335, width=715, height=35)

        take_photo_btn = Button(btn_frame1, text="Lấy ảnh Sinh viên",command=self.generate_dataset, font=("times new roman", 11, "bold"), bg="#00AA00", fg="white",
                           width=17)
        take_photo_btn.grid(row=1, column=0)

        update_photo_btn = Button(btn_frame1, text="Training Data",command=self.train_classifier, font=("times new roman", 11, "bold"), bg="#00AA00", fg="white",
                                width=17)
        update_photo_btn.grid(row=1, column=1)

        show_photo_btn = Button(btn_frame1, text="Xem ảnh", command=self.student_image, font=("times new roman", 11, "bold"), bg="#00AA00", fg="white",
                                width=17)
        show_photo_btn.grid(row=1, column=2)

        importcsv_btn = Button(btn_frame1, text="Import CSV",  command=self.import_stu, font=("times new roman", 11, "bold"), bg="#00AA00", fg="white",
                                width=17)
        importcsv_btn.grid(row=1, column=3)

        # --------------------------right_label-------------------------
        Right_frame = LabelFrame(main_frame, bd=2, bg="#6EC3C9",
                                font=("times new roman", 12, "bold"))
        Right_frame.place(x=680, y=10, width=615, height=300)

        #Search_frame
        search_frame = LabelFrame(Right_frame, bd=2, bg="#6EC3C9", relief=RIDGE, text="Hệ thống tìm kiếm",fg="#FF0000",
                                         font=("times new roman", 13, "bold"))
        search_frame.place(x=5, y=5, width=600, height=70)

        self.var_com_search= StringVar()
        search_label = Label(search_frame, text="Tìm kiếm theo :", font=("times new roman", 11, "bold"),
                            bg="#6EC3C9",fg="black")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 11, "bold"), state="readonly",
                                      width=10,textvariable=self.var_com_search)
        search_combo["values"] = ("ID Sinh viên", "Tên Sinh viên", "Lớp")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        self.var_search = StringVar()
        search_entry = ttk.Entry(search_frame, width=15, font=("times new roman", 11, "bold"),textvariable=self.var_search)
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Tìm kiếm", font=("times new roman", 11, "bold"),bg="#fbd568", fg="#945305", width=8,command=self.search_data)
        search_btn.grid(row=0, column=3,padx=4)

        showAll_btn = Button(search_frame, text="Xem tất cả", font=("times new roman", 11, "bold"), bg="#fbd568", fg="#945305",
                            width=8,command=self.fetch_data)
        showAll_btn.grid(row=0, column=4,padx=4)

        #table-------frame
        table_frame = Frame(Right_frame, bd=2, bg="#6EC3C9", relief=RIDGE)
        table_frame.place(x=5, y=85, width=600, height=200)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("id","year","sem","name","div","gender","dob","email","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("id", text="ID Sinh viên")
        self.student_table.heading("name", text="Họ tên")
        self.student_table.heading("div", text="Lớp học")
        self.student_table.heading("year", text="Năm học")
        self.student_table.heading("sem", text="Học kì")
        self.student_table.heading("gender", text="Giới tính")
        self.student_table.heading("dob", text="Ngày sinh")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("photo", text="Trạng thái ảnh")
        self.student_table["show"]="headings"

        self.student_table.column("id", width=80, anchor=CENTER)
        self.student_table.column("name", width=110)
        self.student_table.column("year", width=80, anchor=CENTER)
        self.student_table.column("sem", width=80, anchor=CENTER)
        self.student_table.column("div", width=80)
        self.student_table.column("gender", width=80, anchor=CENTER)
        self.student_table.column("dob", width=100, anchor=CENTER)
        self.student_table.column("email", width=100)
        self.student_table.column("photo", width=100, anchor=CENTER)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)#click datagrid
        self.fetch_data()#load du lieu len grid

        #===============================bottomright-Class==============================

        Underright_frame = LabelFrame(main_frame, bd=2, bg="#6EC3C9", relief=RIDGE,
                                      font=("times new roman", 11, "bold"))
        Underright_frame.place(x=680, y=315, width=615, height=275)

        label_studentsb = Label(Underright_frame, bg="#6EC3C9", fg="#990000", text="QUẢN LÝ LỚP HỌC",
                                font=("times new roman", 14, "bold"))
        label_studentsb.place(x=0, y=1, width=600, height=35)

        # search
        self.var_com_searchclass = StringVar()
        search_combo = ttk.Combobox(Underright_frame, font=("times new roman", 11, "bold"),
                                    textvariable=self.var_com_searchclass,
                                    state="readonly",
                                    width=10)
        search_combo["values"] = ("Lớp", "Tên lớp")
        search_combo.current(0)
        search_combo.grid(row=0, column=0, padx=10, pady=40, sticky=W)

        self.var_searchclass = StringVar()
        searchstd_entry = ttk.Entry(Underright_frame, textvariable=self.var_searchclass, width=12,
                                    font=("times new roman", 11, "bold"))
        searchstd_entry.grid(row=0, column=1, padx=5, pady=35, sticky=W)

        searchstd_btn = Button(Underright_frame, command=self.search_Classdata, text="Tìm kiếm",
                               font=("times new roman", 10, "bold"), bg="#fbd568", fg="#945305",
                               width=10)
        searchstd_btn.grid(row=0, column=2, padx=5)

        showAllstd_btn = Button(Underright_frame, text="Xem tất cả", command=self.fetch_Classdata,
                                font=("times new roman", 10, "bold"), bg="#fbd568",
                                fg="#945305",
                                width=10)
        showAllstd_btn.grid(row=0, column=3, padx=5)

        # student
        studentid_label = Label(Underright_frame, text="Lớp học:", font=("times new roman", 12, "bold"),
                                bg="#6EC3C9", width=12)
        studentid_label.place(x=20, y=100, width=100)

        studentid_entry = ttk.Entry(Underright_frame, textvariable=self.var_class,
                                    font=("times new roman", 12, "bold"), width=20)
        studentid_entry.place(x=135, y=100, width=200)

        # subject
        subsub_label = Label(Underright_frame, text="Tên lớp học:", font=("times new roman", 12, "bold"),
                             bg="#6EC3C9")
        subsub_label.place(x=20, y=145, width=80)

        subsub_entry = ttk.Entry(Underright_frame, width=22, textvariable=self.var_nameclass,
                                 font=("times new roman", 12, "bold"))
        subsub_entry.place(x=135, y=145, width=200)

        # btn_frameteacher
        btn_framestd = Frame(Underright_frame, bg="#6EC3C9", bd=2, relief=RIDGE)
        btn_framestd.place(x=5, y=200, width=410, height=55)

        addTc_btn = Button(btn_framestd, text="Thêm mới", command=self.add_Classdata,
                           font=("times new roman", 11, "bold"),
                           bg="#3300FF", fg="white", width=9)
        addTc_btn.grid(row=9, column=0, pady=10, padx=5)

        deleteTc_btn = Button(btn_framestd, text="Xóa", command=self.delete_Classdata,
                              font=("times new roman", 11, "bold"),
                              bg="#FF0000", fg="white", width=9)
        deleteTc_btn.grid(row=9, column=3, pady=10, padx=5)

        updateTc_btn = Button(btn_framestd, text="Cập nhật", command=self.update_Classdata,
                              font=("times new roman", 11, "bold"),
                              bg="#3300FF", fg="white", width=9)
        updateTc_btn.grid(row=9, column=1, pady=10, padx=5)

        resetTc_btn = Button(btn_framestd, text="Làm mới", command=self.reset_Classdata,
                             font=("times new roman", 11, "bold"),
                             bg="#3300FF", fg="white", width=9)
        resetTc_btn.grid(row=9, column=2, pady=10, padx=5)

        # table_frame
        tablestd_frame = Frame(Underright_frame, bd=2, relief=RIDGE, bg="#6EC3C9")
        tablestd_frame.place(x=420, y=35, width=185, height=220)

        # scroll bar
        scroll_x = ttk.Scrollbar(tablestd_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tablestd_frame, orient=VERTICAL)

        self.StudentTable = ttk.Treeview(tablestd_frame, column=(
            "class", "name"),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.StudentTable.xview)
        scroll_y.config(command=self.StudentTable.yview)

        self.StudentTable.heading("class", text="Lớp học")
        self.StudentTable.heading("name", text="Tên lớp")

        self.StudentTable["show"] = "headings"
        self.StudentTable.column("class", width=80)
        self.StudentTable.column("name", width=180)

        self.StudentTable.pack(fill=BOTH, expand=1)
        self.StudentTable.bind("<ButtonRelease>", self.get_cursorClass)
        self.fetch_Classdata()
        
    #=========================================Function Student==========================================
    #===================================================================================================
    def student_image(self):
        if   self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Lỗi","Vui lòng nhập đầy đủ thông tin",parent=self.root)
        else:
            student_id(self.var_std_id.get())
            self.new_window=Toplevel(self.root)
            self.app=StdImage(self.new_window)

    def add_data(self):
        # ========check class================
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                       port='3306')

        my_cursor = conn.cursor()
        my_cursor.execute("select lop_id from `lop` ")
        ckclass = my_cursor.fetchall()
        arrayClass = []
        for chc in ckclass:
            # print(chc[0])
            arrayClass.append(str(chc[0]))
        if  self.var_std_name.get()=="" or self.var_std_id.get()=="" or self.var_div.get()=="":
            messagebox.showerror("Lỗi","Vui lòng nhập đầy đủ thông tin",parent=self.root)
        elif (self.var_div.get() not in arrayClass):
            messagebox.showerror("Lỗi", "Tên lớp học không tồn tại ! Vui lòng kiểm tra lại", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv', port='3306')

                my_cursor=conn.cursor()
                my_cursor.execute("insert into sinhvien values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_std_id.get(),
                    
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.dob_entry.get_date().strftime('%y/%m/%d'),
                    self.var_email.get(),
                    self.var_radio1.get()
                ))
                print(conn)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                messagebox.showinfo("Thành công","Thêm thông tin Sinh viên thành công",parent=self.root)
            except Exception as es:
                messagebox.showerror("Lỗi",f"ID Sinh viên đã tồn tại.",parent=self.root)

    #=======================fetch-data========================
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv', port='3306')

        my_cursor = conn.cursor()
        my_cursor.execute("Select sinhvien_id,sinhvien_namhoc,sinhvien_hocky,sinhvien_ten,lop_id,sinhvien_gioitinh,sinhvien_ngaysinh,sinhvien_email,sinhvien_hinh from sinhvien")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
            self.var_com_search.set("ID Sinh viên")
            self.var_search.set("")
        conn.close()

    #======================get-cursor==============================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_std_id.set(data[0]),
        self.var_year.set(data[1]),
        self.var_semester.set(data[2]),
        self.var_std_name.set(data[3]),
        self.var_div.set(data[4]),
        self.var_gender.set(data[5]),
        self.dob_entry.set_date(data[6]),
        self.var_email.set(data[7]),
        self.var_radio1.set(data[8]),

    #======================update_sinhviên==============================
    def update_data(self):
        if  self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Lỗi","Vui lòng nhập đầy đủ thông tin",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Bạn có muốn cập nhật thông tin Sinh viên này không?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv', port='3306')
                    my_cursor = conn.cursor()
                    my_cursor.execute("update sinhvien set sinhvien_namhoc=%s,sinhvien_hocky=%s,sinhvien_ten=%s,lop_id=%s,"
                                      "sinhvien_gioitinh=%s,sinhvien_ngaysinh=%s,sinhvien_email=%s,sinhvien_hinh=%s where sinhvien_id=%s",(
                                            
                                            self.var_year.get(),
                                            self.var_semester.get(),
                                            self.var_std_name.get(),
                                            self.var_div.get(),
                                            self.var_gender.get(),
                                            self.dob_entry.get_date().strftime('%Y/%m/%d'),
                                            self.var_email.get(),
                                            self.var_radio1.get(),
                                            self.var_std_id.get()
                                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Thành công","Cập nhật thông tin Sinh viên thành công",parent=self.root)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Lỗi",f"Lý do:{str(es)}",parent=self.root)
                
    #======================import_sinhviên==============================
    def import_stu(self):
        try:
            global mydata
            mydata.clear()
            fln = filedialog.askopenfilename(initialdir=os.getcwd() + "/ListCSV", title="Open CSV",
                                             filetypes=(("CSV File", ".csv"), ("ALL File", "*.*")), parent=self.root)
            with open(fln) as myfile:
                csvread = csv.reader(myfile, delimiter=",")

                for i in csvread:
                    mydata.append(i)

            del mydata[0]

            conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                           port='3306')
            my_cursor = conn.cursor()
            sql_insert_query = "insert IGNORE into sinhvien values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            my_cursor.executemany(sql_insert_query, mydata)
            conn.commit()
            self.fetch_data()
            self.reset_data()
            messagebox.showinfo("Thông báo", "Thêm thông tin sinh viên thành công!!!", parent=self.root)
            conn.close()
        except Exception as es:
            messagebox.showerror("Lỗi", "Bạn chưa chọn file đúng hoặc chưa chọn", parent=self.root)

    #======================Delete_sinhviên==============================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Lỗi","Không được bỏ trống ID Sinh viên",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Xoá Sinh viên","Bạn có muốn xóa Sinh viên này?",parent=self.root)
                if delete>0:
                        conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv', port='3306')
                        my_cursor = conn.cursor()
                        sql="delete from sinhvien where sinhvien_id=%s"
                        val=(self.var_std_id.get(),)
                        my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                messagebox.showinfo("Xóa","Xóa Sinh viên thành công",parent=self.root)
            except Exception as es:
                messagebox.showerror("Lỗi",f"Lý do:{str(es)}",parent=self.root)

    #===================Reset function====================
    def reset_data(self):
        self.var_year.set("Chọn năm học"),
        self.var_semester.set("Chọn học kì"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set(""),
        self.var_gender.set("Nam"),
        self.dob_entry.set_date(strftime("%Y/%m/%d")),
        self.var_email.set(""),
        self.var_radio1.set(""),

    #======================Search_sinhviên==============================
    def search_data(self):
            if self.var_com_search.get() == "" or self.var_search.get() == "":
                messagebox.showerror("Lỗi !", "Vui lòng nhập thông tin đầy đủ",parent=self.root)

            else:
                try:
                    conn = mysql.connector.connect(host='localhost', user='root', password='',
                                                   database='diemdanhsv', port='3306')
                    my_cursor = conn.cursor()  # "ID Điểm Danh", "Ngày", "ID Sinh viên"
                    if (self.var_com_search.get() == "ID Sinh viên"):
                        self.var_com_search.set("sinhvien_id")
                    elif (self.var_com_search.get() == "Tên Sinh viên"):
                        self.var_com_search.set("sinhvien_ten")
                    elif (self.var_com_search.get() == "Lớp"):
                        self.var_com_search.set("lop_id")

                    my_cursor.execute("select * from sinhvien where " + str(
                        self.var_com_search.get()) + " Like '%" + str(self.var_search.get()) + "%'")
                    data = my_cursor.fetchall()
                    if (len(data) != 0):
                        self.student_table.delete(*self.student_table.get_children())
                        for i in data:
                            self.student_table.insert("", END, values=i)
                        messagebox.showinfo("Thông báo", "Có " + str(len(data)) + " bản ghi thỏa mãn điều kiện",parent=self.root)
                        conn.commit()
                    else:
                        self.student_table.delete(*self.student_table.get_children())
                        messagebox.showinfo("Thông báo", " Không có bản ghi nào thỏa mãn điều kiện",parent=self.root)
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Lỗi", f"Lý do:{str(es)}", parent=self.root)
                    
    #=============generate dataset and take photo=================
    def generate_dataset(self):
        if  self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Lỗi","Vui lòng nhập đầy đủ thông tin",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv', port='3306')

                my_cursor = conn.cursor()
                # my_cursor.execute("select * from student")
                # myresult=my_cursor.fetchall()
                id=self.var_std_id.get()
                # id=0
                # for x in myresult:
                #     id+=1
                my_cursor.execute("update sinhvien set sinhvien_namhoc=%s,sinhvien_hocky=%s,sinhvien_ten=%s,lop_id=%s,"
                              "sinhvien_gioitinh=%s,sinhvien_ngaysinh=%s,sinhvien_email=%s,sinhvien_hinh=%s where sinhvien_id=%s",
                              (
                                  self.var_year.get(),
                                  self.var_semester.get(),
                                  self.var_std_name.get(),
                                  self.var_div.get(),
                                  self.var_gender.get(),
                                  self.dob_entry.get_date().strftime('%d/%m/%Y'),
                                  self.var_email.get(),
                                  self.var_radio1.get(),
                                  self.var_std_id.get()
                              ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #=========load haar===================
                face_classifier=cv2.CascadeClassifier("models/haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    # chuyển độ thang xám
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    #nhận diện khuôn mặt trên hình ảnh thang độ xám
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor 1.3
                    #minimum neighbor 5
                    # Lặp lại qua các hình chữ nhật của các khuôn mặt được phát hiện
                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]

                        return  face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    net, my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        # face=cv2.resize(face_cropped(my_frame),(190,190))
                        # chuyển độ thang xám
                        face=cv2.cvtColor(face_cropped(my_frame),cv2.COLOR_BGR2GRAY)
                        fill_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"

                        cv2.imwrite(fill_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==120:#duyet du 120 anh
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Kết quả","Tạo dữ liệu khuôn mặt thành công",parent=self.root)
            except Exception as es:
                messagebox.showerror("Lỗi",f"Lý do:{str(es)}",parent=self.root)

    #==========================TrainDataSet=======================
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=PIL.Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        # print(ids)
        
        #=================Train data classifier and save============
        X_train,X_test, y_train,y_test = train_test_split(faces, ids, test_size=0.2,stratify=ids, random_state=20,shuffle=True)
        start_time = time.time()
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(X_train,y_train)
        train_time = time.time() - start_time    
        clf.write("models/classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Kết quả","Training dataset Completed",parent=self.root)
        
        #=================Predict_accuracy============
        for i in range(0, len(X_test)):
            start_time = time.time()
            (prediction, conf) = clf.predict(X_test[i])
            predictions.append(prediction)
            predict_time = time.time() - start_time
            
        print(classification_report(y_test, predictions))
        print(confusion_matrix(y_test, predictions))
        
        # accuracy: (tp + tn) / (p + n)
        accuracy = accuracy_score(y_test, predictions)
        print('Accuracy: %f' % accuracy)

        print('Thời gian đào tạo model: ', train_time, 'seconds.')
        print('Thời gian dự đoán một ảnh: ', predict_time, 'seconds.')
        print(len(X_train))
        print(len(X_test))

        
    #=========================================Function Class============================================
    #===================================================================================================

    #===============get_cursorClass==============
    def get_cursorClass(self, event=""):
            cursor_row = self.StudentTable.focus()
            content = self.StudentTable.item(cursor_row)
            rows = content['values']
            self.var_class.set(rows[0])
            self.var_nameclass.set(rows[1])
            
    #===============add_Classdata==============
    def add_Classdata(self):
            conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                           port='3306')
            my_cursor = conn.cursor()

            # =========check class=================
            my_cursor.execute("select lop_id from `lop` ")
            ckClass = my_cursor.fetchall()
            arrayClass = []
            for chs in ckClass:
                # print(chs[0])
                arrayClass.append(str(chs[0]))
            conn.commit()
            conn.close()
            if self.var_class.get() == "" or self.var_nameclass.get() == "":
                messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin", parent=self.root)

            elif (self.var_class.get()  in arrayClass):
                messagebox.showerror("Lỗi", "Lớp đã tồn tại! Vui lòng kiểm tra lại", parent=self.root)
            else:
                try:
                    conn = mysql.connector.connect(host='localhost', user='root', password='',
                                                   database='diemdanhsv', port='3306')
                    my_cursor = conn.cursor()
                    my_cursor.execute("insert into lop values(%s,%s)", (
                        self.var_class.get(),
                        self.var_nameclass.get(),
                    ))
                    conn.commit()
                    self.fetch_Classdata()
                    self.reset_Classdata()                    

                    conn.close()
                    messagebox.showinfo("Thành công", "Thêm thông tin lớp học thành công",
                                        parent=self.root)
                except Exception as es:
                    messagebox.showerror("Lỗi", f"Lý do:{str(es)}", parent=self.root)
                    
    #===============reset_Classdata==============
    def reset_Classdata(self):
            self.var_class.set("")
            self.var_nameclass.set("")

    #===============fetch_Classdata==============
    def fetch_Classdata(self):
            # global mydata
            # mydata.clear()
            conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                           port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("Select * from lop")
            data = my_cursor.fetchall()
            if len(data) != 0:
                self.StudentTable.delete(*self.StudentTable.get_children())
                for i in data:
                    self.StudentTable.insert("", END, values=i)
                    mydata.append(i)
                conn.commit()
                self.var_com_searchclass.set("Lớp")
                self.var_searchclass.set("")
            conn.close()
            
    #===============update_Classdata==============
    def update_Classdata(self):
            if self.var_class == "" or self.var_nameclass.get() == "":
                messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin", parent=self.root)

            else:
                try:
                    Update = messagebox.askyesno("Update", "Bạn có muốn cập nhật bản ghi này không?", parent=self.root)
                    if Update > 0:
                        conn = mysql.connector.connect(host='localhost', user='root', password='',
                                                       database='diemdanhsv', port='3306')
                        my_cursor = conn.cursor()
                        my_cursor.execute("UPDATE lop SET lop_ten=%s  WHERE "
                                          "lop_id = %s",
                                          (
                                              self.var_nameclass.get(),
                                              self.var_class.get(),
                                          ))
                    else:
                        if not Update:
                            return
                    messagebox.showinfo("Thành công", "Cập nhật thông tin lớp học thành công",
                                        parent=self.root)
                    conn.commit()
                    self.reset_Classdata()
                    self.fetch_Classdata()
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Lỗi", f"Lý do:{str(es)}", parent=self.root)

    #===============delete_Classdata==============
    def delete_Classdata(self):
            if self.var_class== "" or self.var_nameclass.get() == "":
                messagebox.showerror("Lỗi", "Không được bỏ trống thông tin! ", parent=self.root)
            else:
                try:
                    delete = messagebox.askyesno("Xoá bản ghi", "Bạn có muốn xóa bản ghi này ?", parent=self.root)
                    if delete > 0:
                        conn = mysql.connector.connect(host='localhost', user='root', password='',
                                                       database='diemdanhsv', port='3306')
                        my_cursor = conn.cursor()
                        sql = "delete from lop where lop_id=%s "
                        val = (self.var_class.get(),)
                        my_cursor.execute(sql, val)
                    else:
                        if not delete:
                            return
                    conn.commit()
                    # self.fetch_data()p
                    conn.close()
                    messagebox.showinfo("Xóa", "Xóa bản ghi thành công", parent=self.root)
                    self.reset_Classdata()
                    self.fetch_Classdata()
                except Exception as es:
                    messagebox.showerror("Lỗi", f"Lý do:{str(es)}", parent=self.root)

    #===============search_Classdata==============
    def search_Classdata(self):
            if self.var_com_searchclass.get() == "" or self.var_searchclass.get() == "":
                messagebox.showerror("Lỗi !", "Vui lòng nhập thông tin đầy đủ",parent=self.root)

            else:
                try:
                    conn = mysql.connector.connect(host='localhost', user='root', password='',
                                                   database='diemdanhsv', port='3306')
                    my_cursor = conn.cursor()  # "ID Điểm Danh", "Ngày", "ID Sinh viên"
                    if (self.var_com_searchclass.get() == "Lớp"):
                        self.var_com_searchclass.set("lop_id")
                    elif (self.var_com_searchclass.get() == "Tên lớp"):
                        self.var_com_searchclass.set("lop_ten")

                    my_cursor.execute("select * from lop where " + str(
                        self.var_com_searchclass.get()) + " Like '%" + str(self.var_searchclass.get()) + "%'")
                    data = my_cursor.fetchall()
                    if (len(data) != 0):
                        self.StudentTable.delete(*self.StudentTable.get_children())
                        for i in data:
                            self.StudentTable.insert("", END, values=i)
                        messagebox.showinfo("Thông báo", "Có " + str(len(data)) + " bản ghi thỏa mãn điều kiện",parent=self.root)
                        conn.commit()
                    else:
                        self.StudentTable.delete(*self.StudentTable.get_children())
                        messagebox.showinfo("Thông báo", " Không có bản ghi nào thỏa mãn điều kiện",parent=self.root)
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Lỗi", f"Lý do:{str(es)}", parent=self.root)
                    
if __name__=="__main__":
    root=Tk() #khoi tao cua so va gan root vao
    obj=Student(root)
    root.mainloop()# cua so hien len
