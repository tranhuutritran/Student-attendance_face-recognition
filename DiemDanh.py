import os
from tkinter import *
from tkinter import ttk
import PIL.Image
import PIL.ImageTk
from tkinter import messagebox
import mysql.connector
import numpy as np
from PIL import Image, ImageTk
import cv2
from datetime import datetime
from time import strftime
import csv

mydata=[]
class Attendance:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.state('zoomed')
        self.root.configure(bg='#7fe5ea')
        self.root.title("Hệ thống điểm danh (Khoa Phát triển Nông thôn - Đại học Cần Thơ)")
        self.isClicked=False
        today = strftime("%Y-%m-%d")


        #===========variables=========
        self.var_atten_id=StringVar()
        self.var_atten_class = StringVar()
        self.var_atten_idsv = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_timein = StringVar()
        self.var_atten_timeout = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()
        self.var_atten_lesson=StringVar()

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
        self.txt = "QUẢN LÝ THÔNG TIN ĐIỂM DANH"
        self.count = 0
        self.text = ''
        self.heading = Label(self.root, text=self.txt, font=("times new roman", 20, "bold"), bg="#7fe5ea", fg="#0000CC",
                             bd=5, relief=FLAT)
        self.heading.place(x=400, y=30, width=650)

        main_frame = Frame(bg_img, bd=2, bg="#7fe5ea")
        main_frame.place(x=23, y=102, width=1482, height=671)


        # left_label
        Left_frame = LabelFrame(main_frame, bd=2, bg="#6EC3C9", relief=RIDGE,
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=20, y=5, width=400, height=580)

        label_Update_att=Label(Left_frame,bg="#6EC3C9",fg="#990000",text="CẬP NHẬT ĐIỂM DANH",font=("times new roman", 14, "bold"))
        label_Update_att.place(x=0, y=1, width=395, height=35)

        left_inside_frame = Frame(Left_frame, bd=1, bg="#6EC3C9")
        left_inside_frame.place(x=0, y=60, width=380, height=500)

        #auttenID
        auttendanceID_label = Label(left_inside_frame, text="ID Điểm Danh:", font=("times new roman", 12, "bold"),
                                bg="#6EC3C9")
        auttendanceID_label.grid(row=0, column=0, padx=20, pady=5, sticky=W)

        auttendanceID_entry = ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,
                                    font=("times new roman", 12, "bold"),state="readonly")
        auttendanceID_entry.grid(row=0, column=1, padx=20, pady=5, sticky=W)


        #idstudent
        roll_label = Label(left_inside_frame, text="ID Sinh viên:", font=("times new roman", 12, "bold"),
                                    bg="#6EC3C9")
        roll_label.grid(row=1, column=0, padx=20, pady=5, sticky=W)

        roll_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_idsv,
                                        font=("times new roman", 12, "bold"),state="readonly")
        roll_entry.grid(row=1, column=1, padx=20, pady=5, sticky=W)



        #name
        nameLabel = Label(left_inside_frame, text="Tên Sinh viên:", font=("times new roman", 12, "bold"),
                                    bg="#6EC3C9")
        nameLabel.grid(row=2, column=0, padx=20, pady=5, sticky=W)

        nameLabel_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_name,
                                        font=("times new roman", 12, "bold"),state="readonly")
        nameLabel_entry.grid(row=2, column=1, padx=20, pady=5, sticky=W)


        #class
        classLabel = Label(left_inside_frame, text="Lớp học:", font=("times new roman", 12, "bold"),
                                    bg="#6EC3C9")
        classLabel.grid(row=3, column=0, padx=20, pady=5, sticky=W)

        classLabel_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_class,
                                        font=("times new roman", 12, "bold"),state="readonly")
        classLabel_entry.grid(row=3, column=1, padx=20, pady=5, sticky=W)

        #time_in
        timeLabel = Label(left_inside_frame, text="Giờ vào:", font=("times new roman", 12, "bold"),
                                    bg="#6EC3C9")
        timeLabel.grid(row=4, column=0, padx=20, pady=5, sticky=W)

        timeLabel_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_timein,
                                        font=("times new roman", 12, "bold"))
        timeLabel_entry.grid(row=4, column=1, padx=20, pady=5, sticky=W)

        # time_out
        timeoutLabel = Label(left_inside_frame, text="Giờ ra:", font=("times new roman", 12, "bold"),
                          bg="#6EC3C9")
        timeoutLabel.grid(row=5, column=0, padx=20, pady=5, sticky=W)

        timeoutLabel_entry = ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_timeout,
                                    font=("times new roman", 12, "bold"))
        timeoutLabel_entry.grid(row=5, column=1, padx=20, pady=5, sticky=W)

        #date
        dateLabel = Label(left_inside_frame, text="Ngày:", font=("times new roman", 12, "bold"),
                          bg="#6EC3C9")
        dateLabel.grid(row=6, column=0, padx=20, pady=5, sticky=W)

        dateLabel_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_date,
                                    font=("times new roman", 12, "bold"),state="readonly")
        dateLabel_entry.grid(row=6, column=1, padx=20, pady=5, sticky=W)

        #auttendance
        auttendanceLabel = Label(left_inside_frame, text="Điểm danh:", font=("times new roman", 12, "bold"),
                           bg="#6EC3C9")
        auttendanceLabel.grid(row=7, column=0,  padx=20, pady=5, sticky=W)

        self.atten_status=ttk.Entry(left_inside_frame    ,width=20,font=("times new roman", 12, "bold"),textvariable=self.var_atten_attendance)

        self.atten_status.grid(row=7,column=1,pady=5,padx=20)


        #lesson
        lessonLabel = Label(left_inside_frame, text="ID Buổi học:", font=("times new roman", 12, "bold"),
                                 bg="#6EC3C9")
        lessonLabel.grid(row=8, column=0, padx=20, pady=5, sticky=W)

        self.lesson = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 12, "bold"),
                                         state="readonly", textvariable=self.var_atten_lesson)
        self.lesson.grid(row=8, column=1, pady=5, padx=20)


        # btn_frame
        label_Update_att = Button(Left_frame, bg="#3300FF", fg="white", text="Xem ảnh",command=self.openImage,
                                 font=("times new roman", 12, "bold"))
        label_Update_att.place(x=100, y=490, width=200, height=30)
        update_btn = Button(Left_frame, text="Xóa", command=self.delete_data,
                            font=("times new roman", 12, "bold"),
                            bg="#FF0000", fg="white", width=250)
        update_btn.place(x=100, y=540,width=200,height=30 )

        update_btn = Button(Left_frame, text="Xuất file CSV",command=self.exportCsv, font=("times new roman", 11, "bold"),
                            bg="#3300FF", fg="white", width=250)
        update_btn.place(x=100, y=440,width=200,height=30)


        btn_frame = Frame(left_inside_frame, bg="#6EC3C9")
        btn_frame.place(x=40, y=320, width=400, height=105)
        
        delete_btn = Button(btn_frame, text="Cập nhật",command=self.update_data ,font=("times new roman", 11, "bold"),
                            bg="#3300FF", fg="white", width=16)
        delete_btn.grid(row=9, column=0,pady=10)

        reset_btn = Button(btn_frame, text="Làm mới",command=self.reset_data, font=("times new roman", 11, "bold"),
                           bg="#3300FF", fg="white", width=16)
        reset_btn.grid(row=9, column=1,pady=10)




        #right_ label
        Right_frame = LabelFrame(main_frame, bd=2, bg="#6EC3C9",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=430, y=5, width=880, height=580)


        #search
        self.var_com_search=StringVar()
        search_label = Label(Right_frame, text="Tìm kiếm theo :", font=("times new roman", 11, "bold"),
                             bg="#6EC3C9")
        search_label.grid(row=0, column=0, padx=15, pady=5, sticky=W)

        search_combo = ttk.Combobox(Right_frame, font=("times new roman", 11, "bold"),textvariable=self.var_com_search, state="read only",
                                    width=13)
        search_combo["values"] = ("ID Điểm Danh", "Ngày", "ID Sinh viên","ID Buổi học")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=15, sticky=W)

        self.var_search=StringVar()
        search_entry = ttk.Entry(Right_frame,textvariable=self.var_search, width=15, font=("times new roman", 11, "bold"))
        search_entry.grid(row=0, column=2, padx=15, pady=5, sticky=W)

        search_btn = Button(Right_frame,command=self.search_data, text="Tìm kiếm", font=("times new roman", 11, "bold"), bg="#fbd568", fg="#945305",
                            width=12)
        search_btn.grid(row=0, column=3, padx=15)

        Today_btn = Button(Right_frame, text="Hôm nay",command=self.today_data, font=("times new roman", 11, "bold"), bg="#fbd568",
                             fg="#945305",
                             width=12)
        Today_btn.grid(row=0, column=4, padx=15)


        showAll_btn = Button(Right_frame, text="Xem tất cả", command=self.fetch_data,font=("times new roman", 11, "bold"), bg="#fbd568",
                             fg="#945305",
                             width=12)
        showAll_btn.grid(row=0, column=5, padx=15)


        #table_frame
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=55, width=860, height=510)

        #scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","idsv","name","class","time_in","time_out","date","lesson","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="AttendanceID")
        self.AttendanceReportTable.heading("idsv", text="ID Sinh viên")
        self.AttendanceReportTable.heading("name", text="Tên Sinh viên")
        self.AttendanceReportTable.heading("class", text="Lớp học")
        self.AttendanceReportTable.heading("time_in", text="Giờ vào")
        self.AttendanceReportTable.heading("time_out", text="Giờ ra")
        self.AttendanceReportTable.heading("date", text="Ngày")
        self.AttendanceReportTable.heading("attendance", text="Điểm danh")
        self.AttendanceReportTable.heading("lesson", text="ID Buổi học")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100, anchor=CENTER)
        self.AttendanceReportTable.column("idsv", width=100, anchor=CENTER)
        self.AttendanceReportTable.column("name", width=130)
        self.AttendanceReportTable.column("class", width=100,anchor=CENTER)
        self.AttendanceReportTable.column("time_in", width=100, anchor=CENTER)
        self.AttendanceReportTable.column("time_out", width=100, anchor=CENTER)
        self.AttendanceReportTable.column("date", width=100, anchor=CENTER)
        self.AttendanceReportTable.column("attendance", width=100, anchor=CENTER)
        self.AttendanceReportTable.column("lesson", width=100, anchor=CENTER)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()  # load du lieu len grid
        #================fetchData======================

        # =======================fetch-data========================
    def fetch_data(self):
            # global mydata
            mydata.clear()
            conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                           port='3306')

            my_cursor = conn.cursor()
            my_cursor.execute("Select diemdanh_id,sinhvien.sinhvien_id, sinhvien.sinhvien_ten,sinhvien.lop_id,diemdanh_giovao,diemdanh_giora,diemdanh_ngay,buoihoc_id,diemdanh_trangthai from diemdanh, sinhvien where sinhvien.sinhvien_id=diemdanh.sinhvien_id")
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                for i in data:

                    self.AttendanceReportTable.insert("", END, values=i)
                    mydata.append(i)
                conn.commit()
                self.var_com_search.set("ID Điểm Danh")
                self.var_search.set("")
            conn.close()
    #update du lieu chuan hoa tren bang?:
    def update(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())

    #export csv
    def exportCsv(self):
        # try:
            if len(mydata)<1:
                messagebox.showerror("Không có dữ liệu","Không có dữ liệu để xuất file",parent=self.root)
                return  False

            with open('Thongke_CSV/DiemDanh.csv',mode="w",newline="",encoding="utf-8") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                exp_write.writerow(('Mã Điểm danh', 'ID Sinh viên', 'Tên Sinh viên', 'Lớp biên chế', 'Giờ vào', 'Giờ ra', 'Ngày', 'ID Buổi học', 'Trạng thái'))
                for i in mydata:
                    exp_write.writerow(i)

                messagebox.showinfo("Xuất Dữ Liệu","Dữ liệu của bạn đã được xuất đến "+os.path.basename('DiemDanh.csv')+" thành công",parent=self.root)
        # except Exception as es:
        #     messagebox.showerror("Lỗi", f"Lý do:{str(es)}", parent=self.root)


    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_idsv.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_class.set(rows[3])
        self.var_atten_timein.set(rows[4])
        self.var_atten_timeout.set(rows[5])
        self.var_atten_date.set(rows[6])
        self.var_atten_attendance.set(rows[8])
        self.var_atten_lesson.set(rows[7])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_idsv.set("")
        self.var_atten_name.set("")
        self.var_atten_class.set("")
        self.var_atten_timein.set("")
        self.var_atten_timeout.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        self.var_atten_lesson.set("")
    def update_data(self):
        if self.var_atten_lesson.get()=="Lesson" or self.var_atten_attendance.get()=="Status" or self.var_atten_id.get()=="":
            messagebox.showerror("Error","Vui lòng nhập đầy đủ thông tin",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Bạn có muốn cập nhật bản ghi này không?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv', port='3306')
                    my_cursor = conn.cursor()
                    my_cursor.execute("update diemdanh set sinhvien_id=%s, diemdanh_giovao=%s,diemdanh_giora=%s,diemdanh_ngay=%s,diemdanh_trangthai=%s,"
                                      "buoihoc_id=%s where diemdanh_id=%s",(
                                            self.var_atten_idsv.get(),
                                            self.var_atten_timein.get(),
                                            self.var_atten_timeout.get(),
                                            self.var_atten_date.get(),
                                            self.var_atten_attendance.get(),
                                            self.var_atten_lesson.get(),

                                            self.var_atten_id.get()
                                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Thành công","Cập nhật thông tin điểm danh thành công",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Lỗi",f"Lý do:{str(es)}",parent=self.root)

    # Delete Function
    def delete_data(self):
            if self.var_atten_id.get() == "":
                messagebox.showerror("Lỗi", "Không được bỏ trống ID ", parent=self.root)
            else:
                try:
                    delete = messagebox.askyesno("Xoá bản ghi", "Bạn có muốn xóa bản ghi này ?", parent=self.root)
                    if delete > 0:
                        conn = mysql.connector.connect(host='localhost', user='root', password='',
                                                       database='diemdanhsv', port='3306')
                        my_cursor = conn.cursor()
                        sql = "delete from diemdanh where diemdanh_id=%s"
                        val = (self.var_atten_id.get(),)
                        my_cursor.execute(sql, val)
                    else:
                        if not delete:
                            return
                    conn.commit()
                    # self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Xóa", "Xóa bản ghi thành công", parent=self.root)
                    self.fetch_data()
                except Exception as es:
                    messagebox.showerror("Lỗi", f"Lý do:{str(es)}", parent=self.root)
    def openImage(self):
        if self.var_atten_id == "":
            messagebox.showerror("Lỗi", " Vui lòng chọn ID để xem ảnh", parent=self.root)


        elif(self.var_atten_timein.get()=='None' ):
            if not os.path.exists("DiemDanhImage\ " + self.var_atten_id.get() +"Ra" +".jpg"):
                messagebox.showerror("Lỗi", "Không tìm thấy ảnh điểm danh", parent=self.root)
            else:
                img = cv2.imread("DiemDanhImage\ " + str(self.var_atten_id.get()) +"Ra"+ ".jpg")
                img = cv2.resize(img, (300, 300))
                cv2.imshow("Out of Class", img)
        elif(self.var_atten_timeout.get()=='None'):
            if not os.path.exists("DiemDanhImage\ " + self.var_atten_id.get() + ".jpg"):
                messagebox.showerror("Lỗi", "Không tìm thấy ảnh điểm danh", parent=self.root)
            else:
                img1=cv2.imread("DiemDanhImage\ " + str(self.var_atten_id.get()) + ".jpg")
                img1=cv2.resize(img1,(300,300))
                cv2.imshow("Into Class",img1)
        elif(self.var_atten_timein.get()!='None' and self.var_atten_timeout.get()!='None'):
            img = cv2.imread("DiemDanhImage\ " + str(self.var_atten_id.get()) + "Ra" + ".jpg")
            img = cv2.resize(img, (300, 300))
            img1 = cv2.imread("DiemDanhImage\ " + str(self.var_atten_id.get()) + ".jpg")
            img1 = cv2.resize(img1, (300, 300))
            Hori = np.concatenate((img, img1), axis=1)
            cv2.imshow("InAndOutClass", Hori)
        else:
            messagebox.showerror("Lỗi", "Không tìm thấy ảnh điểm danh", parent=self.root)
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Lỗi !","Vui lòng nhập thông tin đầy đủ",parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password='',
                                               database='diemdanhsv', port='3306')
                my_cursor = conn.cursor()#"ID Điểm Danh", "Ngày", "ID Sinh viên"
                if(self.var_com_search.get()=="ID Điểm Danh"):
                    self.var_com_search.set("diemdanh_id")
                elif(self.var_com_search.get()=="Ngày"):
                    self.var_com_search.set("diemdanh_ngay")
                else:
                    if(self.var_com_search.get()=="ID Sinh viên"):
                        self.var_com_search.set("diemdanh.sinhvien_id")
                    elif(self.var_com_search.get()=="ID Buổi học"):
                        self.var_com_search.set("buoihoc_id")
                mydata.clear()
                my_cursor.execute("Select diemdanh_id,sinhvien.sinhvien_id, sinhvien.sinhvien_ten,sinhvien.lop_id,diemdanh_giovao,diemdanh_giora,diemdanh_ngay,buoihoc_id,diemdanh_trangthai from diemdanh, sinhvien where sinhvien.sinhvien_id=diemdanh.sinhvien_id and "+str(self.var_com_search.get())+" Like '%"+str(self.var_search.get())+"%'")
                data=my_cursor.fetchall()
                if(len(data)!=0):

                    self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                    for i in data:
                        self.AttendanceReportTable.insert("",END,values=i)
                        mydata.append(i)
                    messagebox.showinfo("Thông báo","Có "+str(len(data))+" bản ghi thỏa mãn điều kiện",parent=self.root)
                    conn.commit()
                else:
                    self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                    messagebox.showinfo("Thông báo", " Không có bản ghi nào thỏa mãn điều kiện",parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showerror("Lỗi", f"Lý do:{str(es)}", parent=self.root)
    def today_data(self):
        try:
            conn = mysql.connector.connect(host='localhost', user='root', password='',
                                           database='diemdanhsv', port='3306')
            my_cursor = conn.cursor()  # "ID Điểm Danh", "Ngày", "ID Sinh viên"
            mydata.clear()
            d1 = strftime("%Y-%m-%d")
            my_cursor.execute("Select diemdanh_id,sinhvien.sinhvien_id, sinhvien.sinhvien_ten,sinhvien.lop_id,diemdanh_giovao,diemdanh_giora,diemdanh_ngay,buoihoc_id,diemdanh_trangthai from diemdanh, sinhvien where sinhvien.sinhvien_id=diemdanh.sinhvien_id and diemdanh_ngay Like '%" + str(
                d1) + "%'")
            data = my_cursor.fetchall()
            if (len(data) != 0):

                self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                for i in data:
                    self.AttendanceReportTable.insert("", END, values=i)
                    mydata.append(i)
                messagebox.showinfo("Thông báo", "Có " + str(len(data)) + " bản ghi hôm nay",parent=self.root)
                conn.commit()
            else:
                self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                messagebox.showinfo("Thông báo", " Không có bản ghi nào trong hôm nay !",parent=self.root)
            conn.close()
        except Exception as es:
            messagebox.showerror("Lỗi", f"Lý do:{str(es)}", parent=self.root)

if __name__=="__main__":
    root=Tk() #khoi tao cua so va gan root vao
    obj=Attendance(root)
    root.mainloop()# cua so hien len