#import Library
from tkinter import *
import tkinter as tk
from tkinter import ttk
from csv import DictWriter
from csv import DictReader
from tkinter import messagebox
import csv
import  numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

#Define Root
root=tk.Tk()
root.title('Life Blood Centre')

#Photos For Background
bg1=tk.PhotoImage(file=r"./Images/title_3_1920x150.png")
ref=tk.PhotoImage(file=r"./Images/refresh_50x50.png")
logo=PhotoImage(file=r"./Images/logo.png")
bg2=tk.PhotoImage(file=r"./Images/main_1600x700.png")
loginPageimg=tk.PhotoImage(file=r"./Images/background1_1920x930.png")
p1=PhotoImage(file=r'./Images/logo.png')
bgloginimg=tk.PhotoImage(file=r"./Images/background2_3_1600x700.png")
bgsignupimg=tk.PhotoImage(file=r"./Images/background3_1_1600x700.png")
useropbg=tk.PhotoImage(file=r"./Images/background4.2_1600x700.png")
userop1bg=tk.PhotoImage(file=r"./Images/background4_1600x700.png")
admin1bg=tk.PhotoImage(file=r"./Images/ADMIN11_1600x700.png")
req_bg_img=tk.PhotoImage(file=r"./Images/REQ_BLOOD_1600x700.png")
contactusimg=tk.PhotoImage(file=r"./Images/CONTACTUS_1600x700.png")
rulesimg=tk.PhotoImage(file=r"./Images/RULES_1600x700.png")
adminanabg=tk.PhotoImage(file=r"./Images/admin_analysis_1600x700.png")
req_bg_img1=tk.PhotoImage(file=r"./Images/1234567890_1600x700.png")

#For Full Screen
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.geometry("%dx%d" %(width,height))

#For Icon Of our application
root.iconphoto(False,p1)

#fram1 like  fixed
Frame1 = tk.Frame(root)
Frame1.place(x=0,y=0,height=150,width=1920)

#frame2 Main Frame like:Editor 
Frame2 = tk.Frame(root)
Frame2.place(x=0,y=150,height=930,width=1920)
# Frame2.grid(row=0)

#Title OF Our Application
title1=Label(Frame1,text='Life Blood Centre',fg='#F73C3C')
title1.configure(font=("Garamond",45,"bold"))
title1.place(x=700,y=5,width=700,height=80)

#Background Image For Main Frame2
Label1 = tk.Label(Frame2)
Label1.place(x=-170,y=-170,height=980, width=1920)
Label1.configure(image=bg2)

#Background Image For Fixed Frame1

back1=tk.Label(Frame1)
back1.place(x=0,y=0,width=1920,height=150)
back1.configure(image=bg1)


#Photo Logo In Fixed Frame1
logo1=tk.Label(Frame1)
logo1.place(x=0,y=0,height=150, width=130)
logo1.configure(image=logo)

#Home Page For Refresh Button
def home():
    Label1 = tk.Label(Frame2)
    Label1.place(x=-170,y=-170,height=980, width=1920)
    Label1.configure(image=bg2)
    
#For Refresh Button And its Placement
refresh=tk.Button(Frame1,command=lambda:home())
refresh.config(image=ref)
refresh.place(x=550,y=95,width=45,height=45)
refresh.configure(relief='flat')

