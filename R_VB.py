from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import ImageTk,Image

mycon=mysql.connector.connect(host="localhost",user="root",password="4.4.2020ruthless",database="library")
cur=mycon.cursor()

def View():
    global viewtop
  

    #CREATING WINDOW
    viewtop=Toplevel()
    viewtop.title("Library")
    viewtop.geometry("600x500")

    #IMPORTING AND RESIZING IMAGE FOR MAIN WINDOW BACKGROUND
    img3=Image.open('C:\\Users\\Dell\\Documents\\Python Project\\Library management (MAIN)\\books.jpg')
    img3=img3.resize((600,500),Image.ANTIALIAS)
    newimg3=ImageTk.PhotoImage(img3)

    #CREATING CANVAS
    canvas3=Canvas(viewtop)
    canvas3.create_image(300,250,image=newimg3)
    canvas3.pack(expand=True,fill=BOTH)

    #HEADING FRAME
    hdframe1=Frame(viewtop,bg="black",bd=4)
    hdframe1.place(relx=0.25,rely=0.1 ,relwidth=0.5 ,relheight=0.1)

    #HEADING LABEL
    hdlabel1=Label(hdframe1,bg="#f0cfa5",fg="black",text="View Books",font=("Comic Sans MS",15,'bold'))
    hdlabel1.place(relx=0 ,rely=0 ,relwidth=1.0 ,relheight=0.98 )

    #LISTBOX FRAME
    lblframe2=Frame(viewtop,bg="black")
    lblframe2.place(relx=0.1 ,rely=0.3 ,relwidth=0.8 ,relheight=0.5 )

    #LISTBOX LABEL
    lbllabel2=Label(lblframe2,bg="#f0cfa5")
    lbllabel2.place(relx=0.01 ,rely=0.018,relwidth=0.977 ,relheight=0.957 )

    #CONTENT HEADING LABEL
    lbllabel3=Label(lblframe2,fg="black",bg="#f0cfa5",text="%-10s%-40s%-30s%-20s"%('BID','Title','Author','Status'))
    lbllabel3.place(relx=0.01 ,rely=0.03 ,relwidth=0.9,relheight=0.1)

    #CONTENT HEADING DIVISION
    lbllabel4=Label(lblframe2,bg="#f0cfa5",fg="black",text="--------------------------------------------------------------------------")
    lbllabel4.place(relx=0.07,rely=0.1,relwidth=0.76 ,relheight=0.1 )
    y=0.06

    #FRAME FOR SCROLLBAR
    lblframe3=Frame(lblframe2,bg="#f0cfa5")
    lblframe3.place(relx=0.05 ,rely=0.2 ,relwidth=0.9 ,relheight=0.7 )
    sb=Scrollbar(lblframe3)
    sb.pack(side=RIGHT,fill=Y)

    try:
        #FETCH DATA FROM DATABASE
        cur.execute("select * from books")
        data=cur.fetchall()
        mycon.commit()

        #CREATING LISTBOX
        mylist = Listbox(lblframe3, yscrollcommand = sb.set,bg="#f0cfa5")

        #INSERTING DATA INTO LISTBOX
        for i in data:
            mylist.insert(END,"%-10s%-35s%-30s%-15s"%(i[0],i[1],i[2],i[3]))
        
        #PLACING LISTBOX
        mylist.place(relx=0.03 ,rely=0.002 ,relwidth=0.9 ,relheight=1.0 )  
        sb.config( command = mylist.yview )  
    except:
        messagebox.showinfo("Error","Failed to fetch files")

    #QUIT BUTTON FRAME
    hdframe1=Frame(viewtop,bg="black",bd=4)
    hdframe1.place(relx=0.3959,rely=0.845 ,relwidth=0.205 ,relheight=0.107)

    #QUIT BUTTON TO DESTROY WINDOW
    quitbtn=Button(viewtop,fg="black",bg="#f0cfa5",text="Quit",font=("Comic Sans MS",10),command=viewtop.destroy)
    quitbtn.place(relx=0.4 ,rely=0.85 ,relwidth=0.2 ,relheight= 0.1)    


    viewtop.mainloop()
   
    
