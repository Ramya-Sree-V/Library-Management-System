from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector as sqltor

#CONNECTING SQL AND PYTHON
con = sqltor.connect(host="localhost",user="root",password="4.4.2020ruthless",database="library")
cur = con.cursor()

#LIST STORES ALL BOOK IDS
allBid = []

def returnn():
    global SubmitBtn,labelFrame,lb1,bookInfo1,quitBtn,window5,canvas,status
    bid = bookInfo1.get()
    
    #RETURNING BOOK FROM DATABASE
    cur.execute("select bid from books_issued ")
    data=cur.fetchall()
    con.commit()
    for i in data:
        allBid.append(i[0])
        
    if bid in allBid:
        cur.execute("select status from books where bid = '"+bid+"'")
        data2=cur.fetchall()
        con.commit()
        for i in data2:
            if i[0] == 'issued':
                status = True
            else:
                status = False
        
    else:
        messagebox.showinfo("Error","Book ID not present")
   
    print(bid in allBid)
    print(status)
    
    if bid in allBid and status == True:
        cur.execute("delete from books_issued where bid = '"+bid+"'")#issue sql
        con.commit()
        cur.execute("update books set status = 'avail' where bid = '"+bid+"'")#update status
        con.commit()
        messagebox.showinfo('Success',"Book Returned Successfully")
    elif bid in allBid and status == False:
        allBid.clear()
        messagebox.showinfo('Message',"Please check the book ID")
        returntop.destroy()
        return
    else:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    
    allBid.clear()
    returntop.destroy()
    
def returnBook(): 
    
    global bookInfo1,SubmitBtn,quitBtn,canvas,con,cur,window5,labelFrame,lb1,returntop

    #CREATING WINDOW
    returntop=Toplevel()
    returntop.title("Library")
    returntop.geometry("600x500")

    #IMPORTING AND RESIZING IMAGE FOR MAIN WINDOW BACKGROUND
    img5=Image.open('C:\\Users\\Dell\\Documents\\Python Project\\Library management (MAIN)\\books.jpg')
    img5=img5.resize((600,500),Image.ANTIALIAS)
    newimg5=ImageTk.PhotoImage(img5)

    #CREATING CANVAS
    canvas5=Canvas(returntop)
    canvas5.create_image(300,250,image=newimg5)
    canvas5.pack(expand=True,fill=BOTH)
    
    #CREATING BLACK HEADING FRAME 
    headingFrame1 = Frame(returntop,bg="black",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    #CREATING BEIGE LABEL WITH BLACK TEXT
    headingLabel = Label(headingFrame1, text="Return Book", bg='#f0cfa5', fg='black', font=("Comic Sans MS",15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    #CREATING BLACK FRAME FOR ENTRY BOXES
    frame1=Frame(returntop,bg="black")
    frame1.place(relx=0.09,rely=0.29,relwidth=0.82,relheight=0.52)

    #CREATING FRAME FOR ENTRY BOXES
    labelFrame = Frame(returntop,bg='#f0cfa5')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    #CREATING LABEL Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='#f0cfa5', fg='black')
    lb1.place(relx=0.05,rely=0.5)

    #CREATING ENTRY BOX FOR Book ID
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #CREATING BLACK FRAME FOR SUBMIT BUTTON
    frame2=Frame(returntop,bg="black")
    frame2.place(relx=0.2765,rely=0.895,relwidth=0.185,relheight=0.085)

    #CREATING SUBMIT BUTTON
    SubmitBtn = Button(returntop,text="Return",bg='#f0cfa5', fg='black',command=returnn)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    #CREATING BLACK FRAME FOR QUIT BUTTON
    frame3=Frame(returntop,bg="black")
    frame3.place(relx=0.5265,rely=0.895,relwidth=0.185,relheight=0.085)

    #CREATING QUIT BUTTON
    quitBtn = Button(returntop,text="Quit",bg='#f0cfa5', fg='black', command=returntop.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    returntop.mainloop()
