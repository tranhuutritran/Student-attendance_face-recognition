import os
import numpy as np
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
import PIL.Image
import PIL.ImageTk
import PIL.ImageOps
from tkinter import messagebox
import mysql.connector
import cv2
from datetime import datetime
from time import strftime
from keras.models import model_from_json
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

value_from_home = None
def new_tcid(value):
    global value_from_home
    value_from_home = value

class Face_Recognition:
    panel=None
    camara=cv2.VideoCapture(0)
    btnOpen=None
    btnClose = None

    check=1
    camara.set(3, 800) ##chiều dài
    camara.set(4, 580)  ##chiều rộng
    camara.set(10, 150)
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.state('zoomed')
        self.root.configure(bg='#7fe5ea')
        self.root.title("Hệ thống điểm danh (Khoa Phát triển Nông thôn - Đại học Cần Thơ)")
        self.isClicked=False
        self.teacherid = None
        today = strftime("%Y-%m-%d")

        img3 = PIL.Image.open(r"ImageFaceDetect\bg2.png")
        img3 = img3.resize((1350, 700), PIL.Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1350, height=700)
        
                #====time====
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(self.root,font=("times new roman", 11, "bold"),bg="#7fe5ea", fg="#000000")
        lbl.place(x=80,y=15,width=100,height=18)
        time()
        lbl1 = Label(self.root,text=today, font=("times new roman", 11, "bold"), bg="#7fe5ea", fg="#000000")
        lbl1.place(x=80, y=40, width=100, height=18)


        heading = Label(bg_img, text="HỆ THỐNG ĐIỂM DANH NHẬN DẠNG KHUÔN MẶT", font=("times new roman", 20, "bold"), bg="#7fe5ea",
                        fg="#0000FF",
                        bd=0, relief=FLAT)
        heading.place(x=400, y=15, width=700, height=30)

        self.current_image = None

        #teacher _ ID
        print(value_from_home)
        self.teacher_id=value_from_home #Chọn teacher id = id người ms đăng nhập
        #lesson_id
        self.lessonid=None


        subject_array = [] #array for append id_lesson,subject
        #call lesson_id from db
        if(value_from_home=="0" or value_from_home==None):
            conn = mysql.connector.connect(host='localhost', user='root', password='',
                                           database='diemdanhsv', port='3306')
            my_cursor = conn.cursor()
            self.teacher_id=0
            my_cursor.execute(
                "SELECT DISTINCT monhoc_ten,buoihoc_id,buoihoc.monhoc_id from buoihoc,`monhoc` where buoihoc.monhoc_id=`monhoc`.monhoc_id and buoihoc_ngay=%s",
                (today,))
            subject_ls = my_cursor.fetchall()
            for i in subject_ls:
                t = str(i).replace("'", "", 6).replace("(", "").replace(")", "").replace(" ","")  ##Subject_lsid to attendance
                # print(t)
                subject_array.append(t)
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='',
                                           database='diemdanhsv', port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute(
                "SELECT DISTINCT monhoc_ten,buoihoc_id,buoihoc.monhoc_id from buoihoc,`monhoc` where buoihoc.monhoc_id=`monhoc`.monhoc_id and buoihoc_ngay=%s and giangvien_id=%s",
                (today, self.teacher_id))
            subject_ls = my_cursor.fetchall()
            for i in subject_ls:
                t = str(i).replace("'", "", 6).replace("(", "").replace(")", "").replace(" ", "") ##Subject_lsid to attendance
                # print(t)
                subject_array.append(t)

        #=======================================LEFT FRAME=========================================
        Left_frame = LabelFrame(self.root, bd=2, bg="#6EC3C9", relief=RIDGE, text="Màn hình nhận dạng",
                                font=("times new roman", 11, "bold"))
        Left_frame.place(x=30, y=70, width=780, height=540)

        self.panel = ttk.Label(Left_frame,borderwidth=2, relief="groove")

        self.panel.place(x=8, y=50, width=760, height=420)

        #choose lesson to attendance
        self.choose_frame = LabelFrame(Left_frame, bd=1, bg="#6EC3C9", relief=RIDGE,
                                  font=("times new roman", 11, "bold"))
        self.choose_frame.place(x=8, y=0, width=760, height=40)

        search_label = Label(self.choose_frame, text="Chọn Môn/ID buổi học: ", font=("times new roman", 11, "bold"),
                             bg="#6EC3C9")
        search_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        self.selectsub=StringVar()
        self.lesson_combo = ttk.Combobox(self.choose_frame,textvariable=self.selectsub ,font=("times new roman", 12, "italic"), state="readonly",
                                    width=18)
        self.lesson_combo["values"] = subject_array
        self.lesson_combo.current()
        self.lesson_combo.bind("<<ComboboxSelected>>", self.callbackFunc)
        self.lesson_combo.grid(row=0, column=1, padx=5, pady=10, sticky=W)

        #choose attendance_value
        choose_type_att=Label(self.choose_frame, text="Chọn loại Điểm Danh: ", font=("times new roman", 12, "bold"),
                             bg="#6EC3C9")
        choose_type_att.grid(row=0, column=2, padx=35, pady=10, sticky=W)

        self.type_attendance=StringVar()
        self.type_combo=ttk.Combobox(self.choose_frame,textvariable=self.type_attendance ,font=("times new roman", 11, "bold"), state="readonly",
                                    width=18)
        self.type_combo["values"] = ("Vào","Ra")
        self.type_combo.current(0)
        self.type_combo.grid(row=0, column=3, padx=0, pady=10, sticky=W)


        #notify-attendance
        self.notify_frame = LabelFrame(Left_frame, bd=1, bg="#6EC3C9", relief=RIDGE,
                                       font=("times new roman", 11, "bold"))
        self.notify_frame.place(x=8, y=480, width=760, height=35)
        self.notify_label = Label(self.notify_frame, text="Thông báo: Vui lòng chọn Môn/ID Buổi học để mở Camera điểm danh !!!", font=("times new roman", 12, "bold"),
                             bg="#6EC3C9",fg="red")
        self.notify_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        #btn Cam
        img_btn1 = PIL.Image.open(r"ImageFaceDetect\btnOpen.png")
        img_btn1 = img_btn1.resize((350, 45), PIL.Image.ANTIALIAS)
        self.photobtn1 = ImageTk.PhotoImage(img_btn1)
        self.btnOpen= Button(self.root ,bg="#6EC3C9", cursor="hand2",
                      borderwidth=0,image=self.photobtn1,command=self.face_recog,fg="#6EC3C9",disabledforeground="black")
        self.btnOpen.place(x=30, y=620, width=350, height=45)
        if self.selectsub.get()=="":
            self.btnOpen['state'] = "disabled"

        img_btn2 = PIL.Image.open(r"ImageFaceDetect\btnClose.png")
        img_btn2 = img_btn2.resize((350, 45), PIL.Image.ANTIALIAS)
        self.photobtn2 = ImageTk.PhotoImage(img_btn2)
        self.btnClose = Button(self.root, cursor="hand2",
                      borderwidth=0,image=self.photobtn2, bg="#6EC3C9",command=self.is_clicked, fg="#6EC3C9")
        self.btnClose.place(x=460, y=620, width=350, height=45)


        #Right_frame
        self.Right_frame = LabelFrame(self.root, bd=2, bg="#6EC3C9", relief=RIDGE, text="Điểm danh thành công",
                                font=("times new roman", 12, "bold"))
        self.Right_frame.place(x=900, y=70, width=400, height=380)

        self.img_right = PIL.Image.open(r"ImageFaceDetect\unknow.jpg")
        self.img_right = self.img_right.resize((190, 190), PIL.Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(self.img_right)

        self.f_lbl = Label(self.Right_frame, image=self.photoimg_left,bg="#6EC3C9",borderwidth=2, relief="groove",highlightcolor="darkblue")
        self.f_lbl.place(x=110, y=10, width=190, height=190)

        self.studentID_atten_info=Label(self.Right_frame, bg="#6EC3C9",
                                font=("times new roman", 12, "bold"))
        self.studentID_atten_info.place(x=5, y=220, width=380, height=120)

        #IDSV
        self.studentID_label = Label(self.studentID_atten_info, text="ID Sinh viên:", font=("times new roman", 11, "bold"), bg="#6EC3C9")
        self.studentID_label.grid(row=0, column=0, padx=10,pady=7, sticky=W)

        self.studentID_atten_label = Label(self.studentID_atten_info, text="", font=("times new roman", 11, "bold"),
                                bg="#6EC3C9")
        self.studentID_atten_label.grid(row=0, column=1, padx=10, pady=7, sticky=W)


        #TenSV
        self.studentname_label = Label(self.studentID_atten_info, text="Tên Sinh viên:", font=("times new roman", 11, "bold"),
                                     bg="#6EC3C9")
        self.studentname_label.grid(row=1, column=0, padx=10, pady=7, sticky=W)

        self.studentname_atten_label = Label(self.studentID_atten_info, text="", font=("times new roman", 11, "bold"),
                                           bg="#6EC3C9")
        self.studentname_atten_label.grid(row=1, column=1, padx=10, pady=7, sticky=W)


        #Time
        self.studentclass_label = Label(self.studentID_atten_info, text="Thời gian:",
                                       font=("times new roman", 11, "bold"),
                                       bg="#6EC3C9")
        self.studentclass_label.grid(row=2, column=0, padx=10, pady=7, sticky=W)

        self.studentclass_atten_label = Label(self.studentID_atten_info, text="",
                                             font=("times new roman", 11, "bold"),
                                             bg="#6EC3C9")
        self.studentclass_atten_label.grid(row=2, column=1, padx=10, pady=7, sticky=W)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        #======================Class-info==============================
        self.RightU_frame = LabelFrame(self.root, bd=2, bg="#6EC3C9", relief=RIDGE, text="Thông tin buổi học",
                                      font=("times new roman", 11, "bold"))
        self.RightU_frame.place(x=900, y=465, width=400, height=180)
        
        # subject ID
        self.subjectid_lesson_label = Label(self.RightU_frame, text="ID - Tên Môn học:",
                                       font=("times new roman", 11, "bold"),
                                       bg="#6EC3C9")
        self.subjectid_lesson_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        self.subjectid_atten_label = Label(self.RightU_frame, text="", font=("times new roman", 11, "bold"),
                                             bg="#6EC3C9",fg="red2")
        self.subjectid_atten_label.grid(row=1, column=1, padx=10, pady=10, sticky=W)


        # subject/lesson
        self.subject_lesson_label = Label(self.RightU_frame, text="ID Buổi học:",
                                       font=("times new roman", 11, "bold"),
                                       bg="#6EC3C9")
        self.subject_lesson_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        self.subject_lesson_atten_label = Label(self.RightU_frame, text="", font=("times new roman", 11, "bold"),
                                             bg="#6EC3C9",fg="red2")
        self.subject_lesson_atten_label.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        # Time
        self.classtime_label = Label(self.RightU_frame, text="Thời gian:",
                                        font=("times new roman", 11, "bold"),
                                        bg="#6EC3C9")
        self.classtime_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        self.classtime_atten_label = Label(self.RightU_frame, text="",
                                              font=("times new roman", 11, "bold"),
                                              bg="#6EC3C9",fg="red2")
        self.classtime_atten_label.grid(row=3, column=1, padx=10, pady=10, sticky=W)


        #=============Kiem tra xem hom nay co mon hoc can diem danh khuong=====
        if not subject_array:
            self.lesson_combo['state'] = "disabled"
            self.notify_label[
                'text'] = "Bạn không có môn học nào cần điểm danh hôm nay"
            self.btnOpen['state']= "disabled"

    def is_clicked(self):
        self.isClicked=True
        self.lesson_combo['state'] = "readonly"
        self.type_combo['state']="readonly"
        self.notify_label[
            'text'] = "Vui lòng chọn ID Buổi học/Tên môn học để điểm danh"
        self.notify_label['fg']="red"

        print("Camera is Closed")

    def on_closing(self):
        self.isClicked = True
        self.root.destroy()

    def callbackFunc(self,event):
        mls = event.widget.get()
        print(mls)

        if self.selectsub.get()=="":
            self.btnOpen['state'] = "disabled"
        else:
            c = str(mls).split(",")
            self.lessonid=str(c[1])
            self.subject_name=str(c[0])
            print(self.subject_name)
            self.btnOpen['state']="normal"
            conn = mysql.connector.connect(host='localhost', user='root', password='',
                                           database='diemdanhsv', port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("select buoihoc_giobatdau,buoihoc_gioketthuc,buoihoc.monhoc_id from buoihoc,monhoc where `monhoc`.monhoc_id=buoihoc.monhoc_id and buoihoc_id=%s ",
                              (self.lessonid,))
            getInfo=my_cursor.fetchone()
            timeclass=str(getInfo[0])+" - "+str(getInfo[1])
            subject_id=str(getInfo[2])+" - "+str(c[0])
            # subject_id=getInfo[2]
            subles=self.lessonid
            self.subjectid_atten_label['text']=subject_id
            self.subject_lesson_atten_label['text']=subles
            self.classtime_atten_label['text']=timeclass
        # print(self.lessonid)


    #===========attendance===================
    def mark_attendance(self,i,r,n,d,face_cropped):
        img_id=0
        self.lesson_combo['state']="disabled"
        self.type_combo['state']="disabled"
        while True:# khi camera mở lên không có lỗi
            #Them data len csdl
            now = datetime.now()
            d1 =now.strftime("%Y-%m-%d")
            dtString = now.strftime("%H:%M:%S")
            ma="SV"+str(i)+d1+self.lessonid
            masp=ma.replace("-","")
            # print(masp)
            img_id+=1

            # kiểm tra xem Sinh viên có trong ds lớp hay không
            conn = mysql.connector.connect(host='localhost', user='root', password='',
                                           database='diemdanhsv', port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute(
                "SELECT sinhvien_id from monhocsinhvien,buoihoc,`monhoc` WHERE `monhoc`.monhoc_id=buoihoc.monhoc_id and"
                " `monhoc`.monhoc_id=monhocsinhvien.monhoc_id and buoihoc.buoihoc_id=" + self.lessonid)
            chkStudent = my_cursor.fetchall()
            chkarray = []
            for cks in chkStudent:

                chkarray.append(cks[0])

            if(i not in chkarray):
                self.notify_label['text']="Thông báo: Sinh viên "+n+" Không có trong danh sách lớp"
                print("Sinh viên:" + n + " không có trong danh sách lớp học ")
            else:
                try:
                        conn = mysql.connector.connect(host='localhost', user='root', password='',
                                                       database='diemdanhsv', port='3306')

                        my_cursor = conn.cursor()
                        my_cursor.execute("select diemdanh_ngay,buoihoc_id from diemdanh where sinhvien_id=" + str(i))

                        idn = my_cursor.fetchall()
                        a = [] #mảng ngày
                        b=[]    #mảng lesson_id

                        for i1 in idn:
                            # str2 = ''.join(i1[0])
                            # str2=''.join(i1[1])
                            a.append(str(i1[0]))
                            b.append(str(i1[1]))
                        #nếu chọn loại điểm danh là ra hoặc vào
                        if(self.type_attendance.get()=="Vào"):
                            if((d1 not in a)) or ((self.lessonid not in b)):

                                my_cursor = conn.cursor()
                                my_cursor.execute("insert into diemdanh values(%s,%s,%s,%s,%s,%s,%s)", (
                                    masp,
                                    str(i),
                                    # n,
                                    # d,
                                    dtString,
                                    None,
                                    d1,
                                    self.lessonid,
                                    "",
                                ))
                                cv2.imwrite("DiemDanhImage\ " + masp + ".jpg",
                                           face_cropped)
                                #=============================Check_attendance===============================

                                self.img_right = PIL.Image.open(r"DiemDanhImage\ " + masp + ".jpg")
                                self.img_right = self.img_right.resize((190, 190), PIL.Image.ANTIALIAS)
                                self.photoimg_left = ImageTk.PhotoImage(self.img_right)

                                self.f_lbl = Label(self.Right_frame, image=self.photoimg_left, bg="#6EC3C9", borderwidth=1,
                                                   relief="groove")
                                self.f_lbl.place(x=110, y=10, width=190, height=190)

                                # stdID
                                self.studentID_label = Label(self.studentID_atten_info, text="ID Sinh viên:",
                                                             font=("times new roman", 11, "bold"), bg="#6EC3C9")
                                self.studentID_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
                                self.studentID_atten_label = Label(self.studentID_atten_info, text=i,
                                                                   font=("times new roman", 11, "bold"),
                                                                   bg="#6EC3C9", relief="sunken", width=20, justify="left")
                                self.studentID_atten_label.grid(row=0, column=1, padx=15, pady=10, sticky=W)

                                # name
                                self.studentname_label = Label(self.studentID_atten_info, text="Tên Sinh viên:",
                                                               font=("times new roman", 11, "bold"),
                                                               bg="#6EC3C9")
                                self.studentname_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

                                self.studentname_atten_label = Label(self.studentID_atten_info, text=n,
                                                                     font=("times new roman", 11, "bold"), relief="sunken",
                                                                     width=18,
                                                                     bg="#6EC3C9", justify="left")
                                self.studentname_atten_label.grid(row=1, column=1, padx=15, pady=10, ipadx=10)

                                # class
                                self.studentclass_label = Label(self.studentID_atten_info, text="Thời gian:",
                                                                font=("times new roman", 11, "bold"),
                                                                bg="#6EC3C9")
                                self.studentclass_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
                                self.studentclass_atten_label = Label(self.studentID_atten_info, text=dtString,
                                                                      font=("times new roman", 11, "bold"),
                                                                      bg="#6EC3C9", relief="sunken", width=20, justify="left")
                                self.studentclass_atten_label.grid(row=2, column=1, padx=15, pady=10, sticky=W)
                            else:
                                # print("Sinh vien:" + n+ " Đã điểm danh ngày "+d1+ ". Vui lòng ra khỏi Camera !!")
                                self.notify_label['text'] = "Thông báo: Sinh viên: " + n + " đã điểm danh vào lớp thành công môn học "+self.subject_name
                                self.notify_label['fg']="green"

                                #=====================Change_AttendanceStatus===================================
                                my_cursor = conn.cursor()
                                my_cursor.execute("Select diemdanh_giovao from diemdanh where sinhvien_id=%s and buoihoc_id=%s ",(str(i),(self.lessonid),))
                                ckTime_in = my_cursor.fetchone()
                                time_in = ckTime_in[0]
                                # print(time_in)

                                # -======Timestart========

                                my_cursor.execute("Select buoihoc_giobatdau from buoihoc where buoihoc_id=%s ",(self.lessonid,))
                                ckStart_in = my_cursor.fetchone()
                                time_start = ckStart_in[0]
                                # print(time_start)
                                if(time_in<time_start):
                                    my_cursor.execute(
                                        "update  diemdanh set diemdanh_trangthai=%s where sinhvien_id=%s and buoihoc_id=%s",
                                        ("Có mặt", str(i), (self.lessonid),))
                                else:
                                    a = datetime.strptime(str(time_in - time_start), '%H:%M:%S').time()
                                    b = datetime.strptime('0:00:00', '%H:%M:%S').time()#thoi gian dc phep diem danh co mat 15 phut
                                    c = datetime.strptime('0:50:00', '%H:%M:%S').time()# thoi gian dc phep diem danh muon
                                    d = datetime.strptime('1:00:00', '%H:%M:%S').time()#thoi gian cho phep sv vang 1 tiet

                                    if (b < a < c):

                                        stt="Đi muộn " + str(a.minute)+" phút"
                                        # print(stt)
                                        my_cursor.execute("update  diemdanh set diemdanh_trangthai=%s where sinhvien_id=%s and buoihoc_id=%s",
                                                          (stt,str(i),(self.lessonid),))
                                    elif (c < a < d):
                                        my_cursor.execute("update  diemdanh set diemdanh_trangthai=%s where sinhvien_id=%s and buoihoc_id=%s",
                                                          ("Vắng 1 tiết",str(i),(self.lessonid),))
                                    else:
                                        my_cursor.execute("update  diemdanh set diemdanh_trangthai=%s where sinhvien_id=%s and buoihoc_id=%s",
                                                          ("Vắng",str(i),(self.lessonid),))
                                    # print("Vắng")
                            conn.commit()
                            # self.fetch_data()
                            conn.close()
                            # messagebox.showinfo("Thành công", "Thêm thông tin Sinh viên thành công", parent=self.root)
                        elif(self.type_attendance.get()=="Ra"):
                            conn = mysql.connector.connect(host='localhost', user='root', password='',
                                                           database='diemdanhsv', port='3306')

                            my_cursor = conn.cursor()
                            my_cursor.execute("select diemdanh_id from diemdanh")
                            idatt = my_cursor.fetchall()
                            att=[]
                            for ida in idatt:
                                att.append(str(ida[0]))
                            if(masp not in att):
                                if ((d1 not in a)) or ((self.lessonid not in b)):

                                    my_cursor = conn.cursor()
                                    my_cursor.execute("insert into diemdanh values(%s,%s,%s,%s,%s,%s,%s)", (
                                        masp,
                                        str(i),
                                        # n,
                                        # d,
                                        None,
                                        dtString,
                                        d1,
                                        self.lessonid,
                                        "Có mặt",
                                    ))
                                    cv2.imwrite("DiemDanhImage\ " + masp +"Ra"+ ".jpg",
                                                face_cropped)
                                    # =============================Check_attendance===============================

                                    self.img_right = PIL.Image.open(r"DiemDanhImage\ " + masp +"Ra" +".jpg")
                                    self.img_right = self.img_right.resize((190, 190), PIL.Image.ANTIALIAS)
                                    self.photoimg_left = ImageTk.PhotoImage(self.img_right)

                                    self.f_lbl = Label(self.Right_frame, image=self.photoimg_left, bg="#6EC3C9",
                                                       borderwidth=1,
                                                       relief="groove")
                                    self.f_lbl.place(x=110, y=10, width=190, height=190)

                                    # stdID
                                    self.studentID_label = Label(self.studentID_atten_info, text="ID Sinh viên:",
                                                                 font=("times new roman", 11, "bold"), bg="#6EC3C9")
                                    self.studentID_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
                                    self.studentID_atten_label = Label(self.studentID_atten_info, text=i,
                                                                       font=("times new roman", 11, "bold"),
                                                                       bg="#6EC3C9", relief="sunken", width=20,
                                                                       justify="left")
                                    self.studentID_atten_label.grid(row=0, column=1, padx=15, pady=10, sticky=W)

                                    # name
                                    self.studentname_label = Label(self.studentID_atten_info, text="Tên Sinh viên:",
                                                                   font=("times new roman", 11, "bold"),
                                                                   bg="#6EC3C9")
                                    self.studentname_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

                                    self.studentname_atten_label = Label(self.studentID_atten_info, text=n,
                                                                         font=("times new roman", 11, "bold"),
                                                                         relief="sunken",
                                                                         width=18,
                                                                         bg="#6EC3C9", justify="left")
                                    self.studentname_atten_label.grid(row=1, column=1, padx=15, pady=10, ipadx=10)

                                    # class
                                    self.studentclass_label = Label(self.studentID_atten_info, text="Thời gian:",
                                                                    font=("times new roman", 11, "bold"),
                                                                    bg="#6EC3C9")
                                    self.studentclass_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
                                    self.studentclass_atten_label = Label(self.studentID_atten_info, text=dtString,
                                                                          font=("times new roman", 11, "bold"),
                                                                          bg="#6EC3C9", relief="sunken", width=20,
                                                                          justify="left")
                                    self.studentclass_atten_label.grid(row=2, column=1, padx=15, pady=10, sticky=W)
                                else:
                                    # print(
                                    #     "Sinh vien:" + n + " Đã điểm danh ngày " + d1 + ". Vui lòng ra khỏi Camera !!")
                                    self.notify_label[
                                        'text'] = "Thông báo: Sinh viên: " + n + " đã điểm danh ra thành công môn học " + self.subject_name
                                    self.notify_label['fg'] = "green"

                                    # =====================Change_AttendanceStatus===================================
                                    my_cursor = conn.cursor()
                                    my_cursor.execute(
                                        "Select diemdanh_giora from diemdanh where sinhvien_id=%s and buoihoc_id=%s ",
                                        (str(i), (self.lessonid),))
                                    ckTime_out = my_cursor.fetchone()
                                    time_out = ckTime_out[0]
                                    # print(time_out)

                                    # -======Timeend========

                                    my_cursor.execute("Select buoihoc_gioketthuc from buoihoc where buoihoc_id=%s ",
                                                      (self.lessonid,))
                                    ckend_in = my_cursor.fetchone()
                                    time_end = ckend_in[0]
                                    # print(time_start)
                                    if(time_end<time_out):
                                        my_cursor.execute(
                                            "update  diemdanh set diemdanh_trangthai=%s where sinhvien_id=%s and buoihoc_id=%s",
                                            ("Có mặt", str(i), (self.lessonid),))
                                    else:
                                        a = datetime.strptime(str(time_end - time_out), '%H:%M:%S').time()
                                        b = datetime.strptime('0:15:00',
                                                              '%H:%M:%S').time()  # thoi gian dc phep diem danh co mat trc 15p
                                        c = datetime.strptime('0:50:00',
                                                              '%H:%M:%S').time()  # thoi gian dc phep diem danh muon

                                        if (a < b):
                                            my_cursor.execute(
                                                "update  diemdanh set diemdanh_trangthai=%s where sinhvien_id=%s and buoihoc_id=%s",
                                                ("Có mặt", str(i), (self.lessonid),))
                                        elif (b < a < c):
                                            my_cursor.execute(
                                                "update  diemdanh set diemdanh_trangthai=%s where sinhvien_id=%s and buoihoc_id=%s",
                                                ("Vắng 1 tiết", str(i), (self.lessonid),))
                                        else:
                                            my_cursor.execute(
                                                "update  diemdanh set diemdanh_trangthai=%s where sinhvien_id=%s and buoihoc_id=%s",
                                                ("Vắng", str(i), (self.lessonid),))

                            else:
                                my_cursor = conn.cursor()
                                my_cursor.execute("select diemdanh_giora from diemdanh where diemdanh_id=%s",(masp,))
                                timeout_check=my_cursor.fetchone()
                                if(timeout_check[0]==None):
                                    my_cursor = conn.cursor()
                                    my_cursor.execute(
                                        "update  diemdanh set diemdanh_giora=%s where sinhvien_id=%s and buoihoc_id=%s",
                                        (dtString, str(i), (self.lessonid),))
                                    cv2.imwrite("DiemDanhImage\ " + masp + "Ra" + ".jpg",
                                                face_cropped)
                                    # =============================Check_attendance===============================

                                    self.img_right = PIL.Image.open(r"DiemDanhImage\ " + masp + "Ra" + ".jpg")
                                    self.img_right = self.img_right.resize((190, 190), PIL.Image.ANTIALIAS)
                                    self.photoimg_left = ImageTk.PhotoImage(self.img_right)

                                    self.f_lbl = Label(self.Right_frame, image=self.photoimg_left, bg="#6EC3C9",
                                                       borderwidth=1,
                                                       relief="groove")
                                    self.f_lbl.place(x=110, y=10, width=190, height=190)

                                    # stdID
                                    self.studentID_label = Label(self.studentID_atten_info, text="ID Sinh viên:",
                                                                 font=("times new roman", 11, "bold"), bg="#6EC3C9")
                                    self.studentID_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
                                    self.studentID_atten_label = Label(self.studentID_atten_info, text=i,
                                                                       font=("times new roman", 11, "bold"),
                                                                       bg="#6EC3C9", relief="sunken", width=20,
                                                                       justify="left")
                                    self.studentID_atten_label.grid(row=0, column=1, padx=15, pady=10, sticky=W)

                                    # name
                                    self.studentname_label = Label(self.studentID_atten_info, text="Tên Sinh viên:",
                                                                   font=("times new roman", 11, "bold"),
                                                                   bg="#6EC3C9")
                                    self.studentname_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

                                    self.studentname_atten_label = Label(self.studentID_atten_info, text=n,
                                                                         font=("times new roman", 11, "bold"),
                                                                         relief="sunken",
                                                                         width=18,
                                                                         bg="#6EC3C9", justify="left")
                                    self.studentname_atten_label.grid(row=1, column=1, padx=15, pady=10, ipadx=10)

                                    # class
                                    self.studentclass_label = Label(self.studentID_atten_info, text="Thời gian:",
                                                                    font=("times new roman", 11, "bold"),
                                                                    bg="#6EC3C9")
                                    self.studentclass_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
                                    self.studentclass_atten_label = Label(self.studentID_atten_info, text=dtString,
                                                                          font=("times new roman", 11, "bold"),
                                                                          bg="#6EC3C9", relief="sunken", width=20,
                                                                          justify="left")
                                    self.studentclass_atten_label.grid(row=2, column=1, padx=15, pady=10, sticky=W)
                                else:
                                    # print(
                                    #     "Sinh vien:" + n + " Đã điểm danh ngày " + d1 + ". Vui lòng ra khỏi Camera !!")
                                    self.notify_label[
                                        'text'] = "Thông báo: Sinh viên: " + n + " đã điểm danh ra thành công môn học " + self.subject_name
                                    self.notify_label['fg'] = "green"
                                    # =====================Change_AttendanceStatus===================================
                                    my_cursor = conn.cursor()
                                    my_cursor.execute(
                                        "Select diemdanh_giora from diemdanh where sinhvien_id=%s and buoihoc_id=%s ",
                                        (str(i), (self.lessonid),))
                                    ckTime_out = my_cursor.fetchone()
                                    time_out = ckTime_out[0]
                                    # print(time_out)

                                    # -======Timestart========

                                    my_cursor.execute("Select buoihoc_gioketthuc from buoihoc where buoihoc_id=%s ",
                                                      (self.lessonid,))
                                    ckend_in = my_cursor.fetchone()
                                    time_end = ckend_in[0]
                                    # print(time_start)
                                    if (time_end < time_out):
                                        my_cursor.execute(
                                            "update  diemdanh set diemdanh_trangthai=%s where sinhvien_id=%s and buoihoc_id=%s",
                                            ("Có mặt", str(i), (self.lessonid),))
                                    else:
                                        a = datetime.strptime(str(time_end - time_out), '%H:%M:%S').time()
                                        b = datetime.strptime('0:15:00',
                                                              '%H:%M:%S').time()  # thoi gian dc phep diem danh co mat trc 15p
                                        c = datetime.strptime('0:50:00',
                                                              '%H:%M:%S').time()  # thoi gian dc phep diem danh muon

                                        if (a < b):
                                            my_cursor.execute(
                                                "update  diemdanh set diemdanh_trangthai=%s where sinhvien_id=%s and buoihoc_id=%s",
                                                ("Có mặt", str(i), (self.lessonid),))
                                        elif (b < a < c):
                                            my_cursor.execute(
                                                "update  diemdanh set diemdanh_trangthai=%s where sinhvien_id=%s and buoihoc_id=%s",
                                                ("Vắng 1 tiết", str(i), (self.lessonid),))
                                        else:
                                            my_cursor.execute(
                                                "update  diemdanh set diemdanh_trangthai=%s where sinhvien_id=%s and buoihoc_id=%s",
                                                ("Vắng", str(i), (self.lessonid),))


                            conn.commit()
                            conn.close()


                except Exception as es:
                        messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
            if img_id==1:
                break

    def face_recog(self):
            self.isClicked=False
            # Load Anti-Spoofing Model graph
            json_file = open('antispoofing_models/finalyearproject_antispoofing_model_mobilenet.json', 'r')
            loaded_model_json = json_file.read()
            json_file.close()
            model = model_from_json(loaded_model_json)                   
            # load antispoofing model weights
            model.load_weights('antispoofing_models/finalyearproject_antispoofing_model_95-0.999048.h5')

            def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
                gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

                coord=[]
                for(x,y,w,h) in features:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),3)
                    id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                    confidence=int((100*(1-predict/300)))

                    #Cat anh
                    face_cropped = gray_image[y:y + h+35, x:x + w+35]
                    face_cropped=cv2.cvtColor(face_cropped,cv2.COLOR_GRAY2BGR)
                    face_cropped=cv2.resize(face_cropped,(160,160))

                    # Tinh nguong nhan dien gia? mao
                    # resized_face = cv2.resize(face, (160, 160))
                    # resized_face = resized_face.astype("float") / 255.0
                    resized_face = face_cropped.astype("float") / 255.0
                    # resized_face = img_to_array(resized_face)
                    resized_face = np.expand_dims(resized_face, axis=0)
                    preds = model.predict(resized_face)[0]

                    conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv', port='3306')
                    my_cursor = conn.cursor()

                    my_cursor.execute("select sinhvien_ten from sinhvien where sinhvien_id=" + str(id))
                    n = my_cursor.fetchone()
                    n = "+".join(n)


                    my_cursor.execute("select sinhvien_email from sinhvien where sinhvien_id=" + str(id))
                    r = my_cursor.fetchone()
                    r = "+".join(r)

                    my_cursor.execute("select lop_id from sinhvien where sinhvien_id=" + str(id))
                    d = my_cursor.fetchone()
                    d = "+".join(d)

                    my_cursor.execute("select sinhvien_id from sinhvien where sinhvien_id=" + str(id))
                    i = my_cursor.fetchone()
                    i = i[0]
                    if preds > 0.3:
                        label = 'Spoof Face'
                        cv2.putText(img, label, (x, y - 10),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                        cv2.rectangle(img, (x, y), (x + w, y + h),
                                      (0, 0, 255), 2)
                        self.notify_label['text'] = "CẢNH BÁO: Khuôn mặt hiển thị là giả mạo !!! Vui lòng kiểm tra lại"
                        self.notify_label['fg'] = "red"
                    else:
                        if confidence>77:
                            cv2.putText(img,f"ID:{i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                            cv2.putText(img, f"Name:{n}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)

                            # cv2.imwrite("DiemDanhImage\ " + i + "." + n + '.' + d + ".jpg",
                            #            array[0])

                            self.mark_attendance(i,r,n,d,face_cropped)
                        else:
                            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                            cv2.putText(img,"Unknow Face",(x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                        coord=[x,y,w,h]
                return coord

            def recognize(img,clf,faceCascade):
                coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
                return img
            faceCascade=cv2.CascadeClassifier("models/haarcascade_frontalface_default.xml")
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.read("models/classifier.xml")

            self.camara=cv2.VideoCapture(0)
            self.camara.set(3, 800) ##chiều dài
            self.camara.set(4, 580)  ##chiều rộng
            self.camara.set(10, 150)  #độ sáng
            while True:

                ret,img=self.camara.read()
                img=recognize(img,clf,faceCascade)
                # cv2.imshow("Welcome to face REg",img)
                img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                
                img = PIL.Image.fromarray(img, mode='RGB')
                img = PIL.ImageTk.PhotoImage(img)  # convert image for tkinter
                self.panel['image']=img
                # self.panel.update()
                self.panel.update()

                if (self.isClicked==True): ##Bam Q de thoat cam
                    break
            self.camara.release()
            cv2.destroyAllWindows()

if __name__=="__main__":
    root=Tk() #khoi tao cua so va gan root vao
    obj=Face_Recognition(root)
    root.mainloop()# cua so hien len