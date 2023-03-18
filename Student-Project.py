from tkinter import *
from tkinter import ttk
import os

class Student :
    def __init__(self, root ):

        self.path_file = os.path.abspath(__file__)
        self.link = os.path.dirname(self.path_file)

        #! Mack windo ----
        self.wind = root
        self.wind.geometry('1400x700')
        self.wind.resizable(False,False)
        self.wind.title('Student-Project')
        self.wind.iconbitmap(r"{}\Database\student-icon.ico".format(self.link))
        self.wind.configure(background="white")
        self.lbl_student = Label( self.wind , text=" Student Project " , fg="black",bg="#2980B9",font=("High Tower Text",15))
        self.lbl_student.pack(fill=X)

        #! The variables --- 
        self.var_to_add_student = ""
        self.name_var = StringVar()
        self.age_var = StringVar()
        self.address_var = StringVar()
        self.dele_var = StringVar()
        self.phone_var = StringVar()
        self.id_var = StringVar()
        self.gender_var = StringVar()
        self.averag_var = StringVar()
        self.search_id_name_phone = StringVar()
        self.search = StringVar()

        #! manager banel ---
        frame_manager = Frame(self.wind ,bg="White")
        frame_manager.place(x=1200,y=30,width=200,height=500)
        frame_manager_style = Frame(self.wind , bg="#2980B9")
        frame_manager_style.place(x=1198,y=30,width=2,height=500)
        frame_manager_style2 = Frame(self.wind , bg="#2980B9")
        frame_manager_style2.place(x=1199,y=530,width=201,height=2)
        lbl_manager = Label(frame_manager , text="control bnal",bg="White",fg="black",font=("Imprint MT Shadow",12))
        lbl_manager.pack()
        lbl_id = Label(frame_manager,text="ID",bg="white",font=("Impact",13),fg="#2980B9")
        lbl_id.pack()
        enter_id = Entry(frame_manager,textvariable=self.id_var,bg="White",bd='2',font=("Century",12),fg="black",justify="center")
        enter_id.pack()
        lbl_name = Label(frame_manager,text="Name",bg="white",font=("Impact",13),fg="#2980B9")
        lbl_name.pack()
        enter_name = Entry(frame_manager,textvariable=self.name_var,bg="White",bd='2',font=("Century",12),fg="black",justify="center")
        enter_name.pack()
        lbl_age = Label(frame_manager,text="Age",bg="White",font=("Impact",13),fg="#2980B9")
        lbl_age.pack()
        enter_age = Entry(frame_manager,textvariable=self.age_var,bg="White",bd='2',font=("Century",12),fg="black",justify="center")
        enter_age.pack()
        lbl_avg = Label(frame_manager,text="Averag",bg="White",font=("Impact",13),fg="#2980B9")
        lbl_avg.pack()
        enter_avg= Entry(frame_manager,textvariable=self.averag_var,bg="White",bd='2',font=("Century",12),fg="black",justify="center")
        enter_avg.pack()
        lbl_phone = Label(frame_manager,text="Phone Number",bg="White",font=("Impact",13),fg="#2980B9")
        lbl_phone.pack()
        enter_phone = Entry(frame_manager,textvariable=self.phone_var,bg="White",bd='2',font=("Century",12),fg="black",justify="center")
        enter_phone.pack()
        lbl_address = Label(frame_manager,text="Address",bg="White",font=("Impact",13),fg="#2980B9")
        lbl_address.pack()
        enter_address = Entry(frame_manager,textvariable=self.address_var,bg="White",bd='2',font=("Century",12),fg="black",justify="center")
        enter_address.pack()
        lbl_gender = Label(frame_manager,text="Gender",bg="White",font=("Impact",13),fg="#2980B9")
        lbl_gender.pack()
        chack_gender = Radiobutton( frame_manager ,text="Male",fg="#2980B9", bg="White",font=("Impact",13), activebackground="White",activeforeground="#2980B9",variable=self.gender_var,value="Male")
        chack_gender.place(x=30,y=370)
        chack_gender = Radiobutton( frame_manager ,text="Female",fg="#2980B9", bg="White",font=("Impact",13), activebackground="White",activeforeground="#2980B9",variable=self.gender_var,value="Female")
        chack_gender.place(x=100,y=370)
        lbl_del_ID = Label(frame_manager,text="Delete With ID",bg="White",font=("Impact",13),fg="#EB0202")
        lbl_del_ID.place(x=40,y=400)
        enter_del_ID = Entry(frame_manager,textvariable=self.dele_var,bg="White",bd='2',font=("Century",12),fg="black",justify="center")
        enter_del_ID.place(x=7,y=430)
        but_dle_ID = Button(frame_manager,text="Delete",fg="#EB0202",bg="#E5E7E9",font=("Century",10),activebackground="white",activeforeground="#EB0202",command=self.delete)
        but_dle_ID.place(x=40,y=460,width=130)
        
        #! The control buttons ----
        frame_button = Frame( self.wind , bg='White')
        frame_button.place(x=1200,y=537,width=200,height=160)
        frame_button_style = Frame(self.wind , bg="#2980B9")
        frame_button_style.place(x=1198,y=532,width=2,height=500)
        frame_button_style2 = Frame(self.wind , bg="#2980B9")
        frame_button_style2.place(x=1200,y=532,width=200,height=3)
        button_add = Button(frame_button,text="Add",fg="#1B2631",bg="#E5E7E9",font=("Century",10),activebackground="White",activeforeground="#2980B9",command=self.add_student)
        button_add.place(x=40,y=5,width=130)
        button_modify = Button(frame_button,text="Modify Data",fg="#1B2631",bg="#E5E7E9",font=("Century",10),activebackground="White",activeforeground="#2980B9",command=self.update)
        button_modify.place(x=40,y=35,width=130)
        button_clear = Button(frame_button,text="Clear",fg="#1B2631",bg="#E5E7E9",font=("Century",10),activebackground="White",activeforeground="#2980B9",command=self.clear)
        button_clear.place(x=40,y=65,width=130)
        button_abot = Button(frame_button,text="Abot",fg="#1B2631",bg="#E5E7E9",font=("Century",10),activebackground="White",activeforeground="#2980B9",command=self.About)
        button_abot.place(x=40,y=95,width=130)
        button_exit = Button(frame_button,text="Exit",fg="#1B2631",bg="#E5E7E9",font=("Century",10),activebackground="White",activeforeground="#2980B9",command=self.wind.quit)
        button_exit.place(x=40,y=125,width=130)

        #! The search frame ----
        self.frame_search = Frame( self.wind , bg="White")
        self.frame_search.place(x=1,y=30,width=1195,height=100)
        self.frame_search_style = Frame( self.wind , bg="#2980B9")
        self.frame_search_style.place(x=1196,y=30,width=3,height=700)
        self.frame_search_style = Frame( self.wind , bg="#2980B9")
        self.frame_search_style.place(x=1,y=133,width=1198,height=2)
        lbl_search = Label(self.frame_search , text="Search With :",bg="White",font=("Impact",13),fg="#2980B9")
        lbl_search.place(x=400,y=30)
        rad_button_search_name = Radiobutton( self.frame_search,text="Name",fg="#2980B9", bg="White",font=("Impact",13), activebackground="White",activeforeground="#2980B9",variable=self.search_id_name_phone,value="name")
        rad_button_search_name.place(x=500,y=28)
        rad_button_search_id = Radiobutton( self.frame_search,text="ID",fg="#2980B9", bg="White",font=("Impact",13), activebackground="White",activeforeground="#2980B9",variable=self.search_id_name_phone,value="ID")
        rad_button_search_id.place(x=580,y=28)
        rad_button_search_phone = Radiobutton( self.frame_search,text="Phone Number",fg="#2980B9", bg="White",font=("Impact",13), activebackground="White",activeforeground="#2980B9",variable=self.search_id_name_phone,value="phone")
        rad_button_search_phone.place(x=640,y=28)
        entry_search = Entry(self.frame_search , bg="White" , bd='2',font=("Century",12),fg="black",justify="center",textvariable=self.search)
        entry_search.place(x=800,y=30)
        button_search = Button(self.frame_search,text="Search",fg="#1B2631",bg="White",font=("Century",10),activebackground="White",activeforeground="#2980B9",command=self.search_student)
        button_search.place(x=1000,y=30)

        #! Show info frame -----
        frame_show = Frame(self.wind , bg="White")
        frame_show.place(x=1,y=135,width=1195,height=565)

        scroll_x_show = Scrollbar(frame_show , orient=HORIZONTAL)
        scroll_y_show = Scrollbar(frame_show , orient=VERTICAL)
        style = ttk.Style()
        style.configure("mystyle.Treeview",background="White")
        self.student_table = ttk.Treeview(
            frame_show,
            columns=('ID','Name','Age','Averag','Phone number','Gender','Address'),
            xscrollcommand=scroll_x_show.set,
            yscrollcommand=scroll_y_show.set,
            )
        self.student_table.place(x=17,y=0,width=1180,height=550)
        scroll_x_show.pack(side=BOTTOM,fill=X)
        scroll_y_show.pack(side=LEFT,fill=Y)
        scroll_x_show.config(command=self.student_table.xview)
        scroll_y_show.config(command=self.student_table.yview)
        self.student_table['show'] = 'headings'
        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Age",text="Age")
        self.student_table.heading("Averag",text="Averag")
        self.student_table.heading("Phone number",text="Phone Number")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Address",text="Address")
        self.student_table.column("ID",width=60)
        self.student_table.column("Age",width=60)
        self.student_table.column("Averag",width=60)
        self.student_table.bind("<ButtonRelease-1>",self.modify)
        
        

    #! def to Add the student in student file  ----
        self.show_student()
    def add_student(self):
        open_file_student = open(r"{}/Database/student-data.txt".format(self.link),"a")
        if (self.id_var.get() != "" and self.name_var.get() != "" and self.age_var.get() != "" and self.averag_var.get() != "" and self.phone_var.get() != "" and self.gender_var.get() != "" and self.address_var.get() != ""):
            open_file_student.writelines(f"{self.id_var.get()}~{self.name_var.get()}~{self.age_var.get()}~{self.averag_var.get()}~{self.phone_var.get()}~{self.gender_var.get()}~{self.address_var.get()}\n")
        else:
            lbl_error_add_student = Label(
                self.frame_search,
                text="You can't add a student except by entering all information.\nif there is information missing , please enter ( unknown ) in the specified survey.",
                bg="White",
                fg="#EB0202",
                font=("Georgia",12)
                )
            lbl_error_add_student.place(x=300,y=60)
            self.frame_search.after(6000,lbl_error_add_student.place_forget)
        open_file_student.close()
        self.clear()
        self.show_student()

    #! def to Show the student in frame_show -----
    def show_student (self):
        Id = "";name ="";age = "";averag = "";phone = "";gender = "";address = "";conter = 0
        self.student_table.delete(*self.student_table.get_children())
        open_file_student_ = open(r"{}/Database/student-data.txt".format(self.link),"r")
        open_file_student_read = open_file_student_.readlines()
        open_file_student_.close()
        for row in open_file_student_read:
            if row != "\n":
                for liter in row:
                    if liter == "~":
                        conter += 1
                        pass
                    else:
                        if liter != "\n":
                            if conter == 0 :
                                Id += liter
                            elif conter == 1:
                                name += liter
                            elif conter == 2:
                                age += liter
                            elif conter == 3 :
                                averag += liter
                            elif conter == 4 :
                                phone += liter
                            elif conter == 5 :
                                gender += liter
                            elif conter == 6 :
                                address += liter
                        else:
                            pass
                else:
                    self.student_table.insert("",END,values=(Id,name,age,averag,phone,gender,address))
                    Id = "";name ="";age = "";averag = "";phone = "";gender = "";address = "";conter = 0
            else:
                pass

    #! def to delete the student with ID ------
    def delete(self):
        Id = ""
        conter_ = 0
        conter = 0
        open_file_student_ = open(r"{}/Database/student-data.txt".format(self.link),"r")
        open_file_student_read = open_file_student_.readlines()
        for num_line , line in enumerate(open_file_student_read,1):
            if line != "\n":
                for liter in line :
                    if liter == "~":
                        conter_ += 1
                    else:
                        if liter == "\n":
                            pass
                        elif conter_ == 0:
                            Id += liter 
                        else:
                            pass
                else:
                    if Id == self.dele_var.get():
                        conter = num_line
                        break
                    else:
                        conter_ = 0
                        Id = ""
        if conter != 0 :
            file_writ = open (r"{}/Database/student-data.txt".format(self.link),"w")
            for lien_num , line_ in enumerate(open_file_student_read):
                if lien_num != conter - 1 :
                    file_writ.write(line_)
            else:
                file_writ.close()
                lbl_error_add_student = Label(
                self.frame_search,
                text="Delete successfully ",
                bg="White",
                fg="#EB0202",
                font=("Georgia",12)
                )
                lbl_error_add_student.place(x=600,y=60)
                self.frame_search.after(3000,lbl_error_add_student.place_forget)
                self.show_student()
        else :
            lbl_error_add_student = Label(    
            self.frame_search,
            text=" Not Found ",
            bg="White",
            fg="#EB0202",
            font=("Georgia",12)
            )
        lbl_error_add_student.place(x=600,y=60)
        self.frame_search.after(4000,lbl_error_add_student.place_forget)
        self.clear()

    #! def to search in student-data and show it in frame_show -----
    def search_student (self):
        conter = 0 ; num = 0 ; Id = "" ; name = "" ; age = "" ; averag = "" ;phone = "" ; gender = "" ; address = ""
        open_file_student_ = open(r"{}/Database/student-data.txt".format(self.link),"r")
        open_file_student_read = open_file_student_.readlines()
        open_file_student_.close()
        for row in open_file_student_read:
            if row != "\n":
                for liter in row :
                    if liter == "~":
                        conter += 1
                    else:
                        if liter != "\n":
                            if conter == 0 :
                                Id += liter
                            elif conter == 1:
                                name += liter
                            elif conter == 2:
                                age += liter
                            elif conter == 3 :
                                averag += liter
                            elif conter == 4 :
                                phone += liter
                            elif conter == 5 :
                                gender += liter
                            elif conter == 6 :
                                address += liter
                        else:
                            pass
                else:
                    if self.search_id_name_phone.get() == "ID":
                        if Id == self.search.get():
                            self.student_table.delete(*self.student_table.get_children())
                            self.student_table.insert("",END,values=(Id,name,age,averag,phone,gender,address))
                            num = 2 
                            break
                        else:
                            conter = 0 ; Id = "" ; name = "" ; age = "" ; averag = "" ;phone = "" ;gender = "" ;address = ""
                    if self.search_id_name_phone.get() == "name":
                        if name == self.search.get():
                            self.student_table.delete(*self.student_table.get_children())
                            self.student_table.insert("",END,values=(Id,name,age,averag,phone,gender,address))
                            num = 2 
                            break
                        else:
                            conter = 0 ; Id = "" ; name = "" ; age = "" ; averag = "" ;phone = "" ;gender = "" ;address = ""
                    if self.search_id_name_phone.get() == "phone":
                        if phone == self.search.get():
                            self.student_table.delete(*self.student_table.get_children())
                            self.student_table.insert("",END,values=(Id,name,age,averag,phone,gender,address))
                            num = 2
                            break
                        else:
                            conter = 0 ; Id = "" ; name = "" ; age = "" ; averag = "" ;phone = "" ;gender = "" ;address = ""
            else :
                pass
        else:
            if num < 1 :
                lbl_error_add_student = Label(    
                    self.frame_search,
                    text=" Not Found ",
                    bg="White",
                    fg="#EB0202",
                    font=("Georgia",12)
                )
                lbl_error_add_student.place(x=600,y=60)
                self.frame_search.after(4000,lbl_error_add_student.place_forget)

    #! def to clear the Entrys ---- 
    def clear(self):
        self.id_var.set('')
        self.name_var.set('')
        self.age_var.set('')
        self.phone_var.set('')
        self.gender_var.set('')
        self.averag_var.set('')
        self.dele_var.set('')
        self.address_var.set('')
        self.search_id_name_phone.set('')
        self.search.set('')
        self.show_student()

    #! def to modify the data --------
    def modify(self,ver):
        cursor_row  = self.student_table.focus()
        conter = self.student_table.item(cursor_row)
        row = conter['values']
        self.id_var.set(row[0])
        self.name_var.set(row[1])
        self.age_var.set(row[2])
        self.averag_var.set(row[3])
        self.phone_var.set(row[4])
        self.gender_var.set(row[5])
        self.address_var.set(row[6])

    #! def to update the data -----
    def update (self ):
        conter = 0 ; Id = "" ; name = "" ; age = "" ; averag = "" ;phone = "" ; gender = "" ; address = ""
        open_file_student_ = open(r"{}/Database/student-data.txt".format(self.link),"r")
        open_file_student_read = open_file_student_.readlines()
        open_file_student_.close()
        for row in open_file_student_read:
            if row != "\n":
                for liter in row :
                    if liter == "~":
                        conter += 1
                    else:
                        if liter != "\n":
                            if conter == 0 :
                                Id += liter
                            elif conter == 1:
                                name += liter
                            elif conter == 2:
                                age += liter
                            elif conter == 3 :
                                averag += liter
                            elif conter == 4 :
                                phone += liter
                            elif conter == 5 :
                                gender += liter
                            elif conter == 6 :
                                address += liter
                        else:
                            pass
                else:
                    if (Id == self.id_var.get()) or (name == self.name_var.get()):
                        index = open_file_student_read.index(f"{Id}~{name}~{age}~{averag}~{phone}~{gender}~{address}\n")
                        open_file_student_read[index] = (f"{self.id_var.get()}~{self.name_var.get()}~{self.age_var.get()}~{self.averag_var.get()}~{self.phone_var.get()}~{self.gender_var.get()}~{self.address_var.get()}\n")
                        open_file_student__ = open(r"{}/Database/student-data.txt".format(self.link),"w")
                        open_file_student_write = open_file_student__.writelines(open_file_student_read)
                        open_file_student__.close()
                        self.show_student()
                        self.clear()
                        break
                    else :
                        conter = 0 ; Id = "" ; name = "" ; age = "" ; averag = "" ;phone = "" ; gender = "" ; address = ""
            else:
                pass
        else:
            self.clear()

    #! About My -----------
    def About (self):
        self.wind_2 =Toplevel(self.wind)
        self.wind_2.geometry('400x400')
        self.wind_2.resizable(False,False)
        self.wind_2.title("About The programmer")
        frame_wind_2 = Frame(self.wind_2,bg="#34495E")
        frame_wind_2.config(width=390,height=390)
        
        lbal10 = Label(frame_wind_2,text="------------------2023-03-90 ; 06:22PM--------------------",bg="#34495E",fg="#EEE")

        lbal6 = Label(frame_wind_2,text="______________",bg="#34495E",fg="#EEE")
        lbal7 = Label(frame_wind_2,text="•GitHub.com  :  @Mohaned2023",bg="#34495E",fg="#EEE",font=("Century",11))

        lbal5 = Label(frame_wind_2,text="____________",bg="#34495E",fg="#EEE")
        lbal8 = Label(frame_wind_2,text="•Instagram   :  @mr.lxzl",bg="#34495E",fg="#EEE",font=("Century",11))

        lbal4 = Label(frame_wind_2,text="_________",bg="#34495E",fg="#EEE")
        lbal9 = Label(frame_wind_2,text="•Twitter :  @MrX48915521",bg="#34495E",fg="#EEE",font=("Century",11))

        lbal3 = Label(frame_wind_2,text="___________________________________________________________",bg="#34495E",fg="#EEE")
        lbal = Label(frame_wind_2,text="•Programmed by Mohaned Sherhan.",bg="#34495E",fg="#EEE",font=("Century",15))
        labl2 = Label(frame_wind_2,
        text="This project is a school management system,\nIt works on: \n1- Adding students by name, ID, Address,\nAge, Phone Number, Averag and Gender,\n2- Saving data in an internal file type Text,\n3- The program modulates the student's data ,\n4- searches by Name, ID and Phone Number,\nAs well as works on deletion by name,and\nthis is the work of the program in a nutshell.",
        bg="#34495E",fg="#EEE",font=("Century",11)
        )
        lbal10.place(x=0,y=350)
        lbal9.place(x=10,y=315)
        lbal8.place(x=10 , y=285)
        lbal7.place(x=10,y=255)
        lbal6.place(x=10 , y=260)
        lbal5.place(x=10 , y=290)
        lbal4.place(x=10 , y=320)
        lbal3.place(x=0 , y=45)
        labl2.place(x=30,y=70)
        lbal.place(x=20,y=30)
        frame_wind_2.place(x=5,y=5)

root = Tk()
ob = Student(root)
root.mainloop()