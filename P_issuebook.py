from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector as sqltor

#CONNECTING SQL TP PYTHON
con = sqltor.connect(host="localhost",user="root",password="4.4.2020ruthless",database="library")
cur = con.cursor()

#LIST TO STORE ALL BOOK IDS
allBid = [] 
def issue():
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,window,Canvas,status

    #RETREIVING DATA FROM ENTRY BOXES
    bid= inf1.get()
    issueto = inf2.get()
    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    
    #ISSUEING BOOKS
    cur.execute("select bid from books")
    data=cur.fetchall()
    con.commit()
    
    for i in data:
        allBid.append(i[0])
    if bid in allBid:
        cur.execute("select status from books where bid = '"+bid+"'")
        data2=cur.fetchall()
        con.commit()
        for j in data2:
            if j[0] == 'avail':
                status = True
            else:
                status = False
    else:
        messagebox.showinfo("Error","Book ID not present")
   
    if bid in allBid and status == True:
        cur.execute("insert into books_issued values ('"+bid+"','"+issueto+"')")#issue sql
        con.commit()
        cur.execute("update books set status = 'issued' where bid = '"+bid+"'")#update status
        con.commit()
        messagebox.showinfo('Success',"Book Issued Successfully")
        window4.destroy()
    elif bid in allBid and status == False:
        allBid.clear()
        messagebox.showinfo('Message',"Book Already Issued")
        window4.destroy()
        return
    else:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")

    print(bid)
    print(issueto)
    
    allBid.clear()
    
def issueBook(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitbtn,window4,canvas,status,issuetop
    
    
    #CREATING WINDOW
    issuetop=Toplevel()
    issuetop.title("Library")
    issuetop.geometry("600x500")

    #IMPORTING AND RESIZING IMAGE FOR MAIN WINDOW BACKGROUND
    img4=Image.open('C:\\Users\\Dell\\Documents\\Python Project\\Library management (MAIN)\\books.jpg')
    img4=img4.resize((600,500),Image.ANTIALIAS)
    newimg4=ImageTk.PhotoImage(img4)

    #CREATING CANVAS
    canvas4=Canvas(issuetop)
    canvas4.create_image(300,250,image=newimg4)
    canvas4.pack(expand=True,fill=BOTH)
    
    #CREATING BLACK HEADING FRAME
    headingFrame1 = Frame(issuetop,bg="black",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)       

    #CREATING BEIGE LABEL WITH BLACK TEST
    headingLabel = Label(headingFrame1, text="Issue Book", bg="#f0cfa5", fg='black', font=("Comic Sans MS",15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    #CREATING BLACK FRAME FOR ENTRY BOXES
    frame1 = Frame(issuetop,bg="black",bd=5)
    frame1.place(relx=0.089,rely=0.289,relwidth=0.82,relheight=0.52)       

 
    #CREATING LABEL FOR ENTRY BOXES
    labelFrame= Frame(issuetop,bg="#f0cfa5")
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  

    #CREATING LABEL Book ID FOR ENTRY BOX
    lb1 = Label(labelFrame,text="Book ID : ", bg="#f0cfa5", fg='black')
    lb1.place(relx=0.05,rely=0.2)

    #CREATING ENTRY BOX FOR Book ID
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)

    #CREATING LABEL Issued To FOR ENTRY BOX
    lb2 = Label(labelFrame,text="Issued To : ", bg="#f0cfa5", fg='black')
    lb2.place(relx=0.05,rely=0.4)

    #CREATING ENTRY BOX FOR Issued To
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)

    #CREATING BLACK FRAME FOR ISSUE BUTTON
    frame2=Frame(issuetop,bg="black")
    frame2.place(relx=0.2765,rely=0.895,relwidth=0.185,relheight=0.085)

    #CREATING ISSUE BUTTON
    issueBtn = Button(issuetop,text="Issue",bg='#f0cfa5', fg='black',command=issue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    #CREATING BLACK FRAME FOR QUIT BUTTON
    frame3=Frame(issuetop,bg="black")
    frame3.place(relx=0.5265,rely=0.895,relwidth=0.185,relheight=0.085)

    #CREATING QUIT BUTTON
    quitbtn = Button(issuetop,text="Quit",bg='#f0cfa5', fg='black', command=issuetop.destroy)
    quitbtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    issuetop.mainloop()
