from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
import PIL.Image
from time import strftime
from math import *
from tkinter import messagebox
from SinhVien import Student
from NhanDang import Face_Recognition
from DiemDanh import Attendance
from NhanDang import new_tcid
from MonHoc import Subject
from GiangVien import Teacher
from BuoiHoc import Lesson
from Thongke import report
from Thongke import new_tcid


import mysql.connector

value_from_p1 = None

def new_print(value):
    global value_from_p1
    value_from_p1 = value
    print(value_from_p1)
    
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg='#323f48')
        self.root.state('zoomed')
        self.root.title("Hệ thống điểm danh (Khoa Phát triển Nông thôn - Đại học Cần Thơ)")
        
        today = strftime("%Y-%m-%d")

        new_tcid(value_from_p1)
        #background
        print(value_from_p1)
        img3 = PIL.Image.open(r"ImageFaceDetect\bgnew1.jpg")
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
        lbl=Label(self.root,font=("times new roman", 11, "bold"),bg="#323f48", fg="white")
        lbl.place(x=80,y=35,width=100,height=18)
        time()
        lbl1 = Label(self.root,text=today, font=("times new roman", 11, "bold"), bg="#323f48", fg="white")
        lbl1.place(x=80, y=60, width=100, height=18)

        #====title=========
        self.txt = "HỆ THỐNG ĐIỂM DANH NHẬN DẠNG KHUÔN MẶT"
        self.count = 0
        self.text = ''
        self.heading = Label(self.root, text=self.txt, font=("yu gothic ui", 26, "bold"), bg="#323f48", fg="white",
                             bd=5, relief=FLAT)
        self.heading.place(x=250, y=22, width=900)
        
        #=========account===========
        #===get email from db=============
        self.account=""
        if(value_from_p1=="0"):
            self.account = "Admin"
        elif(value_from_p1==None):
            self.account="Admin"
        else:

            conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                           port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("select giangvien_email from giangvien where giangvien_id=%s", (
                value_from_p1,
            ))
            row = my_cursor.fetchone()
            self.account = row[0]
        img_peop = PIL.Image.open(r"ImageFaceDetect\peop.png")
        img_peop = img_peop.resize((27, 27), PIL.Image.ANTIALIAS)
        self.photoimgpeop = ImageTk.PhotoImage(img_peop)
        time_img = Label(self.root, image=self.photoimgpeop, bg="#FFFF99")
        time_img.place(x=974, y=100, width=27, height=27)
        self.lblemail = Label(self.root,text=self.account, font=("times new roman", 12, "bold"), bg="#FFFF99", fg="#0000FF")
        self.lblemail.place(x=1000, y=100, width=100, height=27)

        #=======logout==========
        img_logout = PIL.Image.open(r"ImageFaceDetect\logout.png")
        img_logout = img_logout.resize((27, 27), PIL.Image.ANTIALIAS)
        self.photoimglogout = ImageTk.PhotoImage(img_logout)

        b1 = Button(self.root, image=self.photoimglogout, cursor="hand2", command=self.exit,borderwidth=0,bg="#FFFF99",activebackground="#C0C0C0")
        b1.place(x=1153, y=100, width=27, height=27)

        b1_1 = Button(self.root, text="Đăng xuất", cursor="hand2", command=self.exit,
                      font=("times new roman", 11, "bold"),
                      bg="#FFFF99", fg="#FF0000",borderwidth=0,activebackground="#C0C0C0")
        b1_1.place(x=1180, y=100, width=100, height=27)


        #============Sinh viên================
        img_btn2 = PIL.Image.open(r"ImageFaceDetect\student.png")
        img_btn2 = img_btn2.resize((70, 103), PIL.Image.ANTIALIAS)
        self.photobtn2 = ImageTk.PhotoImage(img_btn2)

        b8 = Button(self.root, text="Sinh viên", font=("times new roman", 16, "bold"),command=self.student_details, image=self.photobtn2,
                    cursor="hand2",
                    activebackground="white", bg="white", borderwidth=0, compound="top")
        b8.place(x=460, y=180, width=160, height=160)

        #============Nhận diện============
        img_btn3 = PIL.Image.open(r"ImageFaceDetect\nhandien.png")
        img_btn3 = img_btn3.resize((70, 103), PIL.Image.ANTIALIAS)
        self.photobtn3 = ImageTk.PhotoImage(img_btn3)

        b3 = Button(self.root, text="Nhận diện", font=("times new roman", 16, "bold"),command=self.face_recognition ,image=self.photobtn3,
                    cursor="hand2",
                    activebackground="white", bg="white", borderwidth=0, compound="top")
        b3.place(x=150, y=180, width=160, height=160)


        #==========Môn học=================
        img_btn5 = PIL.Image.open(r"ImageFaceDetect\book.png")
        img_btn5 = img_btn5.resize((70, 103), PIL.Image.ANTIALIAS)
        self.photobtn5 = ImageTk.PhotoImage(img_btn5)

        b5 = Button(self.root, text="Môn học", font=("times new roman", 16, "bold"),command=self.subject_data, image=self.photobtn5,
                    cursor="hand2",
                    activebackground="white", bg="white", borderwidth=0, compound="top")
        b5.place(x=760, y=180, width=160, height=160)

        #==========Buổi học================
        img_btn7 = PIL.Image.open(r"ImageFaceDetect\lesson.png")
        img_btn7 = img_btn7.resize((70, 103), PIL.Image.ANTIALIAS)
        self.photobtn7 = ImageTk.PhotoImage(img_btn7)

        b7 = Button(self.root, text="Buổi học", font=("times new roman", 16, "bold"),command=self.lesson_data, image=self.photobtn7,
                    cursor="hand2",
                    activebackground="white", bg="white", borderwidth=0, compound="top")
        b7.place(x=1058, y=180, width=160, height=160)

        #===========Điểm danh===============
        img_btn4 = PIL.Image.open(r"ImageFaceDetect\ghichu.png")
        img_btn4 = img_btn4.resize((70, 103), PIL.Image.ANTIALIAS)
        self.photobtn4 = ImageTk.PhotoImage(img_btn4)

        b4 = Button(self.root, text="Điểm danh", font=("times new roman", 16, "bold"),command=self.attendance_data ,image=self.photobtn4,
                    cursor="hand2",
                    activebackground="white", bg="white", borderwidth=0, compound="top")
        b4.place(x=300, y=438, width=160, height=160)
        
        #==========Giảng viên=============
        img_btn6 = PIL.Image.open(r"ImageFaceDetect\teacher.png")
        img_btn6 = img_btn6.resize((70, 103), PIL.Image.ANTIALIAS)
        self.photobtn6 = ImageTk.PhotoImage(img_btn6)

        b6 = Button(self.root, text="Giảng viên", font=("times new roman", 16, "bold"),command=self.teacher_data, image=self.photobtn6,
                    cursor="hand2",
                    activebackground="white", bg="white", borderwidth=0, compound="top")
        b6.place(x=610, y=438, width=160, height=160)
 
        #=============Thống kê================
        img_btn1 = PIL.Image.open(r"ImageFaceDetect\report.png")
        img_btn1 = img_btn1.resize((70, 103), PIL.Image.ANTIALIAS)
        self.photobtn1 = ImageTk.PhotoImage(img_btn1)

        b2 = Button(self.root, text="Thống kê",font=("times new roman", 16, "bold"),command=self.report,image=self.photobtn1,cursor="hand2",
                    activebackground="white",bg="white",borderwidth=0,compound="top")
        b2.place(x=910, y=438, width=160, height=160)
        
        
        if(value_from_p1=="0" or value_from_p1==None):
            b8['state']="normal"
            b4['state']="normal"
            b5['state']="normal"
            b6['state']="normal"
            b7['state']="normal"
        else:
            change_pass = Button(self.root, text="Đổi mật khẩu", cursor="hand2", command=self.change_pass,
                          font=("times new roman", 11, "bold"),
                          bg="#38a6f0", fg="white", borderwidth=0)
            change_pass.place(x=1153, y=135, width=126, height=27)
            b8['state'] = "disabled"
            b4['state'] = "disabled"
            b5['state'] = "disabled"
            b6['state'] = "disabled"
            b7['state'] = "disabled"
            
    def exit(self):
        Exit = messagebox.askyesno("Đăng xuất", "Bạn có chắc chắn muốn đăng xuất không?", parent=self.root)
        if(Exit>0):
            self.root.destroy()
        else:
            if not Exit:
                return
            
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def report(self):
        self.new_window=Toplevel(self.root)
        self.app=report(self.new_window)
        
    def face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def subject_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Subject(self.new_window)
        
    def teacher_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Teacher(self.new_window)
        
    def lesson_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Lesson(self.new_window)   
                  
    def reset_pass(self):
        if self.changePass_entry.get=="Select":
            messagebox.showerror("Lỗi","Hãy chọn câu hỏi bảo mật",parent=self.root2)
        elif self.answerLabel_entry.get()=="":
            messagebox.showerror("Lỗi","Hãy nhập câu trả lời",parent=self.root2)
        elif self.passLabel_entry.get()=="":
            messagebox.showerror("Lỗi", "Hãy nhập mật khẩu mới",parent=self.root2)
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                           port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute(
                "SELECT  * from giangvien where giangvien_id=%s and giangvien_cauhoi=%s and giangvien_traloi=%s",
                (str(value_from_p1),self.changePass_entry.get(),self.answerLabel_entry.get(),))
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Lỗi","Sai câu hỏi bảo mật hoặc đáp án ",parent=self.root2)
            else:
                my_cursor.execute("update giangvien set giangvien_matkhau=%s where giangvien_id=%s",(self.passLabel_entry.get(),str(value_from_p1),))
                conn.commit()
                conn.close()
                messagebox.showinfo("Thông báo","Đổi mật khẩu thành công",parent=self.root2)
                self.root2.destroy()
                
    def change_pass(self):
        self.root2=Toplevel()
        self.root2.title("Đổi mật khẩu")
        self.root2.geometry("340x450+910+70")
        self.root2.configure(bg='white')
        l=Label(self.root2,text="Đổi mật khẩu",font=("times new roman",20,"bold"),fg="black",bg="white")
        l.place(x=0,y=10,relwidth=1)
        changePass = Label(self.root2, text="Câu hỏi bảo mật:", font=("times new roman", 12, "bold"),
                          bg="white")
        changePass.place(x=50,y=80)

        self.changePass_entry = ttk.Combobox(self.root2, width=20,
                                       font=("times new roman", 12, "bold"), state='readonly')
        self.changePass_entry["values"] = ("Select", "Bạn thích ăn gì", "Sở thích của bạn", "Chữ số bạn thích")
        self.changePass_entry.place( x=50,y=110,width=250)
        self.changePass_entry.current(0)

        # answer
        answerLabel = Label(self.root2, text="Câu trả lời:", font=("times new roman", 12, "bold"),
                          bg="white")
        answerLabel.place(x=50,y=150)

        self.answerLabel_entry = ttk.Entry(self.root2, width=22,
                                    font=("times new roman", 12, "bold"))
        self.answerLabel_entry.place(x=50,y=180,width=250)

        # pass
        passLabel = Label(self.root2, text="Mật khẩu mới:", font=("times new roman", 12, "bold"),
                          bg="white")
        passLabel.place(x=50,y=220)

        self.passLabel_entry = ttk.Entry(self.root2, width=22,
                                    font=("times new roman", 12, "bold"),show="*")
        self.passLabel_entry.place(x=50,y=250,width=250)

        btn=Button(self.root2,text="Đổi mật khẩu",font=("times new roman", 12, "bold"),fg="white",bg="darkblue",command=self.reset_pass)
        btn.place(x=120,y=300)
        
if __name__=="__main__":
    root=Tk() #khoi tao cua so va gan root vao
    obj=Face_Recognition_System(root)
    root.mainloop()# cua so hien len