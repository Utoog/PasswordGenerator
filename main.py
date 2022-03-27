from tkinter import *
import random as r
import pyperclip

root = Tk()
root.geometry("330x220")
root.title("Password generator")
root.resizable(False, False)
frame = Frame(root)

ctAl = IntVar()
ctDig = IntVar()
ctSp = IntVar()


def generate(ln):
    global res
    result.pack()
    copybtn.pack()
    alpha = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    digits = "0123456789"
    special = "!@#$%^&*()-_+=?"
    x = str()
    if ctAl.get() == 1: x += alpha
    if ctDig.get() == 1: x += digits
    if ctSp.get() == 1: x += special
    res = str()
    if len(x) != 0:
        for _ in range(ln): res += x[r.randint(0, len(x) - 1)]
    result.config(text=f"Password: \n{res}")


lenEn = Entry(root)
lenEn.insert(0, "32")
contAl = Checkbutton(root, text="Contains letters", variable=ctAl)
contDig = Checkbutton(root, text="Contains numbers", variable=ctDig)
contSp = Checkbutton(root, text="Contains special chars", variable=ctSp)
generatebtn = Button(root, text="Generate", command=lambda: generate(int(lenEn.get())))
result = Label(root, text="Result:")
copybtn = Button(root, text="Copy", command=lambda: pyperclip.copy(res))

Label(root, text="Password length:").pack()
lenEn.pack()
contAl.pack()
contDig.pack()
contSp.pack()
generatebtn.pack()


root.mainloop()