#Main login Fuction Of Fram1 Login/Signup Button
def login():

    for widget in Frame2.winfo_children():
        widget.destroy()
    bgforlogin = tk.Label(Frame2)
    bgforlogin.place(x=-270,y=-100,height=980, width=1920)
    bgforlogin.configure(image=loginPageimg)
        
    #This Login Fuction Is For Login Button in Inner Button Of Login/Signup
    def loginfunc():
        for widget in Frame2.winfo_children():
            widget.destroy()

        bglogin=Label(Frame2)
        bglogin.place(x=-200,y=-160,height=980,width=1920)
        bglogin.configure(image=bgloginimg)

        # emaill=tk.Label(Frame2,text='Email :')
        # emaill.grid(row=0, column=0,sticky=tk.W)

        # passwordl=tk.Label(Frame2,text='Password :')
        # passwordl.grid(row=1,column=0,sticky=tk.W)

        emaill_var=tk.StringVar()
        emaill_entrybox=tk.Entry(Frame2,width=20 , textvariable=emaill_var)
        emaill_entrybox.place(x=977,y=160,height=37,width=512)
        emaill_entrybox.configure(background='white',relief='flat',font=("times",15,"bold"),cursor="ibeam #ffffff")
        emaill_entrybox.focus()
        
        passwordl_var=tk.StringVar()
        passwordl_entrybox=tk.Entry(Frame2,width=20 , textvariable=passwordl_var)
        passwordl_entrybox.configure(background='white',show="*",relief='flat',font=("times",15,"bold"),cursor="ibeam #ffffff")
        passwordl_entrybox.place(x=977,y=263,height=37,width=512)

        #This Action Fuction Is For Press Login And check the email and password
        def action1():
            email = emaill_var.get()
            password = passwordl_var.get()

            if email=="" or password=="":
                messagebox.showwarning("Error","Enter Email Or PassWord")
                return None
            else:   
                f = open('records.csv', 'r')
                ok = False
                with f:

                    reader = DictReader(f)

                    for row in reader:
                        if row['Email'] == email and row['Password'] == password:
                            user_options(row['Name'], row['Email'], row['Gender'], row['Age'], row['Phone No'],row['Blood Group'], row['City'])
                            ok = True
                    if not ok:
                        messagebox.showwarning("Warning","Username or Password Incorrect !!")
                        return None

        submit_button=tk.Button(Frame2,text="Login" ,bg="#FFFFFF",command=action1)
        submit_button.place(x=1145,y=378,height=55,width=180)
        submit_button.configure(font=(20),relief="flat")

        loginback=tk.Button(Frame2,text="Back",bg="#FFFFFF",command=lambda:login())
        loginback.place(x=1200,y=550,height=40,width=180)
        loginback.configure(font=("times",25),relief="flat")

    login1=tk.Button(Frame2,text="LOG IN",bg="#7C6E73",command=loginfunc,fg='#FDFDFD')
    login1.place(x=1047,y=175,width=442,height=85)
    login1.configure(font=("times",30),relief="flat")

    #This signup Fuction Is For Sign up Button in Inner Button Of Login/Signup
    def signupfunc():
        for widget in Frame2.winfo_children():
            widget.destroy()

        bgsignup=Label(Frame2)
        bgsignup.place(x=-170,y=-160,height=980,width=1920)
        bgsignup.configure(image=bgsignupimg)

        # name=tk.Label(Frame2,text='Name :')
        # name.grid(row=0,column=0,sticky=tk.W)

        name_var=tk.StringVar()
        name_entrybox=tk.Entry(Frame2,width=20 , textvariable=name_var)
        name_entrybox.focus()
        name_entrybox.place(x=311,y=160,width=393,height=33)
        name_entrybox.configure(background='white',relief='flat',font=("times",15),cursor="ibeam #ffffff")

        # emails=tk.Label(Frame2,text='Email :')
        # emails.grid(row=1, column=0,sticky=tk.W)

        emails_var=tk.StringVar()
        emails_entrybox=tk.Entry(Frame2,width=20 , textvariable=emails_var)
        emails_entrybox.place(x=311,y=232,width=393,height=33)
        emails_entrybox.configure(background='white',relief='flat',font=("times",15),cursor="ibeam #ffffff")

        # passwords=tk.Label(Frame2,text='Password :')
        # passwords.grid(row=2,column=0,sticky=tk.W)

        passwords_var=tk.StringVar()
        passwords_entrybox=tk.Entry(Frame2,width=20 , textvariable=passwords_var)
        passwords_entrybox.place(x=311,y=308,width=393,height=33)
        passwords_entrybox.configure(background='white',show="*",relief='flat',font=("times",15),cursor="ibeam #ffffff")

        # phoneno=tk.Label(Frame2,text='Phone No :')
        # phoneno.grid(row=3,column=0,sticky=tk.W)

        phoneno_var=tk.StringVar()
        phoneno_entrybox=tk.Entry(Frame2,width=20 , textvariable=phoneno_var)
        phoneno_entrybox.place(x=913,y=308,width=315,height=33)
        phoneno_entrybox.configure(background='white',relief='flat',font=("times",15),cursor="ibeam #ffffff")

        # age=tk.Label(Frame2,text='Age :')
        # age.grid(row=4,column=0,sticky=tk.W)

        age_var=tk.StringVar()
        age_spinbox=tk.Spinbox(Frame2,width=18 ,from_=0,to=150, textvariable=age_var)
        age_spinbox.place(x=913,y=384,width=315,height=33)
        age_spinbox.configure(background='white',relief='flat',font=("times",15),cursor="ibeam #ffffff")

        # bloodg=tk.Label(Frame2,text='Blood Group')
        # bloodg.grid(row=5,column=0,sticky=tk.W)

        bloodg_var=tk.StringVar()
        bloodg_combobox=ttk.Combobox(Frame2,width=16,textvariable=bloodg_var,state='readonly')
        bloodg_combobox['values']=('A+','A-','B+','B-','AB+','AB-','O+','O-')
        bloodg_combobox.current(0)
        bloodg_combobox.place(x=311,y=384,width=393,height=33)
        bloodg_combobox.configure(font=("times",14))
        # bloodg_combobox.configure(background='white',relief='flat',font=("times",15),cursor="ibeam #ffffff")

        # gender=tk.Label(Frame2,text='Gender :')
        # gender.grid(row=6,column=0,sticky=tk.W)

        gender_var=tk.StringVar()
        gender_combobox=ttk.Combobox(Frame2,width=16,textvariable=gender_var,state='readonly')
        gender_combobox['values']=('Male','Female' ,'Others ')
        gender_combobox.current(0)
        gender_combobox.place(x=905,y=160,width=325,height=33)
        gender_combobox.configure(font=("times",14))
        # gender_combobox.configure(background='white',relief='flat',font=("times",15),cursor="ibeam #ffffff")

        # city=tk.Label(Frame2,text='City :')
        # city.grid(row=7,column=0,sticky=tk.W)

        city_var=tk.StringVar()
        city_combobox=ttk.Combobox(Frame2,width=16,textvariable=city_var,state='readonly')
        city_combobox['values']=('Rajkot','Surat' ,'Junagadh','Ahemdabad','Vadodara')
        city_combobox.current(0)
        city_combobox.place(x=905,y=232,width=325,height=33)
        city_combobox.configure(font=("times",14))
        # city_combobox.configure(background='white',relief='flat',font=("times",15),cursor="ibeam #ffffff")

        gender_combobox.set(" ")
        city_combobox.set(" ")
        bloodg_combobox.set(" ")
        name_entrybox.delete(0,tk.END)
        age_spinbox.delete(0,tk.END)
        emails_entrybox.delete(0,tk.END)
        passwords_entrybox.delete(0,tk.END)
        phoneno_entrybox.delete(0,tk.END)

        #This Action Function For Fill Form And Signup Button Press then this fired And Save all information in CSV File
        def action2():
            name=name_var.get()
            email=emails_var.get()
            password=passwords_var.get()
            phoneno=phoneno_var.get()
            age=age_var.get()
            bloodg=bloodg_var.get()
            gender=gender_var.get()
            city=city_var.get()

            if len(name)==0:
                messagebox.showerror("Error","Enter Your Name")
                return None
            if len(email)==0:
                messagebox.showerror("Error","Enter Your Email")
                return None
            
            if len(password)==0:
                messagebox.showwarning("Warning","Enter Password")
                return None
            #For Password Conditions
            length = lower = upper = digit = False
            if len(password)== 6:
                length = True
            for letter in password:
                if letter.islower():
                    lower = True
                elif letter.isupper():
                    upper = True
                elif letter.isdigit():
                    digit = True
            
            if length and lower and upper and digit:
                pass
            else:
                messagebox.showerror("Password","Password Must Contain Atleast One UpperCase , LowerCase Letter and Digit And Password Length Must Be 6 Character")
                return None

            if bloodg_combobox==0:
                messagebox.showerror("Error","Enter Your Blood Group")
                return None
            if len(gender)==0:
                messagebox.showerror("Error","Enter Your Gender")
                return None
            if len(city)==0:
                messagebox.showerror("Error","Enter Your City")
                return None
            if len(phoneno)==0:
                messagebox.showerror("Error","Enter Your Phone Number")
                return None    
            if(phoneno.isdecimal()==False):
                messagebox.showwarning("Phone Number Error","Phone Number Only Contain Digits Re-Enter Number")
                return None
            if(len(phoneno)!=10):
                messagebox.showwarning("Phone Number Error","Phone Number Must be 10 digits Re-Enter Number")
                return None
            if len(age)==0:
                messagebox.showerror("Error","Enter Your Age")
                return None

            with open('records.csv','a') as f:
                dict_writer=DictWriter(f,fieldnames=['Name','Email','Password','Phone No','Age','Blood Group','Gender','City'])
                if os.stat('records.csv').st_size==0:
                    dict_writer.writeheader()
                else:
                    dict_writer.writerow({
                    'Name' : name,
                    'Email' :email,
                    'Password':password,
                    'Phone No':phoneno,
                    'Age' : age,
                    'Blood Group':bloodg,
                    'Gender':gender,
                    'City':city   
                    })

                    name_entrybox.delete(0,tk.END)
                    age_spinbox.delete(0,tk.END)
                    emails_entrybox.delete(0,tk.END)
                    passwords_entrybox.delete(0,tk.END)
                    phoneno_entrybox.delete(0,tk.END)
                    gender_combobox.set(" ")
                    city_combobox.set(" ")
                    bloodg_combobox.set(" ")

            messagebox.showinfo("Information","Your Data Saved Sucessfully !")
            return loginfunc()

        signup_button=tk.Button(Frame2,text="Sign Up" ,command=action2)
        signup_button.place(x=557,y=487,width=228,height=53)
        signup_button.configure(font=("times",20),relief='flat',bg="#FFFFFF")

        signupback=tk.Button(Frame2,text="Back",bg="#FFFFFF",command=lambda:login())
        signupback.place(x=1200,y=550,height=40,width=180)
        signupback.configure(font=("times",25),relief="flat")

    signup1=tk.Button(Frame2,text="SIGN UP",bg="#7C6E73",fg="#FDFDFD",command=signupfunc)
    signup1.place(x=1047,y=420,width=442,height=85)
    signup1.configure(font=("times",30),relief="flat")

