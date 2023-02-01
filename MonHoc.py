from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
import PIL.Image
from time import strftime
from math import *
from tkinter import messagebox
import mysql.connector
from tkinter import filedialog
import os
import csv


mydata=[]
class Subject:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.state('zoomed')
        self.root.configure(bg='#7fe5ea')
        self.root.title("Hệ thống điểm danh (Khoa Phát triển Nông thôn - Đại học Cần Thơ)")
        today = strftime("%Y-%m-%d")

        # ================variable-subject===================
        self.var_subname = StringVar()
        self.var_subid = StringVar()

        self.var_teachersub = StringVar()
        self.var_subsub= StringVar()
        self.var_current_tc=StringVar()
        self.var_current_sub=StringVar()

        self.var_studentsub = StringVar()
        self.var_subsubst = StringVar()
        self.var_current_std = StringVar()
        self.var_current_substd = StringVar()
    
        img3 = PIL.Image.open(r"ImageFaceDetect\bg2.png")
        img3 = img3.resize((1350, 700), PIL.Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1350, height=700)

        #==================================heading====================================
        #====time====
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(self.root,font=("times new roman", 11, "bold"),bg="#7fe5ea", fg="#000000")
        lbl.place(x=80,y=35,width=100,height=18)
        time()
        lbl1 = Label(self.root,text=today, font=("times new roman", 11, "bold"), bg="#7fe5ea", fg="#000000")
        lbl1.place(x=80, y=60, width=100, height=18)

        #====title=========
        self.txt = "QUẢN LÝ THÔNG TIN MÔN HỌC"
        self.count = 0
        self.text = ''
        self.heading = Label(self.root, text=self.txt, font=("times new roman", 20, "bold"), bg="#7fe5ea", fg="#0000CC",
                             bd=5, relief=FLAT)
        self.heading.place(x=400, y=30, width=650)

        main_frame = Frame(bg_img, bd=2, bg="#7fe5ea")
        main_frame.place(x=23, y=102, width=1482, height=671)

        # ===================Môn học=====================
        Left_frame = LabelFrame(main_frame, bd=2, bg="#6EC3C9", relief=RIDGE,
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=5, width=1270, height=280)

        label_Update_att = Label(Left_frame, bg="#6EC3C9", fg="#990000", text="THÔNG TIN MÔN HỌC",
                                 font=("times new roman", 14, "bold"))
        label_Update_att.place(x=0, y=1, width=450, height=40)

        left_inside_frame = Frame(Left_frame, bd=1, bg="#6EC3C9")
        left_inside_frame.place(x=0, y=40, width=1260, height=235)

        # id
        auttendanceID_label = Label(left_inside_frame, text="ID Môn học:",font=("times new roman", 11, "bold"),
                                    bg="#6EC3C9")
        auttendanceID_label.grid(row=0, column=0, padx=50, pady=10, sticky=W)

        auttendanceID_entry = ttk.Entry(left_inside_frame, textvariable=self.var_subid,
                                        font=("times new roman", 11, "bold"),width=22)
        auttendanceID_entry.grid(row=0, column=1, padx=20, pady=10, sticky=W)

        # subject
        roll_label = Label(left_inside_frame, text="Tên môn học:", font=("times new roman", 11, "bold"),
                           bg="#6EC3C9")
        roll_label.grid(row=1, column=0, padx=50, pady=10, sticky=W)

        roll_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_subname,
                               font=("times new roman", 11, "bold"))
        roll_entry.grid(row=1, column=1, padx=20, pady=10, sticky=W)
        
        # =====btn_frame============
        btn_frame = Frame(left_inside_frame, bg="#6EC3C9")
        btn_frame.place(x=30, y=140, width=440, height=110)

        add_btn = Button(btn_frame, text="Thêm mới", command=self.add_data, font=("times new roman", 11, "bold"),
                            bg="#3300FF", fg="white", width=17)
        add_btn.grid(row=9, column=0, pady=5,padx=20)

        delete_btn = Button(btn_frame, text="Xóa", command=self.delete_data,
                            font=("times new roman", 11, "bold"),
                            bg="#FF0000", fg="white", width=17)
        delete_btn.grid(row=10, column=1, pady=5,padx=20)

        update_btn = Button(btn_frame, text="Cập nhật", command=self.update_data, font=("times new roman", 11, "bold"),
                            bg="#3300FF", fg="white", width=17)
        update_btn.grid(row=9, column=1, pady=5, padx=5)

        reset_btn = Button(btn_frame, text="Làm mới", command=self.reset_data, font=("times new roman", 11, "bold"),
                           bg="#3300FF", fg="white", width=17)
        reset_btn.grid(row=10, column=0, pady=5,padx=5)

        # ==================right_ label========================
        Right_frame = LabelFrame(Left_frame, bg="#6EC3C9",bd=0,
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=530, y=5, width=730, height=255)

        # search
        self.var_com_search = StringVar()
        search_label = Label(Right_frame, text="Tìm kiếm theo :", font=("times new roman", 11, "bold"),
                             bg="#6EC3C9")
        search_label.grid(row=0, column=0, padx=15, pady=0, sticky=W)

        search_combo = ttk.Combobox(Right_frame, font=("times new roman", 11, "bold"), textvariable=self.var_com_search,
                                    state="read only",
                                    width=13)
        search_combo["values"] = ("ID Môn học", "Tên môn học")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=15, sticky=W)

        self.var_search = StringVar()
        search_entry = ttk.Entry(Right_frame, textvariable=self.var_search, width=15,
                                 font=("times new roman", 11, "bold"))
        search_entry.grid(row=0, column=2, padx=15, pady=5, sticky=W)

        search_btn = Button(Right_frame, command=self.search_data, text="Tìm kiếm",
                            font=("times new roman", 11, "bold"), bg="#fbd568", fg="#945305", width=12)
        search_btn.grid(row=0, column=3, padx=15)

        showAll_btn = Button(Right_frame, text="Xem tất cả", command=self.fetch_data,
                             font=("times new roman", 11, "bold"), bg="#fbd568", fg="#945305", width=12)
        showAll_btn.grid(row=0, column=5, padx=15)

        # table_frame
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="#6EC3C9")
        table_frame.place(x=130, y=55, width=580, height=200)

        # scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=(
        "id", "name"),
                                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="ID Môn học")
        self.AttendanceReportTable.heading("name", text="Tên môn học")


        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("name", width=100)


        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()  # load du lieu len grid

        #=============================Môn dạy của giảng viên============================
        Underleft_frame = LabelFrame(main_frame, bd=2, bg="#6EC3C9", relief=RIDGE,
                                )
        Underleft_frame.place(x=10, y=295, width=625, height=285)

        label_teachersb = Label(Underleft_frame, bg="#6EC3C9", fg="#990000", text="MÔN DẠY CỦA GIẢNG VIÊN",
                                 font=("times new roman", 14, "bold"))
        label_teachersb.place(x=0, y=1, width=600, height=35)

        # search
        self.var_com_searchtc = StringVar()
        search_combo = ttk.Combobox(Underleft_frame, font=("times new roman", 12, "bold"), textvariable=self.var_com_searchtc,
                                    state="read only",
                                    width=12)
        search_combo["values"] = ("ID Giảng viên", "ID môn học")
        search_combo.current(0)
        search_combo.grid(row=0, column=0, padx=10, pady=40, sticky=W)

        self.var_searchtc = StringVar()
        searchtc_entry = ttk.Entry(Underleft_frame, textvariable=self.var_searchtc, width=13,
                                 font=("times new roman", 10, "bold"))
        searchtc_entry.grid(row=0, column=1, padx=5, pady=35, sticky=W)

        searchtc_btn = Button(Underleft_frame, command=self.search_Tcdata, text="Tìm kiếm",
                            font=("times new roman", 10, "bold"), bg="#fbd568", fg="#945305",
                            width=10)
        searchtc_btn.grid(row=0, column=2, padx=5)

        showAlltc_btn = Button(Underleft_frame, text="Xem tất cả", command=self.fetch_Tcdata,
                             font=("times new roman", 10, "bold"), bg="#fbd568",
                             fg="#945305",
                             width=10)
        showAlltc_btn.grid(row=0, column=3, padx=5)

        # id
        self.var_teachersub.trace("w", lambda name, index, mode, var_teachersub=self.var_teachersub: self.callback())
        teacherid_label = Label(Underleft_frame, text="ID Giảng viên:", font=("times new roman", 11, "bold"),
                                    bg="#6EC3C9",width=12)
        teacherid_label.place(x=20, y=120, width=100)

        teacherid_entry = ttk.Entry(Underleft_frame, textvariable=self.var_teachersub,
                                        font=("times new roman", 11, "bold"), width=20)
        teacherid_entry.place(x=130, y=120, width=100)

        #teacher_name
        self.var_teachername=StringVar()
        teachernLabel = Label(Underleft_frame, text="Tên GV:", font=("times new roman", 11, "bold"),
                              bg="#6EC3C9")
        teachernLabel.place(x=240, y=120,width=60)

        teachernLabel_entry = ttk.Entry(Underleft_frame, width=20, textvariable=self.var_teachername,
                                        font=("times new roman", 11, "bold"), state="disabled")
        teachernLabel_entry.place(x=310, y=120,width=110)

        # subject
        self.var_subsub.trace("w", lambda name, index, mode, var_subsub=self.var_subsub: self.callsubtc())
        subsub_label = Label(Underleft_frame, text="ID môn học:", font=("times new roman", 11, "bold"),
                           bg="#6EC3C9")
        subsub_label.place(x=12, y=165, width=100)

        subsub_entry = ttk.Entry(Underleft_frame, width=22, textvariable=self.var_subsub,
                               font=("times new roman", 11, "bold"))
        subsub_entry.place(x=130, y=165, width=100)

        #sub_name
        self.var_subjectname = StringVar()
        subjectnameLabel = Label(Underleft_frame, text="Tên MH:", font=("times new roman", 11, "bold"),
                                 bg="#6EC3C9")
        subjectnameLabel.place(x=240, y=165,width=60)

        subjectnameLabel_entry = ttk.Entry(Underleft_frame, width=22, textvariable=self.var_subjectname,
                                           font=("times new roman", 11, "bold"), state="disabled")
        subjectnameLabel_entry.place(x=310, y=165,width=110)

        #btn_frameteacher
        btn_frametc = Frame(Underleft_frame, bg="#6EC3C9",bd=2,relief=RIDGE)
        btn_frametc.place(x=20, y=225, width=405, height=45)

        addTc_btn = Button(btn_frametc, text="Thêm mới", command=self.add_Tcdata, font=("times new roman", 11, "bold"),
                         bg="#3300FF", fg="white", width=9)
        addTc_btn.grid(row=9, column=0, pady=7, padx=5)

        deleteTc_btn = Button(btn_frametc, text="Xóa", command=self.delete_Tcdata,
                            font=("times new roman", 11, "bold"),
                            bg="#FF0000", fg="white", width=9)
        deleteTc_btn.grid(row=9, column=3, pady=7, padx=5)

        updateTc_btn = Button(btn_frametc, text="Cập nhật", command=self.update_Tcdata, font=("times new roman", 11, "bold"),
                            bg="#3300FF", fg="white", width=9)
        updateTc_btn.grid(row=9, column=1, pady=7, padx=5)

        resetTc_btn = Button(btn_frametc, text="Làm mới", command=self.reset_Tcdata, font=("times new roman", 11, "bold"),
                           bg="#3300FF", fg="white", width=9)
        resetTc_btn.grid(row=9, column=2, pady=7, padx=5)
        
        # table_frame
        tabletc_frame = Frame(Underleft_frame, bd=2, relief=RIDGE, bg="#6EC3C9")
        tabletc_frame.place(x=438, y=40, width=175, height=230)

        # scroll bar
        scroll_x = ttk.Scrollbar(tabletc_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tabletc_frame, orient=VERTICAL)

        self.TeacherTable = ttk.Treeview(tabletc_frame, column=(
            "teacherid", "subid"),
                                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.TeacherTable.xview)
        scroll_y.config(command=self.TeacherTable.yview)

        self.TeacherTable.heading("teacherid", text="ID GV")
        self.TeacherTable.heading("subid", text="ID Môn học")

        self.TeacherTable["show"] = "headings"
        
        self.TeacherTable.column("teacherid", width=80, anchor=CENTER)
        self.TeacherTable.column("subid", width=80)

        self.TeacherTable.pack(fill=BOTH, expand=1)
        self.TeacherTable.bind("<ButtonRelease>", self.get_cursorTc)
        self.fetch_Tcdata()

        #==================Môn học của sinh viên==================
        Underright_frame = LabelFrame(main_frame, bd=2, bg="#6EC3C9", relief=RIDGE,
                                     font=("times new roman", 12, "bold"))
        Underright_frame.place(x=650, y=295, width=628, height=285)

        label_studentsb = Label(Underright_frame, bg="#6EC3C9", fg="#990000", text="MÔN HỌC CỦA SINH VIÊN",
                                font=("times new roman", 14, "bold"))
        label_studentsb.place(x=0, y=1, width=600, height=35)

        # search
        self.var_com_searchstd = StringVar()
        search_combo = ttk.Combobox(Underright_frame, font=("times new roman", 11, "bold"),
                                    textvariable=self.var_com_searchstd,
                                    state="read only",
                                    width=12)
        search_combo["values"] = ("ID Sinh viên", "ID môn học")
        search_combo.current(0)
        search_combo.grid(row=0, column=0, padx=10, pady=40, sticky=W)

        self.var_searchstd = StringVar()
        searchstd_entry = ttk.Entry(Underright_frame, textvariable=self.var_searchstd, width=13,
                                   font=("times new roman", 10, "bold"))
        searchstd_entry.grid(row=0, column=1, padx=5, pady=35, sticky=W)

        searchstd_btn = Button(Underright_frame, command=self.search_Stddata, text="Tìm kiếm",
                              font=("times new roman", 10, "bold"), bg="#fbd568", fg="#945305",
                              width=10)
        searchstd_btn.grid(row=0, column=2, padx=5)

        showAllstd_btn = Button(Underright_frame, text="Xem tất cả", command=self.fetch_Stddata,
                               font=("times new roman", 10, "bold"), bg="#fbd568",
                               fg="#945305",
                               width=10)
        showAllstd_btn.grid(row=0, column=3, padx=5)

        # student
        self.var_studentsub.trace("w", lambda name, index, mode, var_studentsub=self.var_studentsub: self.callstudent())
        studentid_label = Label(Underright_frame, text="ID Sinh viên:", font=("times new roman", 11, "bold"),
                                bg="#6EC3C9", width=12)
        studentid_label.place(x=20, y=120, width=100)

        studentid_entry = ttk.Entry(Underright_frame, textvariable=self.var_studentsub,
                                    font=("times new roman", 11, "bold"), width=20)
        studentid_entry.place(x=130, y=120, width=100)

        #student_name
        self.var_studentname = StringVar()
        studentname_label = Label(Underright_frame, text="Tên HS:", font=("times new roman", 11, "bold"),
                                bg="#6EC3C9", width=12)
        studentname_label.place(x=240, y=120, width=60)

        studentname_entry = ttk.Entry(Underright_frame, textvariable=self.var_studentname,
                                    font=("times new roman", 11, "bold"), width=12,state="disabled")
        studentname_entry.place(x=310, y=120, width=110)

        # subject
        self.var_subsubst.trace("w", lambda name, index, mode, var_subsubst=self.var_subsubst: self.callstSub())
        subsub_label = Label(Underright_frame, text="ID Môn học:", font=("times new roman", 11, "bold"),
                             bg="#6EC3C9")
        subsub_label.place(x=13, y=165, width=100)

        subsub_entry = ttk.Entry(Underright_frame, width=22, textvariable=self.var_subsubst,
                                 font=("times new roman", 11, "bold"))
        subsub_entry.place(x=130, y=165, width=100)

        # subject_name
        self.var_stSubname = StringVar()
        studentname_label = Label(Underright_frame, text="Tên MH:", font=("times new roman", 11, "bold"),
                                  bg="#6EC3C9", width=12)
        studentname_label.place(x=240, y=165, width=60)

        studentname_entry = ttk.Entry(Underright_frame, textvariable=self.var_stSubname,
                                      font=("times new roman", 11, "bold"), width=12, state="disabled")
        studentname_entry.place(x=310, y=165, width=110)

        # btn_frameteacher
        btn_framestd = Frame(Underright_frame, bg="#6EC3C9", bd=2, relief=RIDGE)
        btn_framestd.place(x=20, y=225, width=405, height=45)

        addTc_btn = Button(btn_framestd, text="Thêm mới", command=self.add_Stddata, font=("times new roman", 11, "bold"),
                           bg="#3300FF", fg="white", width=7)
        addTc_btn.grid(row=9, column=0, pady=7, padx=3)

        deleteTc_btn = Button(btn_framestd, text="Xóa", command=self.delete_Stddata,
                              font=("times new roman", 11, "bold"),
                              bg="#FF0000", fg="white", width=7)
        deleteTc_btn.grid(row=9, column=4, pady=7, padx=3)

        updateTc_btn = Button(btn_framestd, text="Cập nhật", command=self.update_Stddata,
                              font=("times new roman", 11, "bold"),
                              bg="#3300FF", fg="white", width=7)
        updateTc_btn.grid(row=9, column=1, pady=7, padx=3)

        resetTc_btn = Button(btn_framestd, text="Làm mới", command=self.reset_Stddata,
                             font=("times new roman", 11, "bold"),
                             bg="#3300FF", fg="white", width=7)
        resetTc_btn.grid(row=9, column=2, pady=7, padx=3)
        
        import_btn = Button(btn_framestd, text="Import", command=self.insert_stu_subject, 
                            font=("times new roman", 11, "bold"),
                            bg="#3300FF", fg="white", width=7)
        import_btn.grid(row=9, column=3, pady=7, padx=3)


        # table_frame
        tablestd_frame = Frame(Underright_frame, bd=2, relief=RIDGE, bg="#6EC3C9")
        tablestd_frame.place(x=437, y=40, width=180, height=230)

        # scroll bar
        scroll_x = ttk.Scrollbar(tablestd_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tablestd_frame, orient=VERTICAL)

        self.StudentTable = ttk.Treeview(tablestd_frame, column=(
            "studentid", "subid"),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.StudentTable.xview)
        scroll_y.config(command=self.StudentTable.yview)

        self.StudentTable.heading("studentid", text="ID Sinh viên")
        self.StudentTable.heading("subid", text="ID Môn học")

        self.StudentTable["show"] = "headings"
        self.StudentTable.column("studentid", width=80, anchor=CENTER)
        self.StudentTable.column("subid", width=80)

        self.StudentTable.pack(fill=BOTH, expand=1)
        self.StudentTable.bind("<ButtonRelease>", self.get_cursorStd)
        self.fetch_Stddata()
        # ================fetchData======================

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_subid.set(rows[0])
        self.var_subname.set(rows[1])


    def add_data(self):
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                       port='3306')
        my_cursor = conn.cursor() 
        
        #============checkid=================
        my_cursor.execute("select monhoc_id from `monhoc` ")
        cksubject = my_cursor.fetchall()
        arraySubject = []
        for chs in cksubject:
            # print(chs[0])
            arraySubject.append(str(chs[0]))
        
        if self.var_subid.get()=="" or self.var_subname.get()=="":
            messagebox.showerror("Lỗi","Vui lòng nhập đầy đủ thông tin",parent=self.root)         
        elif(self.var_subid.get() in arraySubject):
            messagebox.showerror("Lỗi", "Đã tồn tại mã môn học ! Vui lòng kiểm tra lại", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv', port='3306')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into monhoc values(%s,%s) ",(
                    self.var_subid.get(),
                    self.var_subname.get(),
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()

                conn.close()
                messagebox.showinfo("Thành công","Thêm thông tin môn học thành công",parent=self.root)
            except Exception as es:
                messagebox.showerror("Lỗi",f"Lý do:{str(es)}",parent=self.root)
                
    def reset_data(self):
        self.var_subid.set("")
        self.var_subname.set("")

    def fetch_data(self):
            # global mydata
            # mydata.clear()
            conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                           port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("Select * from monhoc")
            data = my_cursor.fetchall()
            if len(data) != 0:
                self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                for i in data:
                    self.AttendanceReportTable.insert("", END, values=i)
                    mydata.append(i)
                conn.commit()
                self.var_com_search.set("ID Môn học")
                self.var_search.set("")

            conn.close()
            
    def update(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        
    def update_data(self):
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                       port='3306')
        my_cursor = conn.cursor()
        # =========check subject============
        my_cursor.execute("select monhoc_ten from `monhoc` ")
        ckSubject = my_cursor.fetchall()
        arraySub = []
        for chk in ckSubject:
            # print(chk[0])
            arraySub.append(str(chk[0]))
            

        if self.var_subid.get()=="" or self.var_subname.get()=="" :
            messagebox.showerror("Lỗi","Vui lòng nhập đầy đủ thông tin",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Bạn có muốn cập nhật bản ghi này không?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv', port='3306')
                    my_cursor = conn.cursor()
                    my_cursor.execute("update monhoc set monhoc_ten=%s"
                                      " where monhoc_id=%s",(
                                            self.var_subname.get(),
                                            self.var_subid.get(),
                                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Thành công","Cập nhật thông tin môn học thành công",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Lỗi",f"Lý do:{str(es)}",parent=self.root)

    # Delete Function
    def delete_data(self):
            if self.var_subid == "":
                messagebox.showerror("Lỗi", "Không được bỏ trống ID ", parent=self.root)
            else:
                try:
                    delete = messagebox.askyesno("Xoá bản ghi", "Bạn có muốn xóa bản ghi này ?", parent=self.root)
                    if delete > 0:
                        conn = mysql.connector.connect(host='localhost', user='root', password='',
                                                       database='diemdanhsv', port='3306')
                        my_cursor = conn.cursor()
                        sql = "delete from monhoc where monhoc_id=%s"
                        val = (self.var_subid.get(),)
                        my_cursor.execute(sql, val)
                    else:
                        if not delete:
                            return
                    conn.commit()
                    # self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Xóa", "Xóa bản ghi thành công", parent=self.root)
                    self.fetch_data()
                    self.reset_data()
                except Exception as es:
                    messagebox.showerror("Lỗi", f"Lý do:{str(es)}", parent=self.root)

    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Lỗi !","Vui lòng nhập thông tin đầy đủ",parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password='',
                                               database='diemdanhsv', port='3306')
                my_cursor = conn.cursor()#"ID Điểm Danh", "Ngày", "ID Sinh viên"
                if(self.var_com_search.get()=="ID Môn học"):
                    self.var_com_search.set("monhoc_id")
                elif(self.var_com_search.get()=="Tên môn học"):
                    self.var_com_search.set("monhoc_ten")
                my_cursor.execute("select * from monhoc where "+str(self.var_com_search.get())+" Like '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if(len(data)!=0):
                    self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                    for i in data:
                        self.AttendanceReportTable.insert("",END,values=i)
                    messagebox.showinfo("Thông báo","Có "+str(len(data))+" bản ghi thỏa mãn điều kiện",parent=self.root)
                    conn.commit()
                else:
                    self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                    messagebox.showinfo("Thông báo", " Không có bản ghi nào thỏa mãn điều kiện",parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showerror("Lỗi", f"Lý do:{str(es)}", parent=self.root)

    #==========================FUNCTION monhocgiangvien===================================

    def get_cursorTc(self,event=""):
        cursor_row=self.TeacherTable.focus()
        content=self.TeacherTable.item(cursor_row)
        rows=content['values']
        self.var_current_tc.set(rows[0])
        self.var_current_sub.set(rows[1])
        self.var_teachersub.set(rows[0])
        self.var_subsub.set(rows[1])
    def callback(self):
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                       port='3306')
        my_cursor = conn.cursor()
        my_cursor.execute("select giangvien_id from `giangvien` ")
        ckteacher = my_cursor.fetchall()
        arrayTeacher = []
        for cht in ckteacher:
            # print(cht[0])
            arrayTeacher.append(str(cht[0]))
        if(self.var_teachersub.get() not in arrayTeacher):

            self.var_teachername.set("")
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                           port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("select giangvien_ten from `giangvien` where giangvien_id=%s", (self.var_teachersub.get(),))
            ckteacher = my_cursor.fetchone()
            self.var_teachername.set(ckteacher[0])
        conn.commit()
        conn.close()
    def callsubtc(self):
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                       port='3306')
        my_cursor = conn.cursor()
        my_cursor.execute("select monhoc_id from `monhoc` ")
        ckteacher = my_cursor.fetchall()
        arrayTeacher = []
        for cht in ckteacher:
            # print(cht[0])
            arrayTeacher.append(str(cht[0]))
        if(self.var_subsub.get() not in arrayTeacher):

            self.var_subjectname.set("")
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                           port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("select monhoc_ten from `monhoc` where monhoc_id=%s", (self.var_subsub.get(),))
            ckteacher = my_cursor.fetchone()
            self.var_subjectname.set(ckteacher[0])
        conn.commit()
        conn.close()

    def add_Tcdata(self):
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                       port='3306')
        my_cursor = conn.cursor()
        # =========check subject============
        my_cursor.execute("select monhoc_id from monhocgiangvien where giangvien_id=%s", (self.var_teachersub.get(),))
        ckSubject = my_cursor.fetchall()
        arraySub = []
        for chk in ckSubject:
            arraySub.append(str(chk[0]))

        # ========check teacher================
        my_cursor.execute("select giangvien_id from `giangvien` ")
        ckteacher = my_cursor.fetchall()
        arrayTeacher = []
        for cht in ckteacher:
            # print(cht[0])
            arrayTeacher.append(str(cht[0]))

        #=========check subject=================
        my_cursor.execute("select monhoc_id from `monhoc` ")
        cksubject = my_cursor.fetchall()
        arraySubject = []
        for chs in cksubject:
            # print(chs[0])
            arraySubject.append(str(chs[0]))
        #=========check teacher-has-1-subject=======
        my_cursor.execute("select COUNT(giangvien_id) from `monhocgiangvien` where monhoc_id=%s",(self.var_subsub.get(),) )
        ckTeacher_has1sub = my_cursor.fetchone()

        conn.commit()
        conn.close()
        if self.var_teachersub.get()=="" or self.var_subsub.get()=="" :
            messagebox.showerror("Lỗi","Vui lòng nhập đầy đủ thông tin",parent=self.root)
        elif(self.var_subsub.get() in arraySub):
            messagebox.showerror("Lỗi", "Giảng viên đã có môn học này! Vui lòng kiểm tra lại", parent=self.root)

        elif(self.var_teachersub.get() not in arrayTeacher):
            messagebox.showerror("Lỗi", "ID Giảng viên không tồn tại! Vui lòng kiểm tra lại", parent=self.root)
        elif(self.var_subsub.get() not in arraySubject):
            messagebox.showerror("Lỗi", "ID Môn học không tồn tại! Vui lòng kiểm tra lại", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv', port='3306')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into monhocgiangvien values(%s,%s)",(
                    self.var_teachersub.get(),
                    self.var_subsub.get(),
                ))
                conn.commit()
                self.fetch_Tcdata()
                self.reset_Tcdata()
                conn.close()
                messagebox.showinfo("Thành công","Thêm thông tin môn học cho Giảng viên thành công",parent=self.root)
            except Exception as es:
                messagebox.showerror("Lỗi",f"Lý do:{str(es)}",parent=self.root)

    def reset_Tcdata(self):
        self.var_teachersub.set("")
        self.var_subsub.set("")


    def fetch_Tcdata(self):
            # global mydata
            # mydata.clear()
            conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                           port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("Select * from monhocgiangvien")
            data = my_cursor.fetchall()
            if len(data) != 0:
                self.TeacherTable.delete(*self.TeacherTable.get_children())
                for i in data:
                    self.TeacherTable.insert("", END, values=i)
                    mydata.append(i)
                conn.commit()
                self.var_com_searchtc.set("ID Giảng viên")
                self.var_searchtc.set("")
            conn.close()

    def update_Tcdata(self):
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                       port='3306')
        my_cursor = conn.cursor()
        # =========check subject============
        my_cursor.execute("select monhoc_id from monhocgiangvien where giangvien_id=%s",
                          (self.var_teachersub.get(),))
        ckSubject = my_cursor.fetchall()
        arraySub = []
        for chk in ckSubject:
            print(chk[0])
            arraySub.append(str(chk[0]))

        # ========check teacher================
        my_cursor.execute("select giangvien_id from `giangvien` ")
        ckteacher = my_cursor.fetchall()
        arrayTeacher = []
        for cht in ckteacher:
            print(cht[0])
            arrayTeacher.append(str(cht[0]))

        # =========check subject=================
        my_cursor.execute("select monhoc_id from `monhoc` ")
        cksubject = my_cursor.fetchall()
        arraySubject = []
        for chs in cksubject:
            print(chs[0])
            arraySubject.append(str(chs[0]))
        conn.commit()
        conn.close()
        if self.var_teachersub == "" or self.var_subsub.get() == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin", parent=self.root)
        elif (self.var_subsub.get() in arraySub):
            messagebox.showerror("Lỗi", "Giảng viên đã có môn học này! Vui lòng kiểm tra lại", parent=self.root)
        elif (self.var_teachersub.get() not in arrayTeacher):
            messagebox.showerror("Lỗi", "ID Giảng viên không tồn tại! Vui lòng kiểm tra lại", parent=self.root)
        elif (self.var_subsub.get() not in arraySubject):
            messagebox.showerror("Lỗi", "ID Môn học không tồn tại! Vui lòng kiểm tra lại", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Bạn có muốn cập nhật bản ghi này không?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv', port='3306')
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE `monhocgiangvien` SET `giangvien_id` = %s, `monhoc_id` = %s WHERE "
                                      "`monhocgiangvien`.`giangvien_id` = %s AND `monhocgiangvien`.`monhoc_id` = %s",(
                                            self.var_teachersub.get(),
                                            self.var_subsub.get(),
                                            self.var_current_tc.get(),
                                            self.var_current_sub.get(),
                                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Thành công","Cập nhật thông tin môn học GV thành công",parent=self.root)
                conn.commit()
                self.reset_Tcdata()
                self.fetch_Tcdata()
                conn.close()
            except Exception as es:
                messagebox.showerror("Lỗi",f"Lý do:{str(es)}",parent=self.root)

    # Delete Function
    def delete_Tcdata(self):
            if self.var_teachersub == "" or self.var_subsub.get() == "":
                messagebox.showerror("Lỗi", "Không được bỏ trống thông tin! ", parent=self.root)
            else:
                try:
                    delete = messagebox.askyesno("Xoá bản ghi", "Bạn có muốn xóa bản ghi này ?", parent=self.root)
                    if delete > 0:
                        conn = mysql.connector.connect(host='localhost', user='root', password='',
                                                       database='diemdanhsv', port='3306')
                        my_cursor = conn.cursor()
                        sql = "delete from monhocgiangvien where giangvien_id=%s and monhoc_id=%s"
                        val = (self.var_teachersub.get(),self.var_subsub.get(),)
                        my_cursor.execute(sql, val)
                    else:
                        if not delete:
                            return
                    conn.commit()
                    # self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Xóa", "Xóa bản ghi thành công", parent=self.root)
                    self.reset_Tcdata()
                    self.fetch_Tcdata()
                except Exception as es:
                    messagebox.showerror("Lỗi", f"Lý do:{str(es)}", parent=self.root)

    def search_Tcdata(self):
        if self.var_com_searchtc.get()=="" or self.var_searchtc.get()=="":
            messagebox.showerror("Lỗi !","Vui lòng nhập thông tin đầy đủ",parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password='',
                                               database='diemdanhsv', port='3306')
                my_cursor = conn.cursor()#"ID Điểm Danh", "Ngày", "ID Sinh viên"
                if(self.var_com_searchtc.get()=="ID Giảng viên"):
                    self.var_com_searchtc.set("giangvien_id")
                elif(self.var_com_searchtc.get()=="ID môn học"):
                    self.var_com_searchtc.set("monhoc_id")

                my_cursor.execute("select * from monhocgiangvien where "+str(self.var_com_searchtc.get())+" Like '%"+str(self.var_searchtc.get())+"%'")
                data=my_cursor.fetchall()
                if(len(data)!=0):
                    self.TeacherTable.delete(*self.TeacherTable.get_children())
                    for i in data:
                        self.TeacherTable.insert("",END,values=i)
                    messagebox.showinfo("Thông báo","Có "+str(len(data))+" bản ghi thỏa mãn điều kiện",parent=self.root)
                    conn.commit()
                else:
                    self.TeacherTable.delete(*self.TeacherTable.get_children())
                    messagebox.showinfo("Thông báo", " Không có bản ghi nào thỏa mãn điều kiện",parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showerror("Lỗi", f"Lý do:{str(es)}", parent=self.root)

    #========================================Function Student======================================

    def get_cursorStd(self, event=""):
            cursor_row = self.StudentTable.focus()
            content = self.StudentTable.item(cursor_row)
            rows = content['values']
            self.var_current_std.set(rows[0])
            self.var_current_substd.set(rows[1])
            self.var_studentsub.set(rows[0])
            self.var_subsubst.set(rows[1])

    def callstudent(self):
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                       port='3306')
        my_cursor = conn.cursor()
        my_cursor.execute("select sinhvien_id from `sinhvien` ")
        ckStudent = my_cursor.fetchall()
        arrayStudent = []
        for cht in ckStudent:
            # print(cht[0])
            arrayStudent.append(str(cht[0]))
        if(self.var_studentsub.get() not in arrayStudent):

            self.var_studentname.set("")
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                           port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("select sinhvien_ten from `sinhvien` where sinhvien_id=%s", (self.var_studentsub.get(),))
            ckStudent = my_cursor.fetchone()
            self.var_studentname.set(ckStudent[0])
        conn.commit()
        conn.close()

    def callstSub(self):
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                       port='3306')
        my_cursor = conn.cursor()
        my_cursor.execute("select monhoc_id from `monhoc` ")
        cksubject = my_cursor.fetchall()
        arraySubject = []
        for cht in cksubject:
            # print(cht[0])
            arraySubject.append(str(cht[0]))
        if(self.var_subsubst.get() not in arraySubject):

            self.var_stSubname.set("")
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                           port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("select monhoc_ten from `monhoc` where monhoc_id=%s", (self.var_subsubst.get(),))
            cksubject = my_cursor.fetchone()
            self.var_stSubname.set(cksubject[0])
        conn.commit()
        conn.close()

    def add_Stddata(self):
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                       port='3306')
        my_cursor = conn.cursor()
        # =========check subject============
        my_cursor.execute("select monhoc_id from monhocsinhvien where sinhvien_id=%s",
                          (self.var_studentsub.get(),))
        ckSubject = my_cursor.fetchall()
        arraySub = []
        for chk in ckSubject:
            arraySub.append(str(chk[0]))

        # ========check student================
        my_cursor.execute("select sinhvien_id from `sinhvien` ")
        ckstudent = my_cursor.fetchall()
        arrayStudent = []
        for cht in ckstudent:
            # print(cht[0])
            arrayStudent.append(str(cht[0]))

        # =========check subject=================
        my_cursor.execute("select monhoc_id from `monhoc` ")
        cksubject = my_cursor.fetchall()
        arraySubject = []
        for chs in cksubject:
            # print(chs[0])
            arraySubject.append(str(chs[0]))
        conn.commit()
        conn.close()
        if self.var_studentsub == "" or self.var_subsubst.get() == "":
                messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin", parent=self.root)
        elif (self.var_subsubst.get() in arraySub):
            messagebox.showerror("Lỗi", "Sinh viên đã có môn học này! Vui lòng kiểm tra lại", parent=self.root)
        elif (self.var_studentsub.get() not in arrayStudent):
            messagebox.showerror("Lỗi", "ID Sinh viên không tồn tại! Vui lòng kiểm tra lại", parent=self.root)
        elif (self.var_subsubst.get() not in arraySubject):
            messagebox.showerror("Lỗi", "ID Môn học không tồn tại! Vui lòng kiểm tra lại", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password='',
                                                   database='diemdanhsv', port='3306')
                my_cursor = conn.cursor()
                my_cursor.execute("insert into monhocsinhvien values(%s,%s)", (
                        self.var_studentsub.get(),
                        self.var_subsubst.get(),
                ))
                conn.commit()
                self.fetch_Stddata()
                self.reset_Stddata()
                conn.close()
                messagebox.showinfo("Thành công", "Thêm thông tin môn học cho Sinh viên thành công",
                                        parent=self.root)
            except Exception as es:
                messagebox.showerror("Lỗi", f"Lý do:{str(es)}", parent=self.root)

    def reset_Stddata(self):
            self.var_studentsub.set("")
            self.var_subsubst.set("")

    def fetch_Stddata(self):
            # global mydata
            # mydata.clear()
            conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                           port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("Select * from monhocsinhvien")
            data = my_cursor.fetchall()
            if len(data) != 0:
                self.StudentTable.delete(*self.StudentTable.get_children())
                for i in data:
                    self.StudentTable.insert("", END, values=i)
                    mydata.append(i)
                conn.commit()
                self.var_com_searchstd.set("ID Sinh viên")
                self.var_searchstd.set("")
            conn.close()

    def update_Stddata(self):
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                       port='3306')
        my_cursor = conn.cursor()
        # =========check subject============
        my_cursor.execute("select monhoc_id from monhocsinhvien where sinhvien_id=%s",
                          (self.var_studentsub.get(),))
        ckSubject = my_cursor.fetchall()
        arraySub = []
        for chk in ckSubject:
            arraySub.append(str(chk[0]))

        # ========check student================
        my_cursor.execute("select sinhvien_id from `sinhvien` ")
        ckstudent = my_cursor.fetchall()
        arrayStudent = []
        for cht in ckstudent:
            # print(cht[0])
            arrayStudent.append(str(cht[0]))

        # =========check subject=================
        my_cursor.execute("select monhoc_id from `monhoc` ")
        cksubject = my_cursor.fetchall()
        arraySubject = []
        for chs in cksubject:
            # print(chs[0])
            arraySubject.append(str(chs[0]))
        conn.commit()
        conn.close()
        if self.var_studentsub == "" or self.var_subsubst.get() == "":
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin", parent=self.root)
        elif (self.var_subsubst.get() in arraySub):
            messagebox.showerror("Lỗi", "Sinh viên đã có môn học này! Vui lòng kiểm tra lại", parent=self.root)
        elif (self.var_studentsub.get() not in arrayStudent):
            messagebox.showerror("Lỗi", "ID Sinh viên không tồn tại! Vui lòng kiểm tra lại", parent=self.root)
        elif (self.var_subsubst.get() not in arraySubject):
            messagebox.showerror("Lỗi", "ID Môn học không tồn tại! Vui lòng kiểm tra lại", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Bạn có muốn cập nhật bản ghi này không?", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host='localhost', user='root', password='',
                                                       database='diemdanhsv', port='3306')
                    my_cursor = conn.cursor()
                    my_cursor.execute("UPDATE `monhocsinhvien` SET `sinhvien_id` = %s, `monhoc_id` = %s WHERE "
                                          "`monhocsinhvien`.`sinhvien_id` = %s AND `monhocsinhvien`.`monhoc_id` = %s",
                                          (
                                              self.var_studentsub.get(),
                                              self.var_subsubst.get(),
                                              self.var_current_std.get(),
                                              self.var_current_substd.get(),
                                          ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Thành công", "Cập nhật thông tin môn Sinh viên viên thành công", parent=self.root)
                conn.commit()
                self.reset_Stddata()
                self.fetch_Stddata()
                conn.close()
            except Exception as es:
                messagebox.showerror("Lỗi", f"Lý do:{str(es)}", parent=self.root)

        # Delete Function
    def delete_Stddata(self):
            if self.var_studentsub == "" or self.var_subsubst.get() == "":
                messagebox.showerror("Lỗi", "Không được bỏ trống thông tin! ", parent=self.root)
            else:
                try:
                    delete = messagebox.askyesno("Xoá bản ghi", "Bạn có muốn xóa bản ghi này ?", parent=self.root)
                    if delete > 0:
                        conn = mysql.connector.connect(host='localhost', user='root', password='',
                                                       database='diemdanhsv', port='3306')
                        my_cursor = conn.cursor()
                        sql = "delete from monhocsinhvien where sinhvien_id=%s and monhoc_id=%s"
                        val = (self.var_studentsub.get(), self.var_subsubst.get(),)
                        my_cursor.execute(sql, val)
                    else:
                        if not delete:
                            return
                    conn.commit()
                    # self.fetch_data()p
                    conn.close()
                    messagebox.showinfo("Xóa", "Xóa bản ghi thành công", parent=self.root)
                    self.reset_Stddata()
                    self.fetch_Stddata()
                except Exception as es:
                    messagebox.showerror("Lỗi", f"Lý do:{str(es)}", parent=self.root)

    def search_Stddata(self):
            if self.var_com_searchstd.get() == "" or self.var_searchstd.get() == "":
                messagebox.showerror("Lỗi !", "Vui lòng nhập thông tin đầy đủ",parent=self.root)

            else:
                try:
                    conn = mysql.connector.connect(host='localhost', user='root', password='',
                                                   database='diemdanhsv', port='3306')
                    my_cursor = conn.cursor()  # "ID Điểm Danh", "Ngày", "ID Sinh viên"
                    if (self.var_com_searchstd.get() == "ID Sinh viên"):
                        self.var_com_searchstd.set("sinhvien_id")
                    elif (self.var_com_searchstd.get() == "ID môn học"):
                        self.var_com_searchstd.set("monhoc_id")

                    my_cursor.execute("select * from monhocsinhvien where " + str(
                        self.var_com_searchstd.get()) + " Like '%" + str(self.var_searchstd.get()) + "%'")
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
                                        
                               
    def insert_stu_subject(self):
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
            # print(mydata[1])

            conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                           port='3306')
            my_cursor = conn.cursor()
            sql_insert_query = "insert IGNORE into monhocsinhvien values(%s,%s)"
            

            my_cursor.executemany(sql_insert_query, mydata)
            conn.commit()
            self.fetch_Stddata()
            self.reset_Stddata()
            messagebox.showinfo("Thông báo", "Thêm danh sách môn học cho sinh viên thành công!!!", parent=self.root)
            conn.close()
        except Exception as es:
            messagebox.showerror("Lỗi", f"Due To:{str(es)}", parent=self.root)

                    
if __name__=="__main__":
    root=Tk() #khoi tao cua so va gan root vao
    obj=Subject(root)
    root.mainloop()# cua so hien len