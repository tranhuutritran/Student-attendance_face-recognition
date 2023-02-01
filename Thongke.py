import os
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
import PIL.Image
from time import strftime
from math import *
from tkinter import messagebox
import mysql.connector
import csv

mydatalate=[]
mydataNot=[]
mydataNotInAtt=[]
mydataall=[]
listdata=[]



value_from_home = None
def new_tcid(value):
    global value_from_home
    value_from_home = value

class report:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.state('zoomed')
        self.root.configure(bg='#7fe5ea')
        self.root.title("Hệ thống điểm danh (Khoa Phát triển Nông thôn - Đại học Cần Thơ)")
        today = strftime("%M-%m-%d")

        #===========variable============
        self.student = StringVar()
        self.att=StringVar()
        self.late=StringVar()
        self.noatt=StringVar()

        img3 = PIL.Image.open(r"ImageFaceDetect\bg2.png")
        img3 = img3.resize((1350, 700), PIL.Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1350, height=700)
        
        # ==================================heading====================================
        # =========time=========
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(self.root,font=("times new roman", 11, "bold"),bg="#7fe5ea", fg="#000000")
        lbl.place(x=80,y=20,width=100,height=18)
        time()
        lbl1 = Label(self.root,text=today, font=("times new roman", 11, "bold"), bg="#7fe5ea", fg="#000000")
        lbl1.place(x=80, y=45, width=100, height=18)


        # ========title=========
        self.txt = "THỐNG KÊ HỆ THỐNG"
        self.count = 0
        self.text = ''
        self.heading = Label(self.root, text=self.txt, font=("times new roman", 20, "bold"), bg="#7fe5ea", fg="#0000CC",
                             bd=0, relief=FLAT)
        self.heading.place(x=400, y=22, width=650,height=40)
        
        main_frame = Frame(bg_img, bd=2, bg="#7fe5ea")
        main_frame.place(x=20, y=69, width=1482, height=692)
        # ===================Top_label=====================
        Top_frame=LabelFrame(main_frame, bd=0, bg="#7fe5ea",
                                font=("times new roman", 12, "bold"))
        Top_frame.place(x=5,y=0,width=1280,height=120)
   
        print(value_from_home)
        self.giangvien_id=value_from_home #Chọn teacher id = id người ms đăng nhập
        
        
        subject_array = [] #array for append id_buoihoc,subject

        #call lesson_id from db
        if(value_from_home=="0" or value_from_home==None):
            conn = mysql.connector.connect(host='localhost', user='root', password='',
                                           database='diemdanhsv', port='3306')
            my_cursor = conn.cursor()
            self.giangvien_id=0
            my_cursor.execute(
                "SELECT monhocgiangvien.monhoc_id, monhoc.monhoc_ten from monhocgiangvien, monhoc where monhocgiangvien.monhoc_id=monhoc.monhoc_id ")
            subject_ls = my_cursor.fetchall()
            for i in subject_ls:
                t = str(i).replace("'", "", 6).replace("(", "").replace(")", "").replace(" ", "") ##Subject_lsid to attendance
                # print(t)
                subject_array.append(t)
                
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='',
                                           database='diemdanhsv', port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute(
                "SELECT monhocgiangvien.monhoc_id, monhoc.monhoc_ten from monhocgiangvien, monhoc where monhocgiangvien.monhoc_id=monhoc.monhoc_id and giangvien_id=%s",
                (self.giangvien_id,))
            subject_ls = my_cursor.fetchall()
            for i in subject_ls:
                t = str(i).replace("'", "", 6).replace("(", "").replace(")", "").replace(" ", "") ##Subject_lsid to attendance
                # print(t)
                subject_array.append(t)
                
        #===================select_for_txt=================
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                       port='3306')
        my_cursor = conn.cursor()

        #========student==========
        if(value_from_home=="0" or value_from_home==None):
            conn = mysql.connector.connect(host='localhost', user='root', password='',
                                            database='diemdanhsv', port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("select count(*) from sinhvien")
            count_st = my_cursor.fetchall()
            self.student.set(count_st[0])
            conn.commit()
            conn.close()
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='',
                                            database='diemdanhsv', port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("select count(*) from monhocsinhvien,monhoc,monhocgiangvien WHERE monhocsinhvien.monhoc_id=monhoc.monhoc_id AND monhoc.monhoc_id=monhocgiangvien.monhoc_id AND monhocgiangvien.giangvien_id=%s", (self.giangvien_id,))
            count_st = my_cursor.fetchall()
            self.student.set(count_st[0])
            conn.commit()
            conn.close()
                 
        #=======attendance========
        if(value_from_home=="0" or value_from_home==None):
            conn = mysql.connector.connect(host='localhost', user='root', password='',
                                            database='diemdanhsv', port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("select count(*) from diemdanh")
            count_att = my_cursor.fetchall()
            self.att.set(count_att[0])
            conn.commit()
            conn.close()
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='',
                                            database='diemdanhsv', port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("select count(*) from diemdanh,buoihoc WHERE diemdanh.buoihoc_id=buoihoc.buoihoc_id AND buoihoc.giangvien_id=%s", (self.giangvien_id,))
            count_att = my_cursor.fetchall()
            self.att.set(count_att[0])
            conn.commit()
            conn.close()
            
        #=======late=============
        if(value_from_home=="0" or value_from_home==None):
            conn = mysql.connector.connect(host='localhost', user='root', password='',
                                            database='diemdanhsv', port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("select  count(sinhvien_id) from diemdanh where diemdanh_trangthai like '%Đi muộn%'")
            count_late = my_cursor.fetchall()
            self.late.set(count_late[0])
            conn.commit()
            conn.close()
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='',
                                            database='diemdanhsv', port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("select  count(*) from diemdanh,buoihoc WHERE diemdanh.buoihoc_id=buoihoc.buoihoc_id AND buoihoc.giangvien_id=%s AND diemdanh_trangthai like '%Đi muộn%'", (self.giangvien_id,))
            count_late = my_cursor.fetchall()
            self.late.set(count_late[0])
            conn.commit()
            conn.close()
            
        #========no-attendance=======
        if(value_from_home=="0" or value_from_home==None):
            conn = mysql.connector.connect(host='localhost', user='root', password='',
                                            database='diemdanhsv', port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT COUNT(*) FROM (select sinhvien.sinhvien_id,sinhvien_ten,lop_id,monhoc.monhoc_id from sinhvien,buoihoc,monhocsinhvien,`monhoc` where sinhvien.sinhvien_id=monhocsinhvien.sinhvien_id and monhocsinhvien.monhoc_id=`monhoc`.monhoc_id and `monhoc`.monhoc_id=buoihoc.monhoc_id and CONCAT(sinhvien.sinhvien_id,buoihoc_id) not in (select CONCAT(sinhvien_id,buoihoc_id) from diemdanh )  UNION all select sinhvien.sinhvien_id,sinhvien_ten,lop_id,monhoc.monhoc_id from sinhvien, diemdanh,`monhoc`,buoihoc where diemdanh_trangthai like '%Vắng%' and buoihoc.monhoc_id=monhoc.monhoc_id and diemdanh.buoihoc_id=buoihoc.buoihoc_id AND diemdanh.sinhvien_id=sinhvien.sinhvien_id) AS T1")
            count_noatt = my_cursor.fetchall()
            self.noatt.set(count_noatt[0])
            conn.commit()
            conn.close()
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='',
                                            database='diemdanhsv', port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT COUNT(*) FROM (select sinhvien.sinhvien_id,sinhvien_ten,lop_id,monhoc.monhoc_id from sinhvien,buoihoc,monhocsinhvien,`monhoc` where sinhvien.sinhvien_id=monhocsinhvien.sinhvien_id and monhocsinhvien.monhoc_id=`monhoc`.monhoc_id and `monhoc`.monhoc_id=buoihoc.monhoc_id and giangvien_id=%s and CONCAT(sinhvien.sinhvien_id,buoihoc_id) not in (select CONCAT(sinhvien_id,buoihoc_id) from diemdanh )  UNION all select sinhvien.sinhvien_id,sinhvien_ten,lop_id,monhoc.monhoc_id from sinhvien, diemdanh,`monhoc`,buoihoc where diemdanh_trangthai like '%Vắng%' and buoihoc.monhoc_id=monhoc.monhoc_id and diemdanh.buoihoc_id=buoihoc.buoihoc_id AND diemdanh.sinhvien_id=sinhvien.sinhvien_id and giangvien_id=%s) AS T1", (self.giangvien_id,self.giangvien_id,))
            count_noatt = my_cursor.fetchall()
            self.noatt.set(count_noatt[0])      
            conn.commit()
            conn.close()


        #student_frame
        student_frame=LabelFrame(Top_frame,bd=1,bg='#27a9e3')
        student_frame.place(x=5,y=0,width=245,height=110)

        img_student = PIL.Image.open(r"ImageFaceDetect\sv.png")
        img_student = img_student.resize((40, 40), PIL.Image.ANTIALIAS)
        self.photoimgsv = ImageTk.PhotoImage(img_student)
        student_img = Label(student_frame, image=self.photoimgsv, bg="#27a9e3")
        student_img.place(x=20, y=40, width=50, height=50)
        student_text=Label(student_frame,text="Số sinh viên",font=("times new roman", 16, "bold"),fg="white",bg="#27a9e3")
        student_text.place(x=80,y=30)
        student_text = Label(student_frame,textvariable=self.student, font=("times new roman", 18, "bold"),fg="white",bg="#27a9e3")
        student_text.place(x=80, y=70)

        #attendance_success
        att_frame = LabelFrame(Top_frame, bd=1, bg='#28b779')
        att_frame.place(x=260, y=0, width=248, height=110)

        img_att = PIL.Image.open(r"ImageFaceDetect\sodd.png")
        img_att = img_att.resize((40, 40), PIL.Image.ANTIALIAS)
        self.photoimgatt = ImageTk.PhotoImage(img_att)
        att_img = Label(att_frame, image=self.photoimgatt, bg="#28b779")
        att_img.place(x=20, y=40, width=50, height=50)
        att_text = Label(att_frame, text="Số bản điểm danh", font=("times new roman", 16, "bold"), fg="white",
                             bg="#28b779")
        att_text.place(x=80, y=30)
        att_text = Label(att_frame, textvariable=self.att, font=("times new roman", 18, "bold"), fg="white",
                             bg="#28b779")
        att_text.place(x=80, y=70)

        #late_attendance
        late_frame = LabelFrame(Top_frame, bd=1, bg='#852b99')
        late_frame.place(x=515, y=0, width=245, height=110)

        img_late = PIL.Image.open(r"ImageFaceDetect\late.png")
        img_late = img_late.resize((40, 40), PIL.Image.ANTIALIAS)
        self.photoimglate = ImageTk.PhotoImage(img_late)
        late_img = Label(late_frame, image=self.photoimglate, bg="#852b99")
        late_img.place(x=20, y=40, width=50, height=50)
        late_text = Label(late_frame, text="Số lần đi muộn", font=("times new roman", 16, "bold"), fg="white",
                         bg="#852b99")
        late_text.place(x=80, y=30)
        late_text = Label(late_frame, textvariable=self.late, font=("times new roman", 18, "bold"), fg="white",
                         bg="#852b99")
        late_text.place(x=80, y=70)

        #no_attendance
        late_frame = LabelFrame(Top_frame, bd=1, bg='#DC143C')
        late_frame.place(x=770, y=0, width=245, height=110)

        img_noatt = PIL.Image.open(r"ImageFaceDetect\vang.png")
        img_noatt = img_noatt.resize((40, 40), PIL.Image.ANTIALIAS)
        self.photoimgnoatt = ImageTk.PhotoImage(img_noatt)
        noatt_img = Label(late_frame, image=self.photoimgnoatt, bg="#DC143C")
        noatt_img.place(x=20, y=40, width=50, height=50)
        noatt_text = Label(late_frame, text="Số lần vắng", font=("times new roman", 16, "bold"), fg="white",
                          bg="#DC143C")
        noatt_text.place(x=80, y=30)
        noatt_text = Label(late_frame, textvariable=self.noatt, font=("times new roman", 18, "bold"), fg="white",
                          bg="#DC143C")
        noatt_text.place(x=80, y=70)
        
        #list data
        late_frame = LabelFrame(Top_frame, bd=1, bg='#000044')
        late_frame.place(x=1025, y=0, width=255, height=110)
        

        noatt_text = Label(late_frame, text="Danh sách sinh viên", font=("times new roman", 16, "bold"), fg="white",
                          bg="#000044")
        noatt_text.place(x=40, y=10)
        
        noatt_text1 = Label(late_frame, text="ID Môn học:", font=("times new roman", 11, "bold"), fg="white",
                          bg="#000044")
        noatt_text1.place(x=5, y=50)

        self.selectsub=StringVar()
        self.lesson_combo = ttk.Combobox(late_frame, textvariable=self.selectsub ,font=("times new roman", 11, "bold"), state="readonly",
                                    width=15)
        self.lesson_combo.place(x=100, y=50)
        self.lesson_combo["values"] = subject_array
        self.lesson_combo.bind("<<ComboboxSelected>>", self.callbackFunc)
        
        export_btn = Button(late_frame, text="Xuất CSV",
                                font=("times new roman", 10, "bold"), bg="#fbd568",command=self.exportList,
                                fg="#945305",
                                width=10)
        export_btn.place(x=100, y=80)

        
        #====================Left_label====================
        Left_frame = LabelFrame(main_frame, bd=2, bg="#6EC3C9",
                               font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=125, width=645, height=470)

        noatt_group = LabelFrame(Left_frame, bd=2, bg="#6EC3C9", text="Danh sách điểm danh",
                                font=("times new roman", 13, "bold"), fg="#FF0000", relief=RIDGE)
        noatt_group.place(x=5, y=5, width=630, height=455)
        
        
        self.noatt_text1 = Label(noatt_group, text="ID Môn học:", font=("times new roman", 11, "bold"), fg="black",
                          bg="#6EC3C9")
        self.noatt_text1.grid(row=0, column=0,padx=5, pady=5, sticky=W)
        
        self.selectsub1=StringVar()
        self.selectsub1.trace("w", lambda name, index, mode, selectsub1=self.selectsub1: self.callback())
        self.lesson_combo = ttk.Combobox(noatt_group, textvariable=self.selectsub1 ,font=("times new roman", 11, "bold"), state="readonly",
                                    width=10)
        self.lesson_combo.grid(row=0, column=1,padx=5, pady=5, sticky=W)
        self.lesson_combo["values"] = subject_array
        self.lesson_combo.bind("<<ComboboxSelected>>", self.callbackFunc1)

        self.noatt_text1 = Label(noatt_group, text="Buổi học:", font=("times new roman", 11, "bold"), fg="black",
                          bg="#6EC3C9")
        self.noatt_text1.grid(row=0, column=2, padx=5,pady=5, sticky=W)

        self.selectlesson=StringVar()
        self.lesson_combo1 = ttk.Combobox(noatt_group, textvariable=self.selectlesson,font=("times new roman", 11, "bold"), state="readonly",
                                    width=3)
        self.lesson_combo1.grid(row=0, column=3, padx=5, pady=5, sticky=W)
        

        searchnoatt_btn = Button(noatt_group, text="Tìm kiếm",
                              font=("times new roman", 10, "bold"), bg="#fbd568", fg="#945305",command=self.search_NoAttTable,
                              width=10)
        searchnoatt_btn.grid(row=0, column=4, padx=5)

        showAllnoatt_btn = Button(noatt_group, text="Xem tất cả",
                               font=("times new roman", 10, "bold"), bg="#fbd568",command=self.fetch_Notdata,
                               fg="#945305",
                               width=10)
        showAllnoatt_btn.grid(row=0, column=5, padx=5)

        exportNoatt_btn = Button(noatt_group, text="Xuất CSV",
                                font=("times new roman", 10, "bold"), bg="#fbd568", command=self.exportUnpresetCsv,
                                fg="#945305",
                                width=10)
        exportNoatt_btn.grid(row=0, column=6, padx=5)

        # table_frame
        tableatt_frame = Frame(noatt_group, bd=2, relief=RIDGE, bg="#5dc9ef")
        tableatt_frame.place(x=15, y=38, width=605, height=390)

        # scroll bar
        scroll_x = ttk.Scrollbar(tableatt_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tableatt_frame, orient=VERTICAL)

        self.NoAttTable = ttk.Treeview(tableatt_frame, column=(
            "studentid", "name","class", "date","subjectid", "subname", "lessonid", "status"),
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.NoAttTable.xview)
        scroll_y.config(command=self.NoAttTable.yview)

        self.NoAttTable.heading("studentid", text="ID SV")
        self.NoAttTable.heading("name", text="Tên Sinh viên")
        self.NoAttTable.heading("class", text="Lớp")
        self.NoAttTable.heading("date", text="Ngày học")
        self.NoAttTable.heading("subjectid", text="ID Môn học")
        self.NoAttTable.heading("subname", text="Môn học")
        self.NoAttTable.heading("lessonid", text="ID Buổi học")
        self.NoAttTable.heading("status", text="Trạng thái")

        self.NoAttTable["show"] = "headings"
        self.NoAttTable.column("studentid", width=100, anchor=CENTER)
        self.NoAttTable.column("name", width=140)
        self.NoAttTable.column("class", width=90,anchor=CENTER)
        self.NoAttTable.column("date", width=100, anchor=CENTER)
        self.NoAttTable.column("subjectid", width=100,anchor=CENTER)
        self.NoAttTable.column("subname", width=150,anchor=CENTER)
        self.NoAttTable.column("lessonid", width=90, anchor=CENTER)
        self.NoAttTable.column("status", width=110, anchor=CENTER)

        self.NoAttTable.pack(fill=BOTH, expand=1)
        self.fetch_Notdata()
        # self.LateTable.bind("<ButtonRelease>", self.get_cursorLate)

        #===================right_label====================
        Right_frame = LabelFrame(main_frame, bd=2, bg="#6EC3C9",
                                font=("times new roman", 12, "bold"))
        Right_frame.place(x=670, y=125, width=615, height=470)

        unright_group = LabelFrame(Right_frame, bd=2, bg="#6EC3C9", text="Tổng lần vắng",
                                font=("times new roman", 13, "bold"), fg="#FF0000", relief=RIDGE)
        unright_group.place(x=5, y=5, width=600, height=455)
        
        self.noatt_text1 = Label(unright_group, text="ID Môn học:", font=("times new roman", 11, "bold"), fg="black",
                          bg="#6EC3C9")
        self.noatt_text1.grid(row=0, column=0,padx=5, pady=5, sticky=W)
        
        self.var_com_searchcouatt=StringVar()
        self.lesson_combo = ttk.Combobox(unright_group, textvariable=self.var_com_searchcouatt ,font=("times new roman", 11, "bold"), state="readonly",
                                    width=12)
        self.lesson_combo.grid(row=0, column=1, padx=15, pady=5, sticky=W)
        self.lesson_combo["values"] = subject_array
        self.lesson_combo.bind("<<ComboboxSelected>>", self.callbackFunc2)

        searchnoatt_btn = Button(unright_group, text="Tìm kiếm",
                              font=("times new roman", 10, "bold"), bg="#fbd568", fg="#945305",command=self.search_Coudata,
                              width=10)
        searchnoatt_btn.grid(row=0, column=2, padx=15)

        showAllnoatt_btn = Button(unright_group, text="Xem tất cả",
                               font=("times new roman", 10, "bold"), bg="#fbd568",command=self.fetch_Coudata,
                               fg="#945305",
                               width=10)
        showAllnoatt_btn.grid(row=0, column=3, padx=15)

        exportNoatt_btn = Button(unright_group, text="Xuất CSV",
                                font=("times new roman", 10, "bold"), bg="#fbd568", command=self.exportCsvcouall,
                                fg="#945305",
                                width=10)
        exportNoatt_btn.grid(row=0, column=4, padx=15)

        # table_frame
        tableatt_frame = Frame(unright_group, bd=2, relief=RIDGE, bg="white")
        tableatt_frame.place(x=10, y=38, width=580, height=390)

        # scroll bar
        scroll_x = ttk.Scrollbar(tableatt_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tableatt_frame, orient=VERTICAL)

        self.CouAttTable = ttk.Treeview(tableatt_frame, column=(
            "studentid", "name","class", "subjectid","subjectname", "sobuoivang"),
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.CouAttTable.xview)
        scroll_y.config(command=self.CouAttTable.yview)

        self.CouAttTable.heading("studentid", text="ID SV")
        self.CouAttTable.heading("name", text="Tên Sinh viên")
        self.CouAttTable.heading("class", text="Lớp")
        self.CouAttTable.heading("subjectid", text="ID Môn học")
        self.CouAttTable.heading("subjectname", text="Môn học")
        self.CouAttTable.heading("sobuoivang", text="Số buổi vắng")

        self.CouAttTable["show"] = "headings"
        
        self.CouAttTable.column("studentid", width=100, anchor=CENTER)
        self.CouAttTable.column("name", width=140)
        self.CouAttTable.column("class", width=90,anchor=CENTER)
        self.CouAttTable.column("subjectid", width=100,anchor=CENTER)
        self.CouAttTable.column("subjectname", width=100,anchor=CENTER)
        self.CouAttTable.column("sobuoivang", width=100, anchor=CENTER)

        self.CouAttTable.pack(fill=BOTH, expand=1)
        self.fetch_Coudata()
        # self.LateTable.bind("<ButtonRelease>", self.get_cursorLate)
        
        
    def callbackFunc(self,event):                
        mls = event.widget.get()
        # print(mls)
        if self.selectsub.get()=="":
            self.btnOpen['state'] = "disabled"
        else:
            c = str(mls).split(",")
            self.monhoc_id=str(c[0])
            # print(str(c[0]))  
            
    def callbackFunc1(self,event):                
        mls = event.widget.get()
        # print(mls)
        if self.selectsub1.get()=="":
            self.btnOpen['state'] = "disabled"
        else:
            c = str(mls).split(",")
            self.monhoc_id=str(c[0])
            self.selectsub1.set(str(c[0]))
            self.lesson_combo1.set("")
            # print(str(c[0]))    
                            
    def callback(self):
        leson_array = []
        self.lesson_combo1["values"] = leson_array
        conn = mysql.connector.connect(host='localhost', user='root', password='',
                                            database='diemdanhsv', port='3306')
        my_cursor = conn.cursor()
        my_cursor.execute(
                    "SELECT buoihoc_id from buoihoc where monhoc_id=%s",
            (self.selectsub1.get(),))
        subject_ls = my_cursor.fetchall()
        for i in subject_ls:
            t = str(i).replace("(", "").replace(")", "").replace(",", "") ##Subject_lsid to attendance
                    # print()
            leson_array.append(t)
            self.lesson_combo1["values"] = leson_array               
                    
    def callbackFunc2(self,event):                
        mls = event.widget.get()
        # print(mls)
        if self.var_com_searchcouatt.get()=="":
            self.btnOpen['state'] = "disabled"
        else:
            c = str(mls).split(",")
            self.subid_couatt=str(c[0])

            
    def fetch_Notdata(self):
            # global mydata
            mydataNot.clear()            
            if(value_from_home=="0" or value_from_home==None):
                conn = mysql.connector.connect(host='localhost', user='root', password='',
                                            database='diemdanhsv', port='3306')
                my_cursor = conn.cursor()
                self.giangvien_id=0
                my_cursor.execute("SELECT T1.sinhvien_id,T1.sinhvien_ten,T1.lop_id,T1.diemdanh_ngay,T1.monhoc_id, T1.monhoc_ten,T1.buoihoc_id,T1.diemdanh_trangthai FROM (select diemdanh.sinhvien_id,sinhvien.sinhvien_ten,sinhvien.lop_id,diemdanh.diemdanh_ngay,monhoc.monhoc_id, monhoc_ten,buoihoc.buoihoc_id,diemdanh_trangthai from sinhvien,diemdanh,`monhoc`,buoihoc where   diemdanh_trangthai like '%Đi muộn%' and buoihoc.monhoc_id=monhoc.monhoc_id and diemdanh.buoihoc_id=buoihoc.buoihoc_id and sinhvien.sinhvien_id=diemdanh.sinhvien_id UNION all select diemdanh.sinhvien_id,sinhvien.sinhvien_ten,sinhvien.lop_id, diemdanh.diemdanh_ngay,monhoc.monhoc_id,monhoc_ten,buoihoc.buoihoc_id,diemdanh_trangthai from sinhvien,diemdanh,`monhoc`,buoihoc where   diemdanh_trangthai like '%Vắng%' and buoihoc.monhoc_id=monhoc.monhoc_id and diemdanh.buoihoc_id=buoihoc.buoihoc_id and sinhvien.sinhvien_id=diemdanh.sinhvien_id UNION all select sinhvien.sinhvien_id,sinhvien_ten,sinhvien.lop_id,buoihoc_ngay,monhoc.monhoc_id,monhoc_ten,buoihoc_id,'Không điểm danh' from sinhvien,buoihoc,monhocsinhvien,`monhoc` where sinhvien.sinhvien_id=monhocsinhvien.sinhvien_id and monhocsinhvien.monhoc_id=`monhoc`.monhoc_id and `monhoc`.monhoc_id=buoihoc.monhoc_id and CONCAT(sinhvien.sinhvien_id,buoihoc_id) not in (select CONCAT(sinhvien_id,buoihoc_id) from diemdanh) UNION ALL select sinhvien.sinhvien_id,sinhvien_ten,sinhvien.lop_id,buoihoc_ngay,monhoc.monhoc_id,monhoc_ten,diemdanh.buoihoc_id,diemdanh_trangthai from sinhvien,diemdanh,buoihoc,monhoc WHERE sinhvien.sinhvien_id=diemdanh.sinhvien_id AND diemdanh.buoihoc_id=buoihoc.buoihoc_id AND buoihoc.monhoc_id=monhoc.monhoc_id AND diemdanh.diemdanh_trangthai='Có mặt') AS T1 ORDER BY T1.sinhvien_id ASC")
                subject_ls = my_cursor.fetchall()
                if len(subject_ls) != 0:
                    self.NoAttTable.delete(*self.NoAttTable.get_children())
                    for i in subject_ls:
                        self.NoAttTable.insert("", END, values=i)
                        mydataNot.append(i)
                    conn.commit()
                conn.close()
            else:
                conn = mysql.connector.connect(host='localhost', user='root', password='',
                                            database='diemdanhsv', port='3306')
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT T1.sinhvien_id,T1.sinhvien_ten,T1.lop_id,T1.diemdanh_ngay,T1.monhoc_id, T1.monhoc_ten,T1.buoihoc_id,T1.diemdanh_trangthai FROM(select diemdanh.sinhvien_id,sinhvien.sinhvien_ten, sinhvien.lop_id,diemdanh.diemdanh_ngay,monhoc.monhoc_id, monhoc_ten,buoihoc.buoihoc_id,diemdanh_trangthai from sinhvien, diemdanh,`monhoc`,buoihoc,monhocgiangvien where   diemdanh_trangthai like '%Đi muộn%' and buoihoc.monhoc_id=monhoc.monhoc_id and diemdanh.buoihoc_id=buoihoc.buoihoc_id and monhocgiangvien.monhoc_id=monhoc.monhoc_id and monhocgiangvien.giangvien_id=%s and sinhvien.sinhvien_id=diemdanh.sinhvien_id UNION ALL select diemdanh.sinhvien_id, sinhvien.sinhvien_ten,sinhvien.lop_id,diemdanh.diemdanh_ngay,monhoc.monhoc_id,monhoc_ten,buoihoc.buoihoc_id,diemdanh_trangthai from sinhvien,diemdanh,`monhoc`,buoihoc, monhocgiangvien where   diemdanh_trangthai like '%Vắng%' and buoihoc.monhoc_id=monhoc.monhoc_id and diemdanh.buoihoc_id=buoihoc.buoihoc_id and monhocgiangvien.monhoc_id=monhoc.monhoc_id and monhocgiangvien.giangvien_id=%s and sinhvien.sinhvien_id=diemdanh.sinhvien_id UNION ALL select sinhvien.sinhvien_id,sinhvien_ten,sinhvien.lop_id,buoihoc_ngay,monhoc.monhoc_id,monhoc_ten,buoihoc_id,'Không điểm danh' from sinhvien,buoihoc,monhocsinhvien,`monhoc`, monhocgiangvien where sinhvien.sinhvien_id=monhocsinhvien.sinhvien_id and monhocsinhvien.monhoc_id=`monhoc`.monhoc_id and `monhoc`.monhoc_id=buoihoc.monhoc_id and CONCAT(sinhvien.sinhvien_id,buoihoc_id) not in (select CONCAT(sinhvien_id,buoihoc_id) from diemdanh) and monhocgiangvien.monhoc_id=monhoc.monhoc_id and monhocgiangvien.giangvien_id=%s UNION ALL select sinhvien.sinhvien_id,sinhvien_ten,sinhvien.lop_id,buoihoc_ngay,monhoc.monhoc_id,monhoc_ten,diemdanh.buoihoc_id,diemdanh_trangthai from sinhvien,diemdanh,buoihoc,monhoc WHERE sinhvien.sinhvien_id=diemdanh.sinhvien_id AND diemdanh.buoihoc_id=buoihoc.buoihoc_id AND buoihoc.monhoc_id=monhoc.monhoc_id AND diemdanh.diemdanh_trangthai='Có mặt' AND buoihoc.giangvien_id=%s) AS T1 ORDER BY T1.sinhvien_id ASC",(self.giangvien_id,self.giangvien_id,self.giangvien_id,self.giangvien_id,))
                subject_ls = my_cursor.fetchall()
                if len(subject_ls) != 0:
                    self.NoAttTable.delete(*self.NoAttTable.get_children())
                    for i in subject_ls:
                        self.NoAttTable.insert("", END, values=i)
                        mydataNot.append(i)
                    conn.commit()
                conn.close()
                
    def search_NoAttTable(self):
        if(value_from_home=="0" or value_from_home==None):
            if self.selectlesson.get()=="":
                messagebox.showerror("Lỗi !","Vui lòng nhập thông tin đầy đủ",parent=self.root)

            else:
                try:
                    conn = mysql.connector.connect(host='localhost', user='root', password='',
                                                database='diemdanhsv', port='3306')
                    my_cursor = conn.cursor()#"ID Điểm Danh", "Ngày", "ID Sinh viên"
                    
                    mydataNot.clear()
                    my_cursor.execute("SELECT T1.sinhvien_id,T1.sinhvien_ten,T1.lop_id,T1.diemdanh_ngay,T1.monhoc_id, T1.monhoc_ten,T1.buoihoc_id,T1.diemdanh_trangthai FROM (select diemdanh.sinhvien_id,sinhvien.sinhvien_ten,sinhvien.lop_id,diemdanh.diemdanh_ngay,monhoc.monhoc_id, monhoc_ten,buoihoc.buoihoc_id,diemdanh_trangthai from sinhvien,diemdanh,`monhoc`,buoihoc where   diemdanh_trangthai like '%Đi muộn%' and buoihoc.monhoc_id=monhoc.monhoc_id and diemdanh.buoihoc_id=buoihoc.buoihoc_id and sinhvien.sinhvien_id=diemdanh.sinhvien_id UNION all select diemdanh.sinhvien_id,sinhvien.sinhvien_ten,sinhvien.lop_id, diemdanh.diemdanh_ngay,monhoc.monhoc_id,monhoc_ten,buoihoc.buoihoc_id,diemdanh_trangthai from sinhvien,diemdanh,`monhoc`,buoihoc where   diemdanh_trangthai like '%Vắng%' and buoihoc.monhoc_id=monhoc.monhoc_id and diemdanh.buoihoc_id=buoihoc.buoihoc_id and sinhvien.sinhvien_id=diemdanh.sinhvien_id UNION all select sinhvien.sinhvien_id,sinhvien_ten,sinhvien.lop_id,buoihoc_ngay,monhoc.monhoc_id,monhoc_ten,buoihoc_id,'Không điểm danh' from sinhvien,buoihoc,monhocsinhvien,`monhoc` where sinhvien.sinhvien_id=monhocsinhvien.sinhvien_id and monhocsinhvien.monhoc_id=`monhoc`.monhoc_id and `monhoc`.monhoc_id=buoihoc.monhoc_id and CONCAT(sinhvien.sinhvien_id,buoihoc_id) not in (select CONCAT(sinhvien_id,buoihoc_id) from diemdanh) UNION ALL select sinhvien.sinhvien_id,sinhvien_ten,sinhvien.lop_id,buoihoc_ngay,monhoc.monhoc_id,monhoc_ten,diemdanh.buoihoc_id,diemdanh_trangthai from sinhvien,diemdanh,buoihoc,monhoc WHERE sinhvien.sinhvien_id=diemdanh.sinhvien_id AND diemdanh.buoihoc_id=buoihoc.buoihoc_id AND buoihoc.monhoc_id=monhoc.monhoc_id AND diemdanh.diemdanh_trangthai='Có mặt') AS T1 having "
                                    "T1.buoihoc_id Like '"+str(self.selectlesson.get())+"' ORDER BY T1.sinhvien_id ASC")
                    data=my_cursor.fetchall()
                    if(len(data)!=0):
                        self.NoAttTable.delete(*self.NoAttTable.get_children())
                        for i in data:
                            self.NoAttTable.insert("",END,values=i)
                            mydataNot.append(i)
                        messagebox.showinfo("Thông báo","Có "+str(len(data))+" bản ghi thỏa mãn điều kiện",parent=self.root)
                        conn.commit()
                    else:
                        self.NoAttTable.delete(*self.NoAttTable.get_children())
                        messagebox.showinfo("Thông báo", " Không có bản ghi nào thỏa mãn điều kiện",parent=self.root)
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Lỗi", f"Lý do:{str(es)}", parent=self.root)
                    
        else:
            
            if self.selectlesson.get()=="":
                messagebox.showerror("Lỗi !","Vui lòng nhập thông tin đầy đủ",parent=self.root)

            else:
                try:
                    conn = mysql.connector.connect(host='localhost', user='root', password='',
                                                database='diemdanhsv', port='3306')
                    my_cursor = conn.cursor()#"ID Điểm Danh", "Ngày", "ID Sinh viên"
                    
                    mydataNot.clear()
                    my_cursor.execute("SELECT T1.sinhvien_id,T1.sinhvien_ten,T1.lop_id,T1.diemdanh_ngay,T1.monhoc_id, T1.monhoc_ten,T1.buoihoc_id,T1.diemdanh_trangthai FROM(select diemdanh.sinhvien_id,sinhvien.sinhvien_ten, sinhvien.lop_id,diemdanh.diemdanh_ngay,monhoc.monhoc_id, monhoc_ten,buoihoc.buoihoc_id,diemdanh_trangthai from sinhvien, diemdanh,`monhoc`,buoihoc,monhocgiangvien where   diemdanh_trangthai like '%Đi muộn%' and buoihoc.monhoc_id=monhoc.monhoc_id and diemdanh.buoihoc_id=buoihoc.buoihoc_id and monhocgiangvien.monhoc_id=monhoc.monhoc_id and monhocgiangvien.giangvien_id=%s and sinhvien.sinhvien_id=diemdanh.sinhvien_id UNION ALL select diemdanh.sinhvien_id, sinhvien.sinhvien_ten,sinhvien.lop_id,diemdanh.diemdanh_ngay,monhoc.monhoc_id,monhoc_ten,buoihoc.buoihoc_id,diemdanh_trangthai from sinhvien,diemdanh,`monhoc`,buoihoc, monhocgiangvien where   diemdanh_trangthai like '%Vắng%' and buoihoc.monhoc_id=monhoc.monhoc_id and diemdanh.buoihoc_id=buoihoc.buoihoc_id and monhocgiangvien.monhoc_id=monhoc.monhoc_id and monhocgiangvien.giangvien_id=%s and sinhvien.sinhvien_id=diemdanh.sinhvien_id UNION ALL select sinhvien.sinhvien_id,sinhvien_ten,sinhvien.lop_id,buoihoc_ngay,monhoc.monhoc_id,monhoc_ten,buoihoc_id,'Không điểm danh' from sinhvien,buoihoc,monhocsinhvien,`monhoc`, monhocgiangvien where sinhvien.sinhvien_id=monhocsinhvien.sinhvien_id and monhocsinhvien.monhoc_id=`monhoc`.monhoc_id and `monhoc`.monhoc_id=buoihoc.monhoc_id and CONCAT(sinhvien.sinhvien_id,buoihoc_id) not in (select CONCAT(sinhvien_id,buoihoc_id) from diemdanh) and monhocgiangvien.monhoc_id=monhoc.monhoc_id and monhocgiangvien.giangvien_id=%s UNION ALL select sinhvien.sinhvien_id,sinhvien_ten,sinhvien.lop_id,buoihoc_ngay,monhoc.monhoc_id,monhoc_ten,diemdanh.buoihoc_id,diemdanh_trangthai from sinhvien,diemdanh,buoihoc,monhoc WHERE sinhvien.sinhvien_id=diemdanh.sinhvien_id AND diemdanh.buoihoc_id=buoihoc.buoihoc_id AND buoihoc.monhoc_id=monhoc.monhoc_id AND diemdanh.diemdanh_trangthai='Có mặt' AND buoihoc.giangvien_id=%s) AS T1 HAVING "
                                    "T1.buoihoc_id Like '"+str(self.selectlesson.get())+"' ORDER BY T1.sinhvien_id,T1.monhoc_id,T1.buoihoc_id ASC",(self.giangvien_id,self.giangvien_id,self.giangvien_id,self.giangvien_id,))
                    data=my_cursor.fetchall()
                    if(len(data)!=0):
                        self.NoAttTable.delete(*self.NoAttTable.get_children())
                        for i in data:
                            self.NoAttTable.insert("",END,values=i)
                            mydataNot.append(i)
                        messagebox.showinfo("Thông báo","Có "+str(len(data))+" bản ghi thỏa mãn điều kiện",parent=self.root)
                        conn.commit()
                    else:
                        self.NoAttTable.delete(*self.NoAttTable.get_children())
                        messagebox.showinfo("Thông báo", " Không có bản ghi nào thỏa mãn điều kiện",parent=self.root)
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Lỗi", f"Lý do:{str(es)}", parent=self.root)
                
                      
    def exportUnpresetCsv(self):
        try:
            if len(mydataNot)<1:
                messagebox.showerror("Không có dữ liệu","Không có dữ liệu để xuất file",parent=self.root)
                return  False

            with open('Thongke_CSV/DanhSachDiemDanh.csv',mode="w",newline="",encoding="utf-8") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                exp_write.writerow(('ID Sinh viên', 'Tên Sinh viên','Lớp', 'Ngày', 'ID Môn học', 'Môn học', 'ID Buổi học','Trạng thái'))
                for i in mydataNot:
                    exp_write.writerow(i)
                messagebox.showinfo("Xuất Dữ Liệu","Dữ liệu của bạn đã được xuất đến "+os.path.basename('Thongke_CSV/DanhSachDiemDanh.csv')+" thành công",parent=self.root)
        except Exception as es:
            messagebox.showerror("Lỗi", f"Lý do:{str(es)}", parent=self.root)
                 
    #===================Cou ATT=========================
    def fetch_Coudata(self):
            # global mydata
            mydataall.clear()            
            if(value_from_home=="0" or value_from_home==None):
                conn = mysql.connector.connect(host='localhost', user='root', password='',
                                            database='diemdanhsv', port='3306')
                my_cursor = conn.cursor()
                self.giangvien_id=0
                my_cursor.execute("SELECT T1.sinhvien_id,T1.sinhvien_ten,T1.lop_id,T1.monhoc_id,T1.monhoc_ten,COUNT(*) FROM (select sinhvien.sinhvien_id,sinhvien_ten,lop_id,monhoc.monhoc_id,monhoc.monhoc_ten from sinhvien,buoihoc,monhocsinhvien,`monhoc` where sinhvien.sinhvien_id=monhocsinhvien.sinhvien_id and monhocsinhvien.monhoc_id=`monhoc`.monhoc_id and	`monhoc`.monhoc_id=buoihoc.monhoc_id and CONCAT(sinhvien.sinhvien_id,buoihoc_id) not in (select CONCAT(sinhvien_id,buoihoc_id) from diemdanh )  UNION all select sinhvien.sinhvien_id,sinhvien_ten,lop_id,monhoc.monhoc_id,monhoc.monhoc_id from sinhvien, diemdanh,`monhoc`,buoihoc where diemdanh_trangthai like '%Vắng%' and buoihoc.monhoc_id=monhoc.monhoc_id and diemdanh.buoihoc_id=buoihoc.buoihoc_id AND diemdanh.sinhvien_id=sinhvien.sinhvien_id) AS T1 GROUP BY T1.sinhvien_id,T1.monhoc_id")
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.CouAttTable.delete(*self.CouAttTable.get_children())
                    for i in data:
                        self.CouAttTable.insert("", END, values=i)
                        mydataall.append(i)
                    conn.commit()
                conn.close()
            else:
                conn = mysql.connector.connect(host='localhost', user='root', password='',
                                            database='diemdanhsv', port='3306')
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT T1.sinhvien_id,T1.sinhvien_ten,T1.lop_id,T1.monhoc_id,T1.monhoc_ten,COUNT(*) FROM (select sinhvien.sinhvien_id,sinhvien_ten,lop_id,monhoc.monhoc_id,monhoc.monhoc_ten from sinhvien,buoihoc,monhocsinhvien,`monhoc`, monhocgiangvien where sinhvien.sinhvien_id=monhocsinhvien.sinhvien_id and monhocsinhvien.monhoc_id=`monhoc`.monhoc_id and `monhoc`.monhoc_id=buoihoc.monhoc_id and CONCAT(sinhvien.sinhvien_id,buoihoc_id) not in (select CONCAT(sinhvien_id,buoihoc_id) from diemdanh ) and monhocgiangvien.monhoc_id=monhoc.monhoc_id and monhocgiangvien.giangvien_id=%s   UNION all select sinhvien.sinhvien_id,sinhvien.sinhvien_id,sinhvien.lop_id,monhoc.monhoc_id,monhoc.monhoc_ten from sinhvien, diemdanh,`monhoc`,buoihoc,monhocgiangvien where diemdanh_trangthai like '%Vắng%' and buoihoc.monhoc_id=monhoc.monhoc_id and diemdanh.buoihoc_id=buoihoc.buoihoc_id AND diemdanh.sinhvien_id=sinhvien.sinhvien_id and monhocgiangvien.monhoc_id=monhoc.monhoc_id and monhocgiangvien.giangvien_id=%s ) AS T1 GROUP BY T1.sinhvien_id,T1.monhoc_id",(self.giangvien_id,self.giangvien_id,))
                data = my_cursor.fetchall()
                if len(data) != 0:
                    self.CouAttTable.delete(*self.CouAttTable.get_children())
                    for i in data:
                        self.CouAttTable.insert("", END, values=i)
                        mydataall.append(i)
                    conn.commit()
                conn.close()
                             
    def search_Coudata(self):
        if(value_from_home=="0" or value_from_home==None):
            if  self.var_com_searchcouatt.get()=="":
                messagebox.showerror("Lỗi !","Vui lòng nhập thông tin đầy đủ",parent=self.root)

            else:
                try:
                    conn = mysql.connector.connect(host='localhost', user='root', password='',
                                                database='diemdanhsv', port='3306')
                    my_cursor = conn.cursor()
                    my_cursor.execute("SELECT T1.sinhvien_id,T1.sinhvien_ten,T1.lop_id,T1.monhoc_id,T1.monhoc_ten,COUNT(*) FROM (select sinhvien.sinhvien_id,sinhvien_ten,lop_id,monhoc.monhoc_id,monhoc.monhoc_ten from sinhvien,buoihoc,monhocsinhvien,`monhoc` where sinhvien.sinhvien_id=monhocsinhvien.sinhvien_id and monhocsinhvien.monhoc_id=`monhoc`.monhoc_id and `monhoc`.monhoc_id=buoihoc.monhoc_id and CONCAT(sinhvien.sinhvien_id,buoihoc_id) not in (select CONCAT(sinhvien_id,buoihoc_id) from diemdanh )  UNION all select sinhvien.sinhvien_id,sinhvien_ten,lop_id,monhoc.monhoc_id,monhoc.monhoc_ten from sinhvien, diemdanh,`monhoc`,buoihoc where diemdanh_trangthai like '%Vắng%' and buoihoc.monhoc_id=monhoc.monhoc_id and diemdanh.buoihoc_id=buoihoc.buoihoc_id AND diemdanh.sinhvien_id=sinhvien.sinhvien_id) AS T1 GROUP BY T1.sinhvien_id,T1.monhoc_id having T1.monhoc_id=%s",(self.subid_couatt,))
                    data=my_cursor.fetchall()
                    if(len(data)!=0):
                        self.CouAttTable.delete(*self.CouAttTable.get_children())
                        for i in data:
                            self.CouAttTable.insert("",END,values=i)
                            mydataall.append(i)
                        messagebox.showinfo("Thông báo","Có "+str(len(data))+" bản ghi thỏa mãn điều kiện",parent=self.root)
                        conn.commit()
                    else:
                        self.CouAttTable.delete(*self.CouAttTable.get_children())
                        messagebox.showinfo("Thông báo", " Không có bản ghi nào thỏa mãn điều kiện",parent=self.root)
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Lỗi", f"Lý do:{str(es)}", parent=self.root)
                    
        else:
            
            if self.var_com_searchcouatt.get()=="":
                messagebox.showerror("Lỗi !","Vui lòng nhập thông tin đầy đủ",parent=self.root)

            else:
                try:
                    conn = mysql.connector.connect(host='localhost', user='root', password='',
                                                database='diemdanhsv', port='3306')
                    my_cursor = conn.cursor()#"ID Điểm Danh", "Ngày", "ID Sinh viên"
                    mydataall.clear()
                    my_cursor.execute("SELECT T1.sinhvien_id,T1.sinhvien_ten,T1.lop_id,T1.monhoc_id,T1.monhoc_ten,COUNT(*) FROM (select sinhvien.sinhvien_id,sinhvien_ten,lop_id,monhoc.monhoc_id,monhoc.monhoc_ten from sinhvien,buoihoc,monhocsinhvien,`monhoc` where sinhvien.sinhvien_id=monhocsinhvien.sinhvien_id and monhocsinhvien.monhoc_id=`monhoc`.monhoc_id and `monhoc`.monhoc_id=buoihoc.monhoc_id and giangvien_id=%s and CONCAT(sinhvien.sinhvien_id,buoihoc_id) not in (select CONCAT(sinhvien_id,buoihoc_id) from diemdanh )  UNION all select sinhvien.sinhvien_id,sinhvien_ten,lop_id,monhoc.monhoc_id,monhoc.monhoc_ten from sinhvien, diemdanh,`monhoc`,buoihoc where diemdanh_trangthai like '%Vắng%' and buoihoc.monhoc_id=monhoc.monhoc_id and diemdanh.buoihoc_id=buoihoc.buoihoc_id AND diemdanh.sinhvien_id=sinhvien.sinhvien_id and giangvien_id=%s) AS T1 GROUP BY T1.sinhvien_id,T1.monhoc_id having "
                                    "T1.monhoc_id =%s",(self.giangvien_id,self.giangvien_id,self.subid_couatt,))
                    data=my_cursor.fetchall()
                    if(len(data)!=0):
                        self.CouAttTable.delete(*self.CouAttTable.get_children())
                        for i in data:
                            self.CouAttTable.insert("",END,values=i)
                            mydataall.append(i)
                        messagebox.showinfo("Thông báo","Có "+str(len(data))+" bản ghi thỏa mãn điều kiện",parent=self.root)
                        conn.commit()
                    else:
                        self.CouAttTable.delete(*self.CouAttTable.get_children())
                        messagebox.showinfo("Thông báo", " Không có bản ghi nào thỏa mãn điều kiện",parent=self.root)
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Lỗi", f"Lý do:{str(es)}", parent=self.root)
          
    def exportCsvcouall(self):
        try:
            if len(mydataall)<1:
                messagebox.showerror("Không có dữ liệu","Không có dữ liệu để xuất file",parent=self.root)
                return  False

            with open('Thongke_CSV/tonglanvang.csv',mode="w",newline="",encoding="utf-8") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                exp_write.writerow(('ID Sinh viên', 'Tên Sinh viên','Lớp',  'ID Môn học', 'Số lần vắng'))
                for i in mydataall:
                    exp_write.writerow(i)
                messagebox.showinfo("Xuất Dữ Liệu","Dữ liệu của bạn đã được xuất đến "+os.path.basename('Thongke_CSV/tonglanvang.csv')+" thành công",parent=self.root)
        except Exception as es:
            messagebox.showerror("Lỗi", f"Lý do:{str(es)}", parent=self.root)

    def exportList(self):
        listdata.clear()         
        if(value_from_home=="0" or value_from_home==None):
            conn = mysql.connector.connect(host='localhost', user='root', password='',
                                            database='diemdanhsv', port='3306')
            my_cursor = conn.cursor()
            self.giangvien_id=0
            my_cursor.execute("select sinhvien.sinhvien_id,sinhvien.sinhvien_ten,sinhvien.lop_id,monhocsinhvien.monhoc_id,monhoc.monhoc_ten from `monhoc`, monhocsinhvien,sinhvien where sinhvien.sinhvien_id=monhocsinhvien.sinhvien_id and monhocsinhvien.monhoc_id=monhoc.monhoc_id and monhoc.monhoc_id=%s" ,(self.monhoc_id,))
            subject_ls = my_cursor.fetchall()
            if len(subject_ls) != 0:
                for i in subject_ls:
                        listdata.append(i)
                conn.commit()
            conn.close()                
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='',
                                            database='diemdanhsv', port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("select sinhvien.sinhvien_id,sinhvien.sinhvien_ten,sinhvien.lop_id,monhocsinhvien.monhoc_id,monhoc.monhoc_ten from `monhoc`, monhocgiangvien, sinhvien, monhocsinhvien where sinhvien.sinhvien_id=monhocsinhvien.sinhvien_id and monhocsinhvien.monhoc_id=monhoc.monhoc_id and monhocgiangvien.monhoc_id=monhoc.monhoc_id and monhocgiangvien.giangvien_id=%s and monhoc.monhoc_id=%s" ,(self.giangvien_id, self.monhoc_id,))
            subject_ls = my_cursor.fetchall()
            if len(subject_ls) != 0:
                for i in subject_ls:
                    listdata.append(i)
                conn.commit()
            conn.close()
        
        try:
            if len(listdata)<1:
                messagebox.showerror("Không có dữ liệu","Không có dữ liệu để xuất file",parent=self.root)
                return  False

            with open('Thongke_CSV/DanhSachSinhVien.csv',mode="w",newline="",encoding="utf-8") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                exp_write.writerow(('ID Sinh viên', 'Tên Sinh viên','Lớp', 'ID Môn học', 'Môn học'))
                for i in listdata:
                    exp_write.writerow(i)
                messagebox.showinfo("Xuất Dữ Liệu","Dữ liệu của bạn đã được xuất đến "+os.path.basename('Thongke_CSV/DanhSachSinhVien.csv')+" thành công",parent=self.root)
        except Exception as es:
            messagebox.showerror("Lỗi", f"Lý do:{str(es)}", parent=self.root)


if __name__=="__main__":
    root=Tk() #khoi tao cua so va gan root vao
    obj=report(root)
    root.mainloop()# cua so hien len
    
    