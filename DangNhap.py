from tkinter import *
from PIL import ImageTk, Image  
from tkinter import ttk
import PIL.Image ,PIL.ImageDraw
from datetime import *
import time
from time import strftime
from math import *
import mysql.connector
from tkinter import messagebox
from TrangChu import Face_Recognition_System
from TrangChu import new_print

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.state('zoomed')
        self.root.title("Hệ thống điểm danh (Khoa Phát triển Nông thôn - Đại học Cần Thơ)")
        today = strftime("%d-%m-%Y")
        
        # =============variable============
        self.var_email = StringVar()
        self.var_password = StringVar()
        
        # ====time====
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl=Label(self.root,font=("times new roman", 11, "bold"), fg="#000000")
        lbl.place(x=80,y=35,width=100,height=18)
        time()
        lbl1 = Label(self.root,text=today, font=("times new roman", 11, "bold"), fg="#000000")
        lbl1.place(x=80, y=60, width=100, height=18)

        # root Icon Photo
        icon = PhotoImage(file='ImageFaceDetect\\pic-icon.png')
        root.iconphoto(True, icon)

        design_frame3 = Listbox(self.root, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
        design_frame3.place(x=75, y=106)

        design_frame4 = Listbox(self.root, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
        design_frame4.place(x=676, y=106)

        # ====== Email ====================
        self.txtuser = Entry(design_frame4, fg="#a7a7a7",textvariable=self.var_email, font=("yu gothic ui semibold", 12), highlightthickness=2)
        self.txtuser.place(x=134, y=170, width=256, height=34)
        self.txtuser.config(highlightbackground="black", highlightcolor="black")
        email_label = Label(design_frame4, text='• Email', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
        email_label.place(x=130, y=140)

        # ==== Password ==================
        self.txtpass = Entry(design_frame4, fg="#a7a7a7",textvariable=self.var_password, font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
        self.txtpass.place(x=134, y=250, width=256, height=34)
        self.txtpass.config(highlightbackground="black", highlightcolor="black")
        password_label = Label(design_frame4, text='• Mật khẩu', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
        password_label.place(x=130, y=220)

        # function for show and hide password
        def password_command():
            if self.txtpass.cget('show') == '•':
                self.txtpass.config(show='')
            else:
                self.txtpass.config(show='•')

        # ====== checkbutton ==============
        checkButton = Checkbutton(design_frame4, bg='#f8f8f8', command=password_command, text='show password')
        checkButton.place(x=390, y=255)

        self.varcheck = IntVar()
        checkButton = Checkbutton(design_frame4, bg='#f8f8f8', variable=self.varcheck, text="Đăng nhập Admin",)
        checkButton.place(x=140, y=290)

        # ===== Welcome Label ==============
        welcome_label = Label(design_frame4, text='Welcome', font=('Arial', 20, 'bold'), bg='#f8f8f8')
        welcome_label.place(x=150, y=15)

        # ======= top Login Button =========
        login_button = Button(self.root, text='ĐĂNG NHẬP', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                            borderwidth=0, activebackground='#1b87d2', cursor='hand2')
        login_button.place(x=870, y=175)

        login_line = Canvas(self.root, width=100, height=5, bg='#1b87d2')
        login_line.place(x=870, y=203)

        # ==== LOGIN  down button ============
        loginBtn1 = Button(design_frame4, fg='#f8f8f8', text='Đăng nhập',command=self.login, bg='#1b87d2', font=("yu gothic ui bold", 15),
                        cursor='hand2', activebackground='#1b87d2')
        loginBtn1.place(x=133, y=340, width=256, height=50)
        
        forgotPassword = Button(design_frame4, text='Quên mật khẩu', font=("yu gothic ui", 8, "bold underline"), bg='#f8f8f8',
                        borderwidth=0, activebackground='#f8f8f8',command=self.forgot_password_window, cursor="hand2")
        forgotPassword.place(x=225, y=410)

        # ======= ICONS =================
        # ===== Email icon =========
        email_icon = Image.open('ImageFaceDetect\\email-icon.png')
        photo = ImageTk.PhotoImage(email_icon)
        emailIcon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
        emailIcon_label.image = photo
        emailIcon_label.place(x=105, y=174)

        # ===== password icon =========
        password_icon = Image.open('ImageFaceDetect\\pass-icon.png')
        photo = ImageTk.PhotoImage(password_icon)
        password_icon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
        password_icon_label.image = photo
        password_icon_label.place(x=105, y=254)

        # ===== picture icon =========
        picture_icon = Image.open('ImageFaceDetect\\pic-icon.png')
        photo = ImageTk.PhotoImage(picture_icon)
        picture_icon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
        picture_icon_label.image = photo
        picture_icon_label.place(x=280, y=5)

        # ===== Left Side Picture ============
        side_image = Image.open('ImageFaceDetect\\vector.png')
        photo = ImageTk.PhotoImage(side_image)
        side_image_label = Label(design_frame3, image=photo, bg='#1e85d0')
        side_image_label.image = photo
        side_image_label.place(x=50, y=10)

    def reset(self):
        self.var_email.set("")
        self.var_password.set("")
        self.varcheck.set(0)
       
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Lỗi","Vui lòng nhập đầy đủ thông tin")
        elif(self.varcheck.get()==1) :
            conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                           port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("select * from admin where admin_ten=%s and admin_matkhau=%s", (
                self.var_email.get(),
                self.var_password.get()
            ))
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Lỗi", "Sai tên đăng nhập, mật khẩu hoặc quyền đăng nhập")
            else:
                new_print(str(0))
                self.reset()
                messagebox.showinfo("Thông báo","Bạn đã đăng nhập thành công với quyền Admin")
                self.new_window = Toplevel(self.root)
                self.app = Face_Recognition_System(self.new_window)
            conn.commit()
            conn.close()
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                           port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("select giangvien_id from giangvien where giangvien_email=%s and giangvien_matkhau=%s",(
                                    self.var_email.get(),
                                    self.var_password.get()
            ))
            row=my_cursor.fetchone()

            # print(row[0])
            if row==None:
                messagebox.showerror("Lỗi", "Sai tên đăng nhập hoặc mật khẩu")
            else:
                new_print(str(row[0]))
                # self.root.destroy()
                # import home
                self.reset()
                self.new_window = Toplevel(self.root)
                self.app = Face_Recognition_System(self.new_window)
            conn.commit()
            conn.close()
    def reset_pass(self):
            if self.combo_security_Q.get=="Select":
                messagebox.showerror("Lỗi","Hãy chọn câu hỏi bảo mật",parent=self.root2)
            elif self.txt_security.get()=="":
                messagebox.showerror("Lỗi","Hãy nhập câu trả lời",parent=self.root2)
            elif self.txt_newpassword.get()=="":
                messagebox.showerror("Lỗi", "Hãy nhập mật khẩu mới",parent=self.root2)
            else:
                conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv', port='3306')
                my_cursor = conn.cursor()
                
                query=("select * from giangvien where giangvien_email=%s and giangvien_cauhoi=%s and giangvien_traloi=%s ")
                value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
                my_cursor.execute(query,value)
                
                row = my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Lỗi","Sai câu hỏi bảo mật hoặc đáp án ",parent=self.root2)
                else:
                    query=("update giangvien set giangvien_matkhau=%s where giangvien_email=%s")
                    value=(self.txt_newpassword.get(),self.txtuser.get())
                    my_cursor.execute(query,value)
                    messagebox.showinfo("Thông báo","Mật khẩu của bạn đã được đặt lại, vui lòng đăng nhập mật khẩu mới",parent=self.root2)
                conn.commit()
                conn.close()
                self.root2.destroy()
                
    #   ************************forget password ko lagi****************
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Lỗi","Vui lòng nhập địa chỉ email để đặt lại mật khẩu")
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='', database='diemdanhsv',
                                           port='3306')
            my_cursor = conn.cursor()
            query=("select * from giangvien where giangvien_email=%s")   
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("Lỗi","Vui lòng nhập tên người dùng hợp lệ")
            else:
                conn.close()
                self.root2= Toplevel()
                self.root2.title("Đặt lại mật khẩu")
                self.root2.geometry("340x450+610+170")
                self.root2.configure(bg='white')
                
                l=Label(self.root2,text="Đặt lại mật khẩu",font=("times new roman", 15, "bold"),bg="white", fg="#1b87d2")
                l.place(x=0,y=10,relwidth=1)

                security_Q = Label(self.root2, text="Câu hỏi bảo mật:", font=("times new roman", 15, "bold"), bg="white")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Bạn thích ăn gì", "Sở thích của bạn", "Chữ số bạn thích")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Câu trả lời:", font=("times new roman", 15, "bold"), bg="white")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="Mật khẩu mới:", font=("times new roman", 15, "bold"), bg="white")
                new_password.place(x=50, y=220)

                self.txt_newpassword = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_newpassword.place(x=50, y=250, width=250)

                btn=Button(self.root2,text="Đổi mật khẩu",command=self.reset_pass,font=("times new roman", 15, "bold"), bg="#1b87d2",fg="#f8f8f8")
                btn.place(x=100,y=300)
    
if __name__=="__main__":
    root=Tk() #khoi tao cua so va gan root vao
    obj=Login_Window(root)
    root.mainloop()# cua so hien len