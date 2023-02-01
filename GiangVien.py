from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
import PIL.Image
from time import strftime
from math import *
from tkinter import messagebox
import mysql.connector
mydata=[]
class Teacher:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.state('zoomed')
        self.root.configure(bg='#7fe5ea')
        self.root.title("Hệ thống điểm danh (Khoa Phát triển Nông thôn - Đại học Cần Thơ)")
        today = strftime("%Y-%m-%d")

        # ================variable===================
        self.var_name = StringVar()
        self.var_id = StringVar()
        self.var_phone = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

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
        self.txt = "QUẢN LÝ THÔNG TIN GIẢNG VIÊN"
        self.count = 0
        self.text = ''
        self.heading = Label(self.root, text=self.txt, font=("times new roman", 20, "bold"), bg="#7fe5ea", fg="#0000CC",
                             bd=5, relief=FLAT)
        self.heading.place(x=400, y=30, width=650)

        main_frame = Frame(bg_img, bd=2, bg="#7fe5ea")
        main_frame.place(x=23, y=102, width=1482, height=671)


        # ===================left_label=====================
        Left_frame = LabelFrame(main_frame, bd=2, bg="#6EC3C9", relief=RIDGE,
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=20, y=5, width=400, height=580)

        label_Update_att = Label(Left_frame, bg="#6EC3C9", fg="#990000", text="THÔNG TIN GIẢNG VIÊN",
                                 font=("times new roman", 14, "bold"))
        label_Update_att.place(x=0, y=1, width=395, height=35)

        left_inside_frame = Frame(Left_frame, bd=1, bg="#6EC3C9")
        left_inside_frame.place(x=0, y=60, width=380, height=500)

        # idgv
        auttendanceID_label = Label(left_inside_frame, text="ID Giảng viên:",font=("times new roman", 12, "bold"),
                                    bg="#6EC3C9")
        auttendanceID_label.grid(row=0, column=0, padx=20, pady=10, sticky=W)

        auttendanceID_entry = ttk.Entry(left_inside_frame, textvariable=self.var_id,
                                        font=("times new roman", 12, "bold"),width=22)
        auttendanceID_entry.grid(row=0, column=1, padx=20, pady=10, sticky=W)

        # namegv
        roll_label = Label(left_inside_frame, text="Họ tên:", font=("times new roman", 12, "bold"),
                           bg="#6EC3C9")
        roll_label.grid(row=1, column=0, padx=20, pady=10, sticky=W)

        roll_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_name,
                               font=("times new roman", 12, "bold"))
        roll_entry.grid(row=1, column=1, padx=20, pady=10, sticky=W)

        # sđt_gv
        nameLabel = Label(left_inside_frame, text="SĐT:", font=("times new roman", 12, "bold"),
                          bg="#6EC3C9")
        nameLabel.grid(row=2, column=0, padx=20, pady=10, sticky=W)

        nameLabel_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_phone,
                                    font=("times new roman", 12, "bold"))
        nameLabel_entry.grid(row=2, column=1, padx=20, pady=10, sticky=W)

        # email
        classLabel = Label(left_inside_frame, text="Email:", font=("times new roman", 12, "bold"),
                           bg="#6EC3C9")
        classLabel.grid(row=3, column=0, padx=20, pady=10, sticky=W)

        classLabel_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_email,
                                     font=("times new roman", 12, "bold"))
        classLabel_entry.grid(row=3, column=1, padx=20, pady=10, sticky=W)

        # Q
        timeLabel = Label(left_inside_frame, text="Câu hỏi bảo mật:", font=("times new roman", 12, "bold"),
                          bg="#6EC3C9")
        timeLabel.grid(row=4, column=0, padx=20, pady=10, sticky=W)

        timeLabel_entry = ttk.Combobox(left_inside_frame, width=20, textvariable=self.var_securityQ,
                                    font=("times new roman", 12, "bold"),state='read-only')
        timeLabel_entry["values"] = ("Select", "Bạn thích ăn gì", "Sở thích của bạn", "Chữ số bạn thích")
        timeLabel_entry.grid(row=4, column=1, padx=20, pady=10, sticky=W)
        timeLabel_entry.current(0)

        # A
        dateLabel = Label(left_inside_frame, text="Câu trả lời:", font=("times new roman", 12, "bold"),
                          bg="#6EC3C9")
        dateLabel.grid(row=5, column=0, padx=20, pady=10, sticky=W)

        dateLabel_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_securityA,
                                    font=("times new roman", 12, "bold"))
        dateLabel_entry.grid(row=5, column=1, padx=20, pady=10, sticky=W)

        # pass
        passLabel = Label(left_inside_frame, text="Password:", font=("times new roman", 12, "bold"),
                                 bg="#6EC3C9")
        passLabel.grid(row=6, column=0, padx=20, pady=5, sticky=W)

        passLabel_entry = ttk.Entry(left_inside_frame, width=22, textvariable=self.var_pass,
                                    font=("times new roman", 12, "bold"))
        passLabel_entry.grid(row=6, column=1, padx=20, pady=5, sticky=W)


        # =====btn_frame============

        btn_frame = Frame(left_inside_frame, bg="#6EC3C9")
        btn_frame.place(x=0, y=350, width=440, height=115)

        add_btn = Button(btn_frame, text="Thêm mới", command=self.add_data, font=("times new roman", 11, "bold"),
                            bg="#3300FF", fg="white", width=17)
        add_btn.grid(row=9, column=0, pady=10,padx=15)

        delete_btn = Button(btn_frame, text="Xóa", command=self.delete_data,
                            font=("times new roman", 11, "bold"),
                            bg="#FF0000", fg="white", width=17)
        delete_btn.grid(row=10, column=1, pady=10,padx=15)

        update_btn = Button(btn_frame, text="Cập nhật", command=self.update_data, font=("times new roman", 11, "bold"),
                            bg="#3300FF", fg="white", width=17)
        update_btn.grid(row=9, column=1, pady=20, padx=15)

        reset_btn = Button(btn_frame, text="Làm mới", command=self.reset_data, font=("times new roman", 11, "bold"),
                           bg="#3300FF", fg="white", width=17)
        reset_btn.grid(row=10, column=0, pady=0,padx=15)

        # ==================right_ label========================
        Right_frame = LabelFrame(main_frame, bd=2, bg="#6EC3C9",
                                 font=("times new roman", 12, "bold"))
        Right_frame.place(x=430, y=5, width=880, height=580)

        # search
        self.var_com_search = StringVar()
        search_label = Label(Right_frame, text="Tìm kiếm theo :", font=("times new roman", 11, "bold"),
                             bg="#6EC3C9")
        search_label.grid(row=0, column=0, padx=15, pady=5, sticky=W)

        search_combo = ttk.Combobox(Right_frame, font=("times new roman", 11, "bold"), textvariable=self.var_com_search,
                                    state="read only",
                                    width=13)
        search_combo["values"] = ("ID GV", "Tên GV", "SĐT")
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
        table_frame.place(x=5, y=55, width=860, height=510)

        # scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=(
        "id", "name", "phone", "email", "quest", "answer", "pass"),
                                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="ID Giảng viên")

        self.AttendanceReportTable.heading("name", text="Tên Giảng viên")
        self.AttendanceReportTable.heading("phone", text="SĐT")
        self.AttendanceReportTable.heading("email", text="Email")
        self.AttendanceReportTable.heading("quest", text="Câu hỏi bảo mật")
        self.AttendanceReportTable.heading("answer", text="Trả lời")
        self.AttendanceReportTable.heading("pass", text="Password")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width=80, anchor=CENTER)
        self.AttendanceReportTable.column("name", width=120)
        self.AttendanceReportTable.column("phone", width=80,anchor=CENTER)
        self.AttendanceReportTable.column("email", width=140)
        self.AttendanceReportTable.column("quest", width=150, anchor=CENTER)
        self.AttendanceReportTable.column("answer", width=150, anchor=CENTER)
        self.AttendanceReportTable.column("pass", width=90, anchor=CENTER)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()  # load du lieu len grid

    #=========================================Function============================================
    #===================================================================================================        
    # ================fetchData======================
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_id.set(rows[0])
        self.var_name.set(rows[1])
        self.var_phone.set(rows[2])
        self.var_email.set(rows[3])
        self.var_securityQ.set(rows[4])
        self.var_securityA.set(rows[5])
        self.var_pass.set(rows[6])

    # ================add_data======================
    def add_data(self):
        if self.var_securityQ.get()=="Select" or self.var_id.get()=="" or self.var_name.get()=="":
            messagebox.showerror("Error","Vui lòng nhập đầy đủ thông tin",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv', port='3306')

                my_cursor=conn.cursor()
                my_cursor.execute("insert into giangvien values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_phone.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get(),

                ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                messagebox.showinfo("Thành công","Thêm thông tin Giảng viên thành công",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"ID Giảng viên đã tồn tại",parent=self.root)

    # ================reset_data======================
    def reset_data(self):
        self.var_id.set("")
        self.var_name.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_securityQ.set("")
        self.var_securityA.set("")
        self.var_pass.set("")
 
    # ================fetch_data======================       
    def fetch_data(self):
            # global mydata
            # mydata.clear()
            conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                           port='3306')

            my_cursor = conn.cursor()
            my_cursor.execute("Select * from giangvien")
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
                for i in data:
                    self.AttendanceReportTable.insert("", END, values=i)
                    mydata.append(i)
                conn.commit()
                self.var_com_search.set("ID GV")
                self.var_search.set("")
            conn.close()
            
    # ================update======================
    def update(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
    def update_data(self):
        if self.var_securityQ.get()=="Select" or self.var_id.get()=="" or self.var_name.get()=="":
            messagebox.showerror("Error","Vui lòng nhập đầy đủ thông tin",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Bạn có muốn cập nhật bản ghi này không?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv', port='3306')
                    my_cursor = conn.cursor()
                    my_cursor.execute("update giangvien set giangvien_ten=%s,giangvien_sdt=%s,giangvien_email=%s,giangvien_cauhoi=%s,giangvien_traloi=%s,giangvien_matkhau=%s"
                                      " where giangvien_id=%s",(
                                            self.var_name.get(),
                                            self.var_phone.get(),
                                            self.var_email.get(),
                                            self.var_securityQ.get(),
                                            self.var_securityA.get(),
                                            self.var_pass.get(),
                                            self.var_id.get(),

                                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Thành công","Cập nhật thông tin điểm danh thành công",parent=self.root)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Lỗi",f"Lý do:{str(es)}",parent=self.root)

    # ================delete_data======================
    def delete_data(self):
            if self.var_id == "":
                messagebox.showerror("Lỗi", "Không được bỏ trống ID ", parent=self.root)
            else:
                try:
                    delete = messagebox.askyesno("Xoá bản ghi", "Bạn có muốn xóa bản ghi này ?", parent=self.root)
                    if delete > 0:
                        conn = mysql.connector.connect(host='localhost', user='root', password='',
                                                       database='diemdanhsv', port='3306')
                        my_cursor = conn.cursor()
                        sql = "delete from giangvien where giangvien_id=%s"
                        val = (self.var_id.get(),)
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

    # ================search_data======================
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Lỗi !","Vui lòng nhập thông tin đầy đủ",parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password='',
                                               database='diemdanhsv', port='3306')
                my_cursor = conn.cursor()#"ID Điểm Danh", "Ngày", "ID Sinh viên"
                if(self.var_com_search.get()=="ID GV"):
                    self.var_com_search.set("giangvien_id")
                elif(self.var_com_search.get()=="Tên GV"):
                    self.var_com_search.set("giangvien_ten")
                else:
                    if(self.var_com_search.get()=="SĐT"):
                        self.var_com_search.set("giangvien_sdt")
                        
                my_cursor.execute("select * from giangvien where "+str(self.var_com_search.get())+" Like '%"+str(self.var_search.get())+"%'")
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
                
if __name__=="__main__":
    root=Tk() #khoi tao cua so va gan root vao
    obj=Teacher(root)
    root.mainloop()# cua so hien len