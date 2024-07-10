import tkinter
from tkinter.constants import  RAISED
from PIL import Image,ImageTk
from book_reader import book_reader
#exite function
def exit():
    root=tkinter.Tk()
    root.geometry("400x200")
    root.minsize(400,200)
    root.maxsize(400,200)
    root.title("Exit")
    root.configure(background="white")
    l1=tkinter.Label(root,text="Do you want to exit",font=("ariel",19,"bold"),pady=20,background="white")
    l1.pack()
    b1=tkinter.Button(root,activebackground="Red",activeforeground="white",background="white",text="Exit",relief=RAISED,border=3,height=2,width=10)
    b1.pack()
    b1.place(relx=0.2,rely=0.6)
    b2=tkinter.Button(root,activebackground="blue",activeforeground="black",background="white",text="Cancel",relief=RAISED,border=3,height=2,width=10)
    b2.pack()
    b2.place(relx=0.6,rely=0.6)
    root.mainloop()




screen=tkinter.Tk()

#setting the scren size
screen.geometry("1200x700")
screen.minsize(1200,700)
screen.maxsize(1200,700)
screen.title("UNi")
screen.configure(bg="#FEFEFE")


#using logo in background
bg_load=Image.open('logo.jpg')
bg_pic=ImageTk.PhotoImage(image=bg_load)
bg=tkinter.Label(image=bg_pic)
bg.pack()
bg.place(relx=0.23,rely=0.27)

#using labrl for name prestation
member=tkinter.Label(text="-:Submitted by:-",font=("comicsense",28,"bold"),padx=40,pady=20,border=3,bg="white")
member.pack()
member.place(relx=0.20,rely=0.5)
member_name=tkinter.Label(text="Priyanshu Kumar Pal",font=("Arial",17),padx=20,pady=20,bg="#FFFAFF")
member_name.pack()
member_name.place(relx=0.195,rely=0.6)

#making button
b1=tkinter.Button(screen,activebackground="white",activeforeground="black",background="grey",text="book reader",relief=RAISED,border=3,height=2,width=30,command=book_reader)
b1.pack()
b1.place(relx=0.66,rely=0.28)
b2=tkinter.Button(screen,activebackground="black",activeforeground="white",background="grey",text="Event msg",relief=RAISED,border=3,height=2,width=30)
b2.pack()
b2.place(relx=0.66,rely=0.38)
b3=tkinter.Button(screen,activebackground="green",activeforeground="black",background="grey",text="Event msg",relief=RAISED,border=3,height=2,width=30)
b3.pack()
b3.place(relx=0.66,rely=0.48)
b4=tkinter.Button(screen,activebackground="blue",activeforeground="red",background="grey",text="Event msg",relief=RAISED,border=3,height=2,width=30)
b4.pack()
b4.place(relx=0.66,rely=0.58)
b5=tkinter.Button(screen,command=exit,activebackground="red",activeforeground="white",background="grey",text="Exit",relief=RAISED,border=3,height=2,width=30)
b5.pack()
b5.place(relx=0.66,rely=0.68)



#main loop
if __name__=="__main__":
    screen.mainloop()
