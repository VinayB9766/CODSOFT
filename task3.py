
from tkinter import *
import pyperclip
import random

viny = Tk()

viny.geometry("400x400")  
viny.title("PassGenerator")
viny.configure(background='grey')


passstr = StringVar()

passlen = IntVar()
passlen.set(0)



def generate():
    
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')']

    
    password = ""

   
    for x in range(passlen.get()):
        password = password + random.choice(pass1)

    
    passstr.set(password)


def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)
    Label(viny,text="Copied to clipboard",bg="red").pack(pady=6)


img = PhotoImage(file="E:\\tasks images\\Back1.png")
Label(viny,image=img,bg="#32405b").place(x=0,y=0)


Label(viny, text="Password Generator ", font="Arial 20 bold").pack()

Label(viny, text="Enter password length", bg='Blue', fg='white').pack(pady=3)

Entry(viny, textvariable=passlen).pack(pady=3)

Button(viny, text="Generate Password", command=generate, bg='yellow', fg='black').pack(pady=7)

Entry(viny, textvariable=passstr).pack(pady=3)

Button(viny, text="Copy to clipboard", command=copytoclipboard, bg='black', fg='white').pack()


viny.mainloop()