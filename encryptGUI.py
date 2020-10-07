from tkinter import *
from cryptography.fernet import Fernet
import tkinter as tk

root = Tk()
root.geometry("800x800")
root.title("Simple's (En/De)Cryptor")
root.iconbitmap(#IMPORT LOGO HERE -> r"")
ebox = Entry(root, width = 50)
fbox = Entry(root, width = 50)

#Start of commands

key = "4TgrL-_WTm2RSuVkeF91MyNQnLQJniilNvPtEKnRAXk="
encryption_type = Fernet(key)

def encrypt():
    global e
    message = message = ebox.get()
    encrypted_message = encryption_type.encrypt(message.encode('utf-8'))
    print("-------------------------------------------------------------------------------")
    print(encrypted_message)
    print("-------------------------------------------------------------------------------")
    decrypted_message = encryption_type.decrypt(encrypted_message)
    print(decrypted_message)
    logbox.insert(END, b"Encrypted:\n-------------------------------------------- " + encrypted_message + b"\n--------------------------------------------")

def decrypt():
    global e1
    message = message = fbox.get()
    decrypted_message = encryption_type.decrypt(message.encode('utf-8'))
    print("-------------------------------------------------------------------------------")
    print(decrypted_message)
    print("-------------------------------------------------------------------------------")
    logbox.insert(END, b"Decrypted:\n-------------------------------------------- " + decrypted_message + b"\n--------------------------------------------")

#def submit():





#Creating a Label Widget
myLabel = Label(root, text = "Welcome to Simple's Encryption Software! - Questions? Email vinayven@yahoo.com")
myInstructions = Label(root, text = "Please select your Method")
#Shoving it onto the screen
myLabel.pack()
myInstructions.pack(pady=10)

button = Button(root, text="Encrypt", bg="#0052cc", fg="#ffffff", command=encrypt)
button1 = Button(root, text="Decrypt", bg="#0052cc", fg="#ffffff", command=decrypt)
l2 = Label(root, text="Logs: ")
logbox = Text(root, width=44, height=20, wrap=WORD)

button.pack(pady=40)
ebox.pack()
button1.pack(pady=40)
fbox.pack()
l2.pack(pady=5)
logbox.pack()
myLabel.pack()
root.mainloop()
