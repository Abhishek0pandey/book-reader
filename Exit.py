import tkinter
from tkinter.constants import RAISED, SUNKEN

root=tkinter.Tk()
root.geometry("400x200")
root.minsize(400,200)
root.maxsize(400,200)
root.title("Exit")
root.configure(background="white")
l1=tkinter.Label(text="Do you want to exit",font=("ariel",19,"bold"),pady=20,background="white")
l1.pack()
b1=tkinter.Button(root,activebackground="Red",activeforeground="white",background="white",text="Exit",relief=RAISED,border=3,height=2,width=10)
b1.pack()
b1.place(relx=0.2,rely=0.6)
b2=tkinter.Button(root,activebackground="blue",activeforeground="black",background="white",text="Cancel",relief=RAISED,border=3,height=2,width=10)
b2.pack()
b2.place(relx=0.6,rely=0.6)
def exit():
    root.mainloop()

exit()