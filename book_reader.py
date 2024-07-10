import tkinter
from tkinter import Button, Label, filedialog
from tkinter.constants import X,Y,RAISED
from PIL import Image
import PIL.Image
import PIL.ImageTk
import pytesseract
from pyttsx3 import speak
import pyttsx3
#universel variable
#Window screen
root=tkinter.Tk()
root.geometry("400x400")
root.minsize(400,400)
root.maxsize(400,400)
root.configure(bg="#FEFEFE")
root.title("Book Reader")
scren_title=tkinter.Label(text="Book Reader",font=("comicsense",19,"bold"),bg="#FEFEFE",pady=20)
scren_title.pack()

#screen label 
image = PIL.Image.open('book.jpg')
photo = PIL.ImageTk.PhotoImage(image)
label = tkinter.Label(root, image=photo)
label.place(x=90, y=60, height=230, width=230)
#open box
def open_a_file():
    location=filedialog.askopenfilename(initialdir="C:/Users/Abhay Singh/Pictures",title="Select An Iamge",filetypes=[("jpg",".jpg"),("png",".pmg"),("jpeg",".jpeg")])
    speak(location)
#text to speech
def speak(location):
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    img=Image.open(location)
    output=pytesseract.image_to_string(img)
    print(output)
    text_to_speech = pyttsx3.init()
    text_to_speech.say(output)
    text_to_speech.runAndWait()
#creating the open button
b1=tkinter.Button(root,activebackground="Red",activeforeground="white",background="white",text="Open",relief=RAISED,border=3,height=2,width=30,command=open_a_file)
b1.pack()
b1.place(x=95,y=300)
def book_reader():
    root.mainloop()

book_reader()
