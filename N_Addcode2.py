from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector as sqLtor

def bookRegister():

    #RETREIVING DATA FROM ENTRY BOXES
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()
    
    #INSERTING BOOKS IN DATABASE 
    insertBooks = "insert into books values('"+bid+"','"+title+"','"+author+"','"+status+"')"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success',"Book added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    

    #PRINTING ON PYTHON SHELL
    print(bid)
    print(title)
    print(author)
    print(status)


    addtop.destroy()
    
def addBook(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,addtop   

    con = sqLtor.connect(host="localhost",user="root",password='4.4.2020ruthless',database='library')
    cur = con.cursor()
    

    #TABLE NAME
    bookTable = "books"

    #CREATING TOPLEVEL WINDOW
    addtop=Toplevel()
    addtop.title("Library")
    addtop.geometry("600x500")

    #IMPORTING AND RESIZING BG IMAGE
    img1=Image.open('C:\\Users\\Dell\\Documents\\Python Project\\Library management (MAIN)\\books.jpg')
    img1=img1.resize((600,500),Image.ANTIALIAS)
    newimg1=ImageTk.PhotoImage(img1)

    #CREATING CANVAS
    canvas1=Canvas(addtop)
    canvas1.create_image(300,250,image=newimg1)
    canvas1.pack(expand=True,fill=BOTH)
   
    #CREATING BLACK HEADING FRAME
    headingFrame1 = Frame(addtop,bg="black",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    #CREATING BEIGE LABEL WITH BLACK TEXT
    headingLabel = Label(headingFrame1, text="Add Books", bg='#f0cfa5', fg='black', font=('Comic Sans MS',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    #CREATING BLACK FRAME FOR ENTRY LABEL
    entryframe=Frame(addtop,bg="black")
    entryframe.place(relx=0.09,rely=0.39,relwidth=0.82,relheight=0.42)

    #CREATING BEIGE LABEL FOR ENTRY BOXES
    labelFrame = Frame(addtop,bg='#f0cfa5')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    #CREATING LABEL Book ID ON ENTRY LABEL
    lb1 = Label(labelFrame,text="Book ID : ", bg='#f0cfa5', fg='black')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)

    #CREATING ENTRY BOX NEXT TO Book ID LABEL    
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    #CREATING LABEL Title ON ENTRY LABEL
    lb2 = Label(labelFrame,text="Title : ", bg='#f0cfa5', fg='black')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    #CREATING ENTRY BOX NEXT TO Title LABEL  
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    #CREATING LABEL Author ON ENTRY LABEL
    lb3 = Label(labelFrame,text="Author : ", bg='#f0cfa5', fg='black')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    #CREATING ENTRY BOX NEXT TO Author LABEL  
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    #CREATING LABEL Status ON ENTRY LABEL
    lb4 = Label(labelFrame,text="Status(Avail/issued) : ", bg='#f0cfa5', fg='black')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    #CREATING ENTRY BOX NEXT TO Status LABEL  
    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
    #CREATING BLACK FRAME FOR SUBMIT BUTTON
    frame1=Frame(addtop,bg="black")
    frame1.place(relx=0.2765,rely=0.895,relwidth=0.185,relheight=0.085)

    #CREATING SUBMIT BUTTON
    SubmitBtn = Button(addtop,text="SUBMIT",bg='#f0cfa5', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    #CREATING BLACK FRAME FOR QUIT BUTTON
    frame2=Frame(addtop,bg="black")
    frame2.place(relx=0.5265,rely=0.895,relwidth=0.185,relheight=0.085)

    #CREATING QUIT BUTTON
    quitBtn = Button(addtop,text="Quit",bg='#f0cfa5', fg='black', command=addtop.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    addtop.mainloop()