loginsignup=tk.Button(Frame1,text='LogIn/SignUp',command=login)
loginsignup.place(x=650,y=95,width=150,height=45)
loginsignup.configure(font=(15),relief='flat')

def admin1():
    for widget in Frame2.winfo_children():
        widget.destroy()
    
    def adminaction():
        Password = "Admin9"
        Username = "Admin"
        uname=username_var.get()
        password=password_var.get()

        def view_donners():
            for widget in Frame2.winfo_children():
                widget.destroy()

            scrollbarx = ttk.Scrollbar(Frame2, orient=HORIZONTAL)
            scrollbary = ttk.Scrollbar(Frame2, orient=VERTICAL)
            tree = ttk.Treeview(Frame2,
                                columns=("Email", "Name", "Phone No", "Age", "Blood Group", "Gender", "City"),
                                height=400, selectmode="extended",
                                yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            tree.place(x=0,y=200,width=1000)

            style=ttk.Style()
            style.configure("Treeview", rowheight=35)

            tree.heading('Email', text="Email", anchor=W)
            tree.heading('Name', text="Name", anchor=W)
            tree.heading('Phone No', text="Phone No", anchor=W)
            tree.heading('Age', text="Age", anchor=W)
            tree.heading('Blood Group', text="Blood Group", anchor=W)
            tree.heading('Gender', text="Gender", anchor=W)
            tree.heading('City', text="City", anchor=W)

            tree.column('#0', stretch=YES, minwidth=0, width=0)
            tree.column('#1', stretch=YES, minwidth=0, width=150)
            tree.column('#2', stretch=YES, minwidth=0, width=150)
            tree.column('#3', stretch=YES, minwidth=0, width=150)
            tree.column('#4', stretch=YES, minwidth=0, width=150)
            tree.column('#5', stretch=YES, minwidth=0, width=150)
            tree.column('#6', stretch=YES, minwidth=0, width=150)
            tree.column('#7', stretch=YES, minwidth=0, width=150)
            tree.place(x=-50,y=0,width=1600,height=700)
            with open('activedoners.csv') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    email = row['Email']
                    name = row['Name']
                    age = row['Age']
                    phno = row['Phone No']
                    gender = row['Gender']
                    city = row['City']
                    bloodg = row['Blood Group']
                    tree.insert("", 0, values=(email, name, phno, age, bloodg, gender, city))

            viewback1=tk.Button(Frame2,text="Back",bg="#FFFFFF",command=lambda:adminaction())
            viewback1.place(x=1200,y=550,height=40,width=180)
            viewback1.configure(font=("times",25),relief="flat")

        def view_history():
            for widget in Frame2.winfo_children():
                widget.destroy()

            scrollbarx = Scrollbar(Frame2, orient=HORIZONTAL)
            scrollbary = Scrollbar(Frame2, orient=VERTICAL)
            tree = ttk.Treeview(Frame2,
                                columns=("Name","Email", "Aname" ,"Aemail","Aphone No","Aage" ,"Agender"),
                                height=400, selectmode="extended",
                                yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)

            style=ttk.Style()
            style.configure("Treeview", rowheight=35, rowwidth=20)

            tree.heading('Name', text="Name", anchor=W)
            tree.heading('Email', text="Email", anchor=W)
            tree.heading('Aname', text="Accepter name", anchor=W)
            tree.heading('Aemail', text="Accepter email", anchor=W)
            tree.heading('Aphone No', text="Accepter phone No", anchor=W)
            tree.heading('Aage', text="Accepter age", anchor=W)
            tree.heading('Agender', text="Accepter gender", anchor=W)


            tree.column('#0', stretch=YES, minwidth=0, width=0)
            tree.column('#1', stretch=YES, minwidth=0, width=160)
            tree.column('#2', stretch=YES, minwidth=0, width=160)
            tree.column('#3', stretch=YES, minwidth=0, width=160)
            tree.column('#4', stretch=YES, minwidth=0, width=160)
            tree.column('#5', stretch=YES, minwidth=0, width=160)
            tree.column('#6', stretch=YES, minwidth=0, width=160)

            tree.place(x=-40,y=0,width=1600,height=700)
            with open('history.csv') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    email = row['Email']
                    name = row['Name']
                    aemail = row['Aemail']
                    aname = row['Aname']
                    age = row['Aage']
                    phno = row['Aphone No']
                    gender = row['Agender']

                    tree.insert("", 0, values=(name, email,aname,aemail,phno, age, gender))

            viewback3=tk.Button(Frame2,text="Back",bg="#FFFFFF",command=lambda:adminaction())
            viewback3.place(x=1200,y=550,height=40,width=180)
            viewback3.configure(font=("times",25),relief="flat")

        def view_analysis():
            for widget in Frame2.winfo_children():
                widget.destroy()
            
            def present_blood():
                for widget in Frame2.winfo_children():
                    widget.destroy()
                with open('activedoners.csv', 'r') as f:
                    y = np.array([0, 0, 0, 0, 0, 0, 0, 0])
                    reader = DictReader(f)
                    for row in reader:
                        if row['Blood Group'] == "A+":
                            y[0] += 1
                        elif row['Blood Group'] == "A-":
                            y[1] += 1
                        elif row['Blood Group'] == "B+":
                            y[2] += 1
                        elif row['Blood Group'] == "B-":
                            y[3] += 1
                        elif row['Blood Group'] == "O+":
                            y[4] += 1
                        elif row['Blood Group'] == "O-":
                            y[5] += 1
                        elif row['Blood Group'] == "AB+":
                            y[6] += 1
                        elif row['Blood Group'] == "AB-":
                            y[7] += 1

                    fig = Figure(figsize=(1,1), dpi=100)
                    x = np.array(["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
                    groups = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

                    plot1 = fig.add_subplot(1, 2, 1)
                    plot1.bar(x, y, width=0.5)

                    for i, v in enumerate(y):
                        plot1.text(i - 0.10, v + 0.015, str(v))
                    plot1.set_title('Blood Storage Chart')
                    plot1.set_xlabel('Blood Group')
                    plot1.set_ylabel('Available Storage')

                    plot2 = fig.add_subplot(1, 2, 2)
                    plot2.pie(y, wedgeprops=dict(width=0.5), startangle=-40, labels=groups)
                    plot2.legend(title="blood groups", loc=5, bbox_to_anchor=(0.80, 0.25, 0.5, 0.5))
                    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
                    kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

                    plot2.set_title('Blood Storage Pie Chart')
                    

                    canvas = FigureCanvasTkAgg(fig, master=Frame2)  # A tk.DrawingArea.
                    canvas.draw()
                    canvas.get_tk_widget().place(x=0,y=200,width=700,height=600)

                    toolbar = NavigationToolbar2Tk(canvas, Frame2)
                    toolbar.update()
                    canvas.get_tk_widget().place(x=-50,y=-10,width=1580,height=700)

                    viewback2=tk.Button(Frame2,text="Back",bg="#FFFFFF",command=view_analysis)
                    viewback2.place(x=1200,y=550,height=40,width=180)
                    viewback2.configure(font=("times",25),relief="flat")

            def blood_ava_city():
                with open('activedoners.csv', 'r') as f:
                    y1 = np.array([0, 0, 0, 0, 0, 0, 0, 0])
                    y2 = np.array([0, 0, 0, 0, 0, 0, 0, 0])
                    y3 = np.array([0, 0, 0, 0, 0, 0, 0, 0])
                    y4 = np.array([0, 0, 0, 0, 0, 0, 0, 0])
                    y5 = np.array([0, 0, 0, 0, 0, 0, 0, 0])
                    reader = DictReader(f)
                    for row in reader:
                        if row['Blood Group'] == "A+" and row['City'] == "Rajkot":
                            y1[0] += 1
                        elif row['Blood Group'] == "A-" and row['City'] == "Rajkot":
                            y1[1] += 1
                        elif row['Blood Group'] == "B+" and row['City'] == "Rajkot":
                            y1[2] += 1
                        elif row['Blood Group'] == "B-" and row['City'] == "Rajkot":
                            y1[3] += 1
                        elif row['Blood Group'] == "O+" and row['City'] == "Rajkot":
                            y1[4] += 1
                        elif row['Blood Group'] == "O-" and row['City'] == "Rajkot":
                            y1[5] += 1
                        elif row['Blood Group'] == "AB+" and row['City'] == "Rajkot":
                            y1[6] += 1
                        elif row['Blood Group'] == "AB-" and row['City'] == "Rajkot":
                            y1[7] += 1
                        elif row['Blood Group'] == "A+" and row['City'] == "Surat":
                            y2[0] += 1
                        elif row['Blood Group'] == "A-" and row['City'] == "Surat":
                            y2[1] += 1
                        elif row['Blood Group'] == "B+" and row['City'] == "Surat":
                            y2[2] += 1
                        elif row['Blood Group'] == "B-" and row['City'] == "Surat":
                            y2[3] += 1
                        elif row['Blood Group'] == "O+" and row['City'] == "Surat":
                            y2[4] += 1
                        elif row['Blood Group'] == "O-" and row['City'] == "Surat":
                            y2[5] += 1
                        elif row['Blood Group'] == "AB+" and row['City'] == "Surat":
                            y2[6] += 1
                        elif row['Blood Group'] == "AB-" and row['City'] == "Surat":
                            y2[7] += 1
                        elif row['Blood Group'] == "A+" and row['City'] == "Junagadh":
                            y3[0] += 1
                        elif row['Blood Group'] == "A-" and row['City'] == "Junagadh":
                            y3[1] += 1
                        elif row['Blood Group'] == "B+" and row['City'] == "Junagadh":
                            y3[2] += 1
                        elif row['Blood Group'] == "B-" and row['City'] == "Junagadh":
                            y3[3] += 1
                        elif row['Blood Group'] == "O+" and row['City'] == "Junagadh":
                            y3[4] += 1
                        elif row['Blood Group'] == "O-" and row['City'] == "Junagadh":
                            y3[5] += 1
                        elif row['Blood Group'] == "AB+" and row['City'] == "Junagadh":
                            y3[6] += 1
                        elif row['Blood Group'] == "AB-" and row['City'] == "Junagadh":
                            y3[7] += 1
                        elif row['Blood Group'] == "A+" and row['City'] == "Ahemdabad":
                            y4[0] += 1
                        elif row['Blood Group'] == "A-" and row['City'] == "Ahemdabad":
                            y4[1] += 1
                        elif row['Blood Group'] == "B+" and row['City'] == "Ahemdabad":
                            y4[2] += 1
                        elif row['Blood Group'] == "B-" and row['City'] == "Ahemdabad":
                            y4[3] += 1
                        elif row['Blood Group'] == "O+" and row['City'] == "Ahemdabad":
                            y4[4] += 1
                        elif row['Blood Group'] == "O-" and row['City'] == "Ahemdabad":
                            y4[5] += 1
                        elif row['Blood Group'] == "AB+" and row['City'] == "Ahemdabad":
                            y4[6] += 1
                        elif row['Blood Group'] == "AB-" and row['City'] == "Ahemdabad":
                            y4[7] += 1
                        elif row['Blood Group'] == "A+" and row['City'] == "Vadodara":
                            y5[0] += 1
                        elif row['Blood Group'] == "A-" and row['City'] == "Vadodara":
                            y5[1] += 1
                        elif row['Blood Group'] == "B+" and row['City'] == "Vadodara":
                            y5[2] += 1
                        elif row['Blood Group'] == "B-" and row['City'] == "Vadodara":
                            y5[3] += 1
                        elif row['Blood Group'] == "O+" and row['City'] == "Vadodara":
                            y5[4] += 1
                        elif row['Blood Group'] == "O-" and row['City'] == "Vadodara":
                            y5[5] += 1
                        elif row['Blood Group'] == "AB+" and row['City'] == "Vadodara":
                            y5[6] += 1
                        elif row['Blood Group'] == "AB-" and row['City'] == "Vadodara":
                            y5[7] += 1

                    fig = Figure(figsize=(15, 15), dpi=100)
                    groups = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
                    plot1 = fig.add_subplot(2, 3, 1)
                    plot1.pie(y1, wedgeprops=dict(width=0.5), startangle=-40, labels=groups)
                    plot1.legend(title="blood groups", loc=5, bbox_to_anchor=(0.90, 0.25, 0.5, 0.5))
                    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
                    kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")
                    
                    plot1.set_title('Rajkot',fontsize=18)

                    plot2 = fig.add_subplot(2, 3, 2)
                    plot2.pie(y2, wedgeprops=dict(width=0.5), startangle=-40, labels=groups)
                    plot2.legend(title="blood groups", loc=5, bbox_to_anchor=(0.90, 0.25, 0.5, 0.5))
                    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
                    kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

                    plot2.set_title('Surat',fontsize=18)    
                
                    plot3 = fig.add_subplot(2, 3, 3)
                    plot3.pie(y3, wedgeprops=dict(width=0.5), startangle=-40, labels=groups)
                    plot3.legend(title="blood groups",loc=5, bbox_to_anchor=(0.90, 0.25, 0.5, 0.5))
                    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
                    kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

                    plot3.set_title('Junagadh',fontsize=18)

                    plot4 = fig.add_subplot(2, 3, 4)
                    plot4.pie(y4, wedgeprops=dict(width=0.5), startangle=-40, labels=groups)
                    plot4.legend(title="blood groups", loc=5, bbox_to_anchor=(0.90, 0.25, 0.5, 0.5))
                    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
                    kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

                    plot4.set_title('Ahemdabad',fontsize=18)

                    plot5 = fig.add_subplot(2, 3, 5)
                    plot5.pie(y5, wedgeprops=dict(width=0.5), startangle=-40, labels=groups)
                    plot5.legend(title="blood groups", loc=5, bbox_to_anchor=(0.90, 0.25, 0.5, 0.5))
                    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
                    kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

                    plot5.set_title('Vadodara',fontsize=18)

                    canvas = FigureCanvasTkAgg(fig, master=Frame2)  # A tk.DrawingArea.
                    canvas.draw()
                    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

                    toolbar = NavigationToolbar2Tk(canvas, Frame2)
                    toolbar.update()
                    canvas.get_tk_widget().place(x=-50,y=-10,width=1580,height=700)

                    viewback4=tk.Button(Frame2,text="Back",bg="#FFFFFF",command=lambda:view_analysis())
                    viewback4.place(x=1200,y=550,height=40,width=180)
                    viewback4.configure(font=("times",25),relief="flat")

            def donner_history():
                for widget in Frame2.winfo_children():
                    widget.destroy()
                
                fig = Figure(figsize=(1, 1), dpi=100)
                with open("history.csv", 'r') as f20:
                    dict1 = {}
                    name = []
                    reader1 = DictReader(f20)
                    for row in reader1:
                        if row['Email'] in dict1.keys():
                            dict1[row['Email']] += 1
                        else:
                            dict1[row['Email']] = 1
                            name.append(row['Name'])


                    values = dict1.values()
                    plot3 = fig.add_subplot(1, 1, 1)
                    plot3.bar(name, values, width=0.3)
                    
                    for i, v in enumerate(values):
                        plot3.text(i - 0.10, v + 0.015, str(v))
                    plot3.set_title('Donation Chart',fontsize=30)
                    plot3.set_xlabel('Donor Name')
                    plot3.set_ylabel('No. Of Donation')

                    f20.close()

                    canvas = FigureCanvasTkAgg(fig, master=Frame2)  # A tk.DrawingArea.
                    canvas.draw()
                    canvas.get_tk_widget().place(x=0,y=150,width=700,height=600)

                    toolbar = NavigationToolbar2Tk(canvas, Frame2)
                    toolbar.update()
                    canvas.get_tk_widget().place(x=-70,y=-30,width=1580,height=700)

                    viewback5=tk.Button(Frame2,text="Back",bg="#FFFFFF",command=lambda:view_analysis())
                    viewback5.place(x=1300,y=550,height=40,width=180)
                    viewback5.configure(font=("times",25),relief="flat")

            adminana=tk.Label(Frame2)
            adminana.place(x=-150,y=-170,height=980, width=1920)
            adminana.configure(image=adminanabg)

            present_blood_chart = tk.Button(Frame2, text="Available Blood", command = present_blood , bg="#CDC068")
            present_blood_chart.place(x=200, y=200, height=50, width=550)
            present_blood_chart.configure(font=("times", 30), relief="flat")

            city_blood_chart = tk.Button(Frame2, text="Available Blood According to City", command = blood_ava_city,bg="#CDC068")
            city_blood_chart.place(x=200, y=310, height=50, width=550)
            city_blood_chart.configure(font=("times", 30), relief="flat")

            Donner_history = tk.Button(Frame2, text="Donners Donation History", command = donner_history,bg="#CDC068")
            Donner_history.place(x=200, y=420, height=50, width=550)
            Donner_history.configure(font=("times", 30), relief="flat")

            viewback6=tk.Button(Frame2,text="Back",bg="#FFFFFF",command=lambda:adminaction())
            viewback6.place(x=1200,y=550,height=40,width=180)
            viewback6.configure(font=("times",25),relief="flat")

        if uname=="" or password=="":
            messagebox.showwarning("Warning","Enter Username or Password")
            return None

        elif password==Password and uname==Username:
            for widget in Frame2.winfo_children():
                widget.destroy()

            adminbg2=Label(Frame2)
            adminbg2.place(x=-210,y=-140,height=980, width=1920)
            adminbg2.configure(image=adminanabg)

            view_donners = tk.Button(Frame2, text="View Donners", command=view_donners ,bg="#4F1DB8",fg="#FFFFFF")
            view_donners.place(x=300, y=150, height=55, width=300)
            view_donners.configure(font=("times", 30), relief="flat")

            view_history = tk.Button(Frame2, text="View History", command= view_history,bg="#4F1DB8",fg="#FFFFFF")
            view_history.place(x=300, y=255, height=55, width=300)
            view_history.configure(font=("times", 30), relief="flat")

            view_analysis_b = tk.Button(Frame2, text="View analysis", command=view_analysis,bg="#4F1DB8",fg="#FFFFFF")
            view_analysis_b.place(x=300, y=360, height=55, width=300)
            view_analysis_b.configure(font=("times", 30), relief="flat")
        
        else:
            messagebox.showerror("Error","Username or Password Incorrect!!")
            return None

        adminback=tk.Button(Frame2,text="Back",bg="#FFFFFF",command=lambda:admin1())
        adminback.place(x=1200,y=550,height=45,width=180)
        adminback.configure(font=("times",25),relief="flat")

    adminbg=Label(Frame2)
    adminbg.place(x=-210,y=-140,height=980, width=1920)
    adminbg.configure(image=admin1bg)

    username_var = tk.StringVar()
    username_entrybox = tk.Entry(Frame2, width=20, textvariable=username_var)
    username_entrybox.focus()
    username_entrybox.place(x=1000, y=197, width=315, height=45)
    username_entrybox.configure(background='white', font=("times", 15), cursor="ibeam #ffffff")

    password_var = tk.StringVar()
    password_entrybox = tk.Entry(Frame2, width=20, textvariable=password_var)
    password_entrybox.configure(show="*")
    password_entrybox.place(x=1000, y=290, width=315, height=45)
    password_entrybox.configure(background='white', font=("times", 15), cursor="ibeam #ffffff")
        
    loginadmin=tk.Button(Frame2,text="LOG IN",command=lambda:adminaction(),bg="#FFFFFF")
    loginadmin.place(x=1003,y=413,height=57,width=190)
    loginadmin.configure(font=("times",30),relief="flat")


admin=tk.Button(Frame1,text='Admin',command=admin1)
admin.place(x=870,y=95,width=150,height=45)
admin.configure(font=(15),relief='flat')

def bankrules():
    for widget in Frame2.winfo_children():
        widget.destroy()
    
    rules=tk.Label(Frame2)
    rules.place(x=-195,y=-190,height=980, width=1920)
    rules.configure(image=rulesimg)

bankrules=tk.Button(Frame1,text='Rules',command=bankrules)
bankrules.place(x=1090,y=95,width=150,height=45)
bankrules.configure(font=(15),relief='flat')

def contactus1():
    for widget in Frame2.winfo_children():
        widget.destroy()

    def inq_form():
        name=name_inq_var.get()
        email=email_inq_var.get()
        phone=phone_inq_var.get()
        subject=subject_inq_var.get()
        message=message_inq_var.get()

        with open('inquiry.csv','a') as f20:
                dict_writer=DictWriter(f20,fieldnames=['Name','Email','Phone No','Subject','Message'])
                if os.stat('inquiry.csv').st_size==0:
                    dict_writer.writeheader()
                else:
                    dict_writer.writerow({
                    'Name' : name,
                    'Email' :email,
                    'Phone No' : phone,
                    'Subject':subject,
                    'Message':message  
                    })
        name_inq_entrybox.delete(0,tk.END)
        email_inq_entrybox.delete(0,tk.END)
        phone_inq_entrybox.delete(0,tk.END)
        message_inq_entrybox.delete(0,tk.END)
        subject_inq_entrybox.delete(0,tk.END)

        messagebox.showinfo("Information","Your Inquiry Saved Sucessfully !")
        return None

    contactbg=Label(Frame2)
    contactbg.place(x=-195,y=-190,height=980, width=1920)
    contactbg.configure(image=contactusimg)

    name_inq_var = tk.StringVar()
    name_inq_entrybox = tk.Entry(Frame2, width=20, textvariable=name_inq_var)
    name_inq_entrybox.focus()
    name_inq_entrybox.place(x=775, y=243, width=330, height=47)
    name_inq_entrybox.configure(background='white', font=("times", 15), cursor="ibeam #ffffff")

    email_inq_var = tk.StringVar()
    email_inq_entrybox = tk.Entry(Frame2, width=20, textvariable=email_inq_var)
    email_inq_entrybox.place(x=1143, y=243, width=330, height=47)
    email_inq_entrybox.configure(background='white', font=("times", 15), cursor="ibeam #ffffff")

    phone_inq_var = tk.StringVar()
    phone_inq_entrybox = tk.Entry(Frame2, width=20, textvariable=phone_inq_var)
    phone_inq_entrybox.place(x=775, y=353, width=330, height=47)
    phone_inq_entrybox.configure(background='white', font=("times", 15), cursor="ibeam #ffffff")

    subject_inq_var = tk.StringVar()
    subject_inq_entrybox = tk.Entry(Frame2, width=20, textvariable=subject_inq_var)
    subject_inq_entrybox.place(x=1143, y=353, width=330, height=47)
    subject_inq_entrybox.configure(background='white', font=("times", 15), cursor="ibeam #ffffff")

    message_inq_var = tk.StringVar()
    message_inq_entrybox = tk.Entry(Frame2, width=20, textvariable=message_inq_var)
    message_inq_entrybox.place(x=775, y=460, width=697, height=95)
    message_inq_entrybox.configure(background='white', font=("times", 15), cursor="ibeam #ffffff")

    submit_inq=tk.Button(Frame2,text="SUBMIT",bg="#FF0000",fg="#FFFFFF",command=inq_form)
    submit_inq.place(x=775,y=590,width=135,height=48)
    submit_inq.configure(font=(("times"),18))

contactus=tk.Button(Frame1,text='Contact Us',command=contactus1)
contactus.place(x=1310,y=95,width=150,height=45)
contactus.configure(font=(15),relief='flat')


def user_options(username,useremail,usergender,userage,userphonno,userbloodgroup,usercity):
    
    def request_blood2():
        
        for widget in Frame2.winfo_children():
            widget.destroy()

        req_bg=Label(Frame2)
        req_bg.place(x=-180,y=-170,height=980, width=1920)
        req_bg.configure(image=req_bg_img)

        bloodg_var_req=tk.StringVar()
        bloodg_req_combobox=ttk.Combobox(Frame2,width=16,textvariable=bloodg_var_req,state='readonly')
        bloodg_req_combobox['values']=('A+','A-','B+','B-','AB+','AB-','O+','O-')
        bloodg_req_combobox.current(0)
        bloodg_req_combobox.place(x=1102,y=320,width=390,height=55)
        bloodg_req_combobox.configure(font=("times",18))

        city_var_req=tk.StringVar()
        city_req_combobox=ttk.Combobox(Frame2,width=16,textvariable=city_var_req,state='readonly')
        city_req_combobox['values']=('Rajkot','Surat' ,'Junagadh','Ahemdabad','Vadodara')
        city_req_combobox.current(0)
        city_req_combobox.place(x=1102,y=187,width=390,height=55)
        city_req_combobox.configure(font=("times",18))

        def req_accept1():
            for widget in Frame2.winfo_children():
                widget.destroy()

            Label11 = tk.Label(Frame2)
            Label11.place(x=-200,y=-170,height=980, width=1920)
            Label11.configure(image=req_bg_img1)
        
            def select_doner(name, email, phno, age, gender):
                f13 = open('temp.csv', 'a')

                f12 = open('activedoners.csv', 'r')
                with f12:
                    dict_reader5 = DictReader(f12)
                    dict_writer6 = DictWriter(f13,
                                              fieldnames=['Name', 'Email', 'Phone No', 'Age', 'Blood Group',
                                                          'Gender', 'City'])
                
                    dict_writer6.writeheader()
                    for row in dict_reader5:
                        if row['Name'] == name and row['Email'] == email and row['Phone No'] == phno and row[
                            'Age'] == age and row['Gender'] == gender:
                            continue
                        else:

                            
                                # print("flase")
                            dict_writer6.writerow(
                                {
                                    'Name': row['Name'],
                                    'Email': row['Email'],
                                    'Phone No': row['Phone No'],
                                    'Age': row['Age'],
                                    'Blood Group': row['Blood Group'],
                                    'Gender': row['Gender'],
                                    'City': row['City']
                                }
                            )

                

                fileVariable1 = open('activedoners.csv', 'r+')
                fileVariable1.truncate(0)
                fileVariable1.close()
                
                f12.close()
                f13.close()

                f16 = open('activedoners.csv', 'a')
                f17 = open('temp.csv', 'r')
                with f17:
                    dict_reader7 = DictReader(f17)
                    dict_writer7 = DictWriter(f16, fieldnames=['Name', 'Email', 'Phone No', 'Age', 'Blood Group',
                                                               'Gender', 'City'])
                     
                    dict_writer7.writeheader()
                           
                    for row in dict_reader7:
                       

                        dict_writer7.writerow(
                            {
                                'Name': row['Name'],
                                'Email': row['Email'],
                                'Phone No': row['Phone No'],
                                'Age': row['Age'],
                                'Blood Group': row['Blood Group'],
                                'Gender': row['Gender'],
                                'City': row['City']
                            })
                f16.close()
                f17.close()

                fileVariable = open('temp.csv', 'r+')
                fileVariable.truncate(0)
                fileVariable.close()

                f11 = open('history.csv', 'a')
                with f11:

                    dict_writer5 = DictWriter(f11, fieldnames=['Name', 'Email', 'Aname', 'Aemail', 'Aphone No', 'Aage',
                                                               'Agender'])

                    if os.stat('history.csv').st_size == 0:
                        dict_writer5.writeheader()
                    else:
                        dict_writer5.writerow({
                            'Name': name,
                            'Email': email,
                            'Aname': username,
                            'Aemail': useremail,
                            'Aage': userage,
                            'Aphone No': userphonno,
                            'Agender': usergender,
                        })
                messagebox.showinfo("Information","Your Request Saved Sucessfully !")
                return request_blood2()

            h_count=190
            f2 = open('activedoners.csv', 'r')
            with f2:
                reader13= DictReader(f2)
                for row in reader13:
                    name=row['Name']
                    email=row['Email']
                    phno=row['Phone No']
                    age=row['Age']
                    bloodg=row['Blood Group']
                    gender=row['Gender']
                    city=row['City']
                    
                    if(bloodg==bloodg_var_req.get() and city==city_var_req.get()):
                        button1=tk.Button(Frame2,text=f"{name}\t\t{email}\t\t{phno}\t\t{age}\t\t{gender}")
                        button1.place(x=100,y=h_count,height=30)
                        button1.configure(font=("times",20))
                        h_count=h_count+30
                        button1["command"] = lambda name=name , email=email,  phno=phno, age=age, gender=gender: select_doner(name, email, phno, age, gender)

            reqback1=tk.Button(Frame2,text="Back",bg="#FFFFFF",command=lambda:request_blood2())
            reqback1.place(x=1200,y=550,height=40,width=180)
            reqback1.configure(font=("times",25))

        req_accept=tk.Button(Frame2,text="Request",bg="#C6E1B5",fg="black",command=lambda:req_accept1())
        req_accept.place(x=1205,y=453,width=200,height=50)
        req_accept.configure(font=("times" , 20),relief="flat")

        reqback2=tk.Button(Frame2,text="Back",bg="#FFFFFF",command=lambda:user_options(username,useremail,usergender,userage,userphonno,userbloodgroup,usercity))
        reqback2.place(x=1200,y=550,height=40,width=180)
        reqback2.configure(font=("times",25))

    def history_check():
        for widget in Frame2.winfo_children():
            widget.destroy()    
        if os.path.exists('./history.csv') == False:
            messagebox.showerror("Error","Your History Is Empty")
        scrollbarx = Scrollbar(Frame2, orient=HORIZONTAL)
        scrollbary = Scrollbar(Frame2, orient=VERTICAL)
        tree = ttk.Treeview(Frame2,
                            columns=("Name", "Email", "Aname", "Aemail", "Aphone No", "Aage", "Agender"),
                            height=400, selectmode="extended",
                            yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)

        style=ttk.Style()
        style.configure("Treeview", rowheight=35)

        tree.heading('Name', text="Name", anchor=W)
        tree.heading('Email', text="Email", anchor=W)
        tree.heading('Aname', text="Accepter name", anchor=W)
        tree.heading('Aemail', text="Accepter email", anchor=W)
        tree.heading('Aphone No', text="Accepter phone No", anchor=W)
        tree.heading('Aage', text="Accepter Age", anchor=W)

        tree.heading('Agender', text="Accepter Gender", anchor=W)

        tree.column('#0', stretch=YES, minwidth=0, width=0)
        tree.column('#1', stretch=YES, minwidth=0, width=150)
        tree.column('#2', stretch=YES, minwidth=0, width=150)
        tree.column('#3', stretch=YES, minwidth=0, width=150)
        tree.column('#4', stretch=YES, minwidth=0, width=150)
        tree.column('#5', stretch=YES, minwidth=0, width=150)
        tree.column('#6', stretch=YES, minwidth=0, width=150)

        tree.place(x=0,y=00,width=1600)
        with open('history.csv') as f:
            reader = csv.DictReader(f)
            ok =False
            for row in reader:
                if row['Name']==username and row['Email']==useremail:
                    email = row['Email']
                    name = row['Name']
                    aemail = row['Aemail']
                    aname = row['Aname']
                    age = row['Aage']
                    phno = row['Aphone No']
                    gender = row['Agender']
                    ok=True
                    tree.insert("", 0, values=(name, email, aname, aemail, phno, age, gender))

            if not ok:
                messagebox.showerror("Error","Your History is Empty")
        
        hisback=tk.Button(Frame2,text="Back",bg="#FFFFFF",command=lambda:user_options(username,useremail,usergender,userage,userphonno,userbloodgroup,usercity))
        hisback.place(x=1200,y=550,height=40,width=180)
        hisback.configure(font=(25),relief="flat")

    def donate_blood():
        for widget in Frame2.winfo_children():
            widget.destroy()    
        
        def actiondona():
            w=weight_var.get()
            pre=prev_dona_var.get()
            hea=health_var.get()
            alc=alcohol_var.get()
            if (w<50 or pre=='YES' or hea=='NO' or alc=='YES'):
                messagebox.showerror("Error","You are Not Eligible")
                return user_options(username,useremail,usergender,userage,userphonno,userbloodgroup,usercity)
            else:
                with open('activedoners.csv', 'a') as f1:
                    dict_writer1 = DictWriter(f1,fieldnames=['Name', 'Email','Phone No', 'Age', 'Blood Group','Gender', 'City'])
                    if os.stat('activedoners.csv').st_size == 0:
                        dict_writer1.writeheader()
                    dict_writer1.writerow({
                        'Name': username,
                        'Email': useremail,
                        'Phone No': userphonno,
                        'Age': userage,
                        'Blood Group': userbloodgroup,
                        'Gender': usergender,
                        'City': usercity
                    })
            weight.delete(0,tk.END)
            prev_dona_combobox.delete(0,tk.END)
            health_combobox.delete(0,tk.END)
            alcohol_combobox.delete(0,tk.END)
            messagebox.showinfo("Sucess","You SucessFully Donated Your Blood Thank You ! Come Again !")
            return user_options(username,useremail,usergender,userage,userphonno,userbloodgroup,usercity)
            
        bguserop1=Label(Frame2)
        bguserop1.place(x=-170,y=-160,height=980,width=1920)
        bguserop1.configure(image=userop1bg)

        weight_var=tk.IntVar()
        weight=tk.Entry(Frame2,textvariable=weight_var)
        weight.place(x=1110,y=141,width=290,height=44)
        weight.configure(background='white',relief='flat',font=("times",15),cursor="ibeam #ffffff")

        prev_dona_var=tk.StringVar()
        prev_dona_combobox=ttk.Combobox(Frame2,width=16,textvariable=prev_dona_var,state='readonly')
        prev_dona_combobox['values']=('YES','NO')
        prev_dona_combobox.current(0)
        prev_dona_combobox.place(x=1110,y=260,width=292,height=44)
        
        health_var=tk.StringVar()
        health_combobox=ttk.Combobox(Frame2,width=16,textvariable=health_var,state='readonly')
        health_combobox['values']=('YES','NO')
        health_combobox.current(0)
        health_combobox.place(x=1110,y=375,width=292,height=44)

        alcohol_var=tk.StringVar()
        alcohol_combobox=ttk.Combobox(Frame2,width=16,textvariable=alcohol_var,state='readonly')
        alcohol_combobox['values']=('YES','NO')
        alcohol_combobox.current(0)
        alcohol_combobox.place(x=1110,y=482,width=292,height=44)

        submit_donation=tk.Button(Frame2,text="Submit" ,command=lambda:actiondona())
        submit_donation.place(x=1110,y=575,width=292,height=55)
        submit_donation.configure(font=("times",20),relief='flat',bg="#FFFFFF")

        donaback=tk.Button(Frame2,text="Back",bg="#FFFFFF",command=lambda:user_options(username,useremail,usergender,userage,userphonno,userbloodgroup,usercity))
        donaback.place(x=557,y=600,height=40,width=228)
        donaback.configure(font=(25),relief="flat")
    
    for widget in Frame2.winfo_children():
        widget.destroy()

    bguserop=Label(Frame2)
    bguserop.place(x=-170,y=-160,height=980,width=1920)
    bguserop.configure(image=useropbg)

    donate_blood_bt=tk.Button(Frame2,text='Donate Blood',fg="#182758",bg="#F8CBAD",command=donate_blood)
    donate_blood_bt.place(x=212,y=114,width=342,height=84)
    donate_blood_bt.configure(font=("times",30),relief='flat')

    history_check_bt=tk.Button(Frame2,text='Check History',fg="#182758",bg="#F8CBAD",command=history_check)
    history_check_bt.place(x=212,y=291,width=342,height=84)
    history_check_bt.configure(font=("times",30),relief='flat')

    request_blood_bt=tk.Button(Frame2,text='Request Blood',fg="#182758",bg="#F8CBAD",command=request_blood2)
    request_blood_bt.place(x=212,y=457,width=342,height=84)
    request_blood_bt.configure(font=("times",30),relief='flat')

    useropback=tk.Button(Frame2,text="Back",bg="#FFFFFF",command=lambda:login())
    useropback.place(x=1200,y=550,height=40,width=180)
    useropback.configure(font=("times",25),relief="flat")
 
#mainloop Of full Gui
root.mainloop()