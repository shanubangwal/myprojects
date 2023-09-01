from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from tkinter.ttk import Combobox
import openpyxl,xlrd
from openpyxl import Workbook
import pathlib

background="#06283D"
framebg="#EDEDED"
framefg="#06283D"

root=Tk()
root.title("student regestration system")
root.geometry("1250x700+210+100")
root.config(bg="red")

file=pathlib.Path("student_data.xlsx")
if file.exists():
    pass
else:
    file=Workbook()
    sheet=file.active
    sheet['A1']="Registration No."
    sheet['B1']="Name"
    sheet['C1']="Class"
    sheet['D1']="Gender"
    sheet['E1']="DOB"
    sheet['F1']="Date Of Registration"
    sheet['G1']="Religion"
    sheet['H1']="Skill"
    sheet['I1']="Father Name"
    sheet['J1']="Mother Name" 
    sheet['l1']="Mothers's Occupation"
    
    file.save('student_data.xlsx')

#gender
def selection():
    value=radio.get()
    if value==1:
        gender="Male"
        print(gender)
    else:
        gender="Female"
        print(gender)

#top Frames
Label(root,text="Email:Officialshanubangwal@gmail.com",width=10,height=3,bg="#f0687c",anchor="e").pack(side=TOP,fill=X)
Label(root,text="Student Registrations",width=8,height=2,bg="#c36464",fg="#fff",font="arial 20 bold").pack(side=TOP,fill=X)



#search 
Search=StringVar()
Entry(root,textvariable=Search,width=15,bd=2,font="arial 20").place(x=920,y=70)
imageicon3=PhotoImage(file="D:\My Journy\pngs for programs\icons8-search-50.png")
srch=Button(root,text="Search",compound=LEFT,image=imageicon3,width=123,bg="#68ddfa",font="arial 13 bold")
srch.place(x=1160,y=58  )

imageicon4=PhotoImage(file="pngs for programs/icons8-file-64.png")
Update_button=Button(root,image=imageicon4, width=50,height=50,bg="#c36464")
Update_button.place(x=90,y=60)


#Regestration and data filling
Label(root,text="Registration no :",font="arial 13",fg=framebg,bg=background).place(x=30,y=150)
Label(root,text="Date:",font="arial 13",fg=framebg,bg=background).place(x=500,y=150)

Registration=StringVar()
Date = StringVar()

reg_entry = Entry(root,textvariable= Registration ,width=20 ,font="ariaal 10")
reg_entry.place(x=160,y=150)

# registration_no ()

today = date.today()
d1 = today.strftime("%d/%m/%y")
date_entery = Entry(root,textvariable=Date,width=15,font="arial 10")
date_entery.place(x=550,y=150)

Date.set(d1)

# student details 
obj=LabelFrame(root,text="student,s Details",font=20,bd=2,width=900,bg=framefg, fg=framebg,height=250,relief=GROOVE)
obj.place(x=30,y=200)


Label(obj,text="Full name",font="arial 13",bg=framebg,fg=framefg).place(x=30,y=50)
Label(obj,text="Date of Birth",font="arial 13",bg=framebg,fg=framefg).place(x=30,y=100)
Label(obj,text="Gender",font="arial 13",bg=framebg,fg=framefg).place(x=30,y=150)

Label(obj,text="Class",font="arial 13",bg=framebg,fg=framefg).place(x=500,y=50)
Label(obj,text="Religion",font="arial 13",bg=framebg,fg=framefg).place(x=500,y=100)
Label(obj,text="Skills",font="arial 13",bg=framebg,fg=framefg).place(x=500,y=150)

name = StringVar()
name_entery = Entry(obj,textvariable=name,width=20,font="arial 10")
name_entery.place(x=160,y=50)

dob = StringVar()
dob_entery = Entry(obj,textvariable=dob,width=20,font="arial 10")
dob_entery.place(x=160,y=100)

religion = StringVar()
religion_entery = Entry(obj,textvariable=religion,width=20,font="arial 10")
religion_entery.place(x=630,y=100)

skill = StringVar()
skill_entery = Entry(obj,textvariable=skill,width=20,font="arial 10")
skill_entery.place(x=630,y=150)


Class= Combobox(obj,value=['1','2','3','4','5','6','7','8','9','10','11','12'],font="Roboto 10",width=17,state="r")
Class.place(x=630,y=50)
Class.set("Select Class")

# radio buttons
radio=IntVar()
r1=Radiobutton(obj,text="Male",variable=radio,value=1,bg=framebg,fg=framefg ,command=selection)
r1.place(x=150,y=150)

r2=Radiobutton(obj,text="Female",variable=radio,value=2,bg=framebg,fg=framefg, command=selection)
r2.place(x=250,y=150)







# parents details 
obj2=LabelFrame(root,text="parent,s Details",font=20,bd=2,width=900,bg=framefg, fg=framebg,height=220,relief=GROOVE)
obj2.place(x=30,y=470)

# biometric details 
obj3=LabelFrame(root,text="biometric,s Details",font=20,bd=2,width=300,bg=framefg, fg=framebg,height=490,relief=GROOVE)
obj3.place(x=960,y=200)








root.mainloop()

