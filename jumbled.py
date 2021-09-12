from tkinter import messagebox
from tkinter import *
import random
t=Tk()
t.resizable(0,0)
t.title("Jumbled Game")
w=300
h=300
x=(t.winfo_screenwidth()-w)/2
y=(t.winfo_screenheight()-h)/2
t.geometry("%dx%d+%d+%d"%(w,h,x,y))
t.configure(bg="black")

words=["hveeica","mtruaae","cnintae","mcexpol","oocderk","toeyrsd","egvnine","iniftco","ohlfios","ogefirv","reetpsn","esdedcn","lhaowls","nongrim","iceever"]
answer=["achieve","amateur","ancient","complex","crooked","destroy","evening","fiction","foolish","forgive","present","descend","shallow","morning","receive"]

num=random.randrange(0,15,1)

def deafult():
    global words,answer,num
    u1.config(text=words[num])

def checkans():
    global words,answer,num    
    p=e1.get()
    if p==answer[num]:
        messagebox.showinfo("sucess","this is correct ans")
    else:    
        messagebox.showinfo("error","this is not correct ans")
    a.set("")
    
def res():    
        global words,answer,num
        num=random.randrange(0,15,1)
        u1.config(text=words[num])
        a.set("")
    
a=StringVar()
    
u1=Label(text="YOU HERE",font=("",20),bg="orange",fg="black")
u1.place(x=50,y=50,width=200,height=30)
e1=Entry(font=("",15),textvariable=a)
e1.place(x=50,y=100,width=200,height=30)
b2=Button(text="Check",font=("",15),bg="red",fg="black",activebackground="black",activeforeground="red",command=checkans)
b2.place(x=50,y=150,width=200,height=45)
b3=Button(text="Reset",font=("",15),bg="red",fg="black",activebackground="black",activeforeground="red",command=res)
b3.place(x=50,y=220,width=200,height=45)
deafult()
    
t.mainloop()