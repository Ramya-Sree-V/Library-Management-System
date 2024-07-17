from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from N_Addcode2 import *
from N_Deletecode import *
from R_VB import *
from P_issuebook import *
from P_returnbook import *
import mysql.connector

con = mysql.connector.connect(host="localhost",user="root",password="4.4.2020ruthless",database="library")
cur = con.cursor()

global addtop,window,deltop,viewtop,issuetop

#CREATING WINDOW
window=Tk()
window.title("Library")
window.minsize(width=400,height=400)
window.geometry("600x500")

#IMPORTING AND RESIZING IMAGE FOR MAIN WINDOW BACKGROUND
img=Image.open('C:\\Users\\Dell\\Documents\\Python Project\\Library management (MAIN)\\books5.jpg')
img=img.resize((600,500),Image.ANTIALIAS)
newimg=ImageTk.PhotoImage(img)

#CREATING CANVAS
canvas=Canvas(window)
canvas.create_image(300,250,image=newimg)
canvas.pack(expand=True,fill=BOTH)

#CREATING FRAME AND LABEL FOR HEADING
headingFrame1 = Frame(window,bg="black",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="LIBRARY MANAGEMENT SYSTEM", bg='#f0cfa5', fg='black', font=("Comic Sans MS",15,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

#CREATING ADDBOOK BUTTON
photo1=Image.open(r"C:\Users\Dell\Documents\Python Project\Library management (MAIN)\Addbook4.png")#IMPORTING AND RESIZING IMAGE
photo1=photo1.resize((100,100),Image.ANTIALIAS)
newphoto1=ImageTk.PhotoImage(photo1)

btn1frame=Frame(window,bg="black")#APPLYING BUTTON FRAME
btn1frame.place(relx=0.138,rely=0.387,relwidth=0.22,relheight=0.27)

btn1 = Button(window,text="Add Book Details",bg='#f0cfa5', fg='black',image=newphoto1 ,compound="top",command=addBook,font=("Comic Sans MS",10))
btn1.place(relx=0.15,rely=0.4, relwidth=0.2,relheight=0.25)#APPLYING BUTTON

#CREATING DELETEBOOK BUTTON
photo2=Image.open(r"C:\Users\Dell\Documents\Python Project\Library management (MAIN)\DeleteBook3.png")#IMPORTING AND RESIZING IMAGE
photo2=photo2.resize((100,100),Image.ANTIALIAS)
newphoto2=ImageTk.PhotoImage(photo2)

btn2frame=Frame(window,bg="black")#APPLYING BUTTON FRAME
btn2frame.place(relx=0.65,rely=0.387,relwidth=0.22,relheight=0.27)

btn2 = Button(window,text="Delete Book",bg='#f0cfa5', fg='black',image=newphoto2,compound="top",font=("Comic Sans MS",10),command=delete)
btn2.place(relx=0.66,rely=0.4, relwidth=0.2,relheight=0.25)#APPLYING BUTTON
    
#CREATING VIEWBOOK BUTTON

photo3=Image.open(r"C:\Users\Dell\Documents\Python Project\Library management (MAIN)\viewbook.png")#IMPORTING AND RESIZING IMAGE
photo3=photo3.resize((100,100),Image.ANTIALIAS)
newphoto3=ImageTk.PhotoImage(photo3)

btn3frame=Frame(window,bg="black")#APPLYING BUTTON FRAME
btn3frame.place(relx=0.39,rely=0.537,relwidth=0.22,relheight=0.27)


btn3 = Button(window,text="View Book List",bg='#f0cfa5', fg='black',image=newphoto3,compound="top",command=View,font=("Comic Sans MS",10))
btn3.place(relx=0.4,rely=0.55, relwidth=0.2,relheight=0.25)#APPLYING BUTTON


#CREATING ISSUEBOOK BUTTON
photo4=Image.open(r"C:\Users\Dell\Documents\Python Project\Library management (MAIN)\issuebook2.png")#IMPORTING AND RESIZING IMAGE
photo4=photo4.resize((100,100),Image.ANTIALIAS)
newphoto4=ImageTk.PhotoImage(photo4)

btn4frame=Frame(window,bg="black")#APPLYING BUTTON FRAME
btn4frame.place(relx=0.138,rely=0.687,relwidth=0.22,relheight=0.27)

btn4 = Button(window,text="Issue Book",bg='#f0cfa5', fg='black',image=newphoto4,compound="top", command = issueBook,font=("Comic Sans MS",10))
btn4.place(relx=0.15,rely=0.7, relwidth=0.2,relheight=0.25)#APPLYING BUTTON
    
#CREATING RETURNBOOK BUTTON
photo5=Image.open(r"C:\Users\Dell\Documents\Python Project\Library management (MAIN)\returnbook2.png")#IMPORTING AND RESIZING IMAGE
photo5=photo5.resize((100,100),Image.ANTIALIAS)
newphoto5=ImageTk.PhotoImage(photo5)

btn5frame=Frame(window,bg="black")#APPLYING BUTTON FRAME
btn5frame.place(relx=0.65,rely=0.687,relwidth=0.22,relheight=0.27)

btn5 = Button(window,text="Return Book",bg='#f0cfa5', fg='black',image=newphoto5,compound="top",command = returnBook,font=("Comic Sans MS",10))
btn5.place(relx=0.66,rely=0.7, relwidth=0.2,relheight=0.25)#APPLYING BUTTON

window.mainloop()
