from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector as sqLtor

#CONNECTING PYTHON AND SQL 
con = sqLtor.connect(host="localhost",user="root",password='4.4.2020ruthless',database='library')
cur = con.cursor()

#TABLE NAMES
issueTable = "books_issued" 
bookTable = "books" #Book Table


def deleteBook():
    
    bid = bookInfo1.get()

    #DELETING BOOK FROM DATABASE
    try:
        cur.execute("delete from "+bookTable+" where bid = '"+bid+"'")
        con.commit()
        cur.execute("delete from "+issueTable+" where bid = '"+bid+"'")
        con.commit()
        messagebox.showinfo('Success',"Book Record Deleted Successfully")
        #con.close()
    except:
        messagebox.showinfo("error","Please check Book ID")
    

    print(bid)

    bookInfo1.delete(0, END)
    deltop.destroy()
    
def delete(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,deltop
    
    #CREATING WINDOW
    deltop=Toplevel()
    deltop.title("Library")
    deltop.geometry("600x500")

    #IMPORTING AND RESIZING IMAGE
    img2=Image.open('C:\\Users\\Dell\\Documents\\Python Project\\Library management (MAIN)\\books.jpg')
    img2=img2.resize((600,500),Image.ANTIALIAS)
    newimg2=ImageTk.PhotoImage(img2)

    #CREATING CANVAS
    canvas2=Canvas(deltop)
    canvas2.create_image(300,250,image=newimg2)
    canvas2.pack(expand=True,fill=BOTH)
        
    #CREATING BLACK HEADING FRAME
    headingFrame2 = Frame(deltop,bg='black',bd=5)
    headingFrame2.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    #CREATING BEIGE HEADING LABEL WITH BLACK TEXT 
    headingLabel = Label(headingFrame2, text="Delete Book", bg='#f0cfa5', fg='black', font=('Comic Sans MS',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    #CREATING BLACK FRAME FOR ENTRY BOXES
    frame1=Frame(deltop,bg="black")
    frame1.place(relx=0.09,rely=0.29,relwidth=0.82,relheight=0.52)

    #CREATING BEIGE FRAME FOR ENTRY BOXES
    labelFrame = Frame(deltop,bg='#f0cfa5')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    #CREATING LABEL Book ID ON PREV FRAME
    lb2 = Label(labelFrame,text="Book ID : ", bg='#f0cfa5', fg='black')
    lb2.place(relx=0.05,rely=0.5)
        
    #CREATING ENTRY BOX FOR Book ID
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #CREATING BLACK FRAME FOR SUBMIT BUTTON
    frame2=Frame(deltop,bg="black")
    frame2.place(relx=0.2765,rely=0.895,relwidth=0.185,relheight=0.085)

    #CREATING SUBMIT BUTTON
    SubmitBtn = Button(deltop,text="SUBMIT",bg='#f0cfa5', fg='black',command=deleteBook)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    #CREATING BLACK FRAME FOR QUIT BUTTON
    frame3=Frame(deltop,bg="black")
    frame3.place(relx=0.5265,rely=0.895,relwidth=0.185,relheight=0.085)

    #CREATING QUIT BUTTON
    quitBtn = Button(deltop,text="Quit",bg='#f0cfa5', fg='black', command=deltop.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    deltop.mainloop()
