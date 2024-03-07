from tkinter import *
from encrypt import encrypt

def encryptThis():
    plain_text = plainTextTextBox.get()
    key = keyTextBox.get()
    cipher_text = encrypt(plain_text, key)
    cipherTextTextBox.delete(0, END)  
    cipherTextTextBox.insert(0, cipher_text)

window = Tk()
window.title("Vigenere Cipher")
window.geometry("800x400")

heading = Label(window, text= "Vigenere Cipher",font = ("Arial", 25,"bold","underline"))
heading.pack(side = "top")

plainText = Label(window, text="Enter Plain Text: ",font =  ("Arial",16))
plainText.pack(side = "top",  anchor ="w")

plainTextTextBox = Entry(window, font=("Arial", 14))
plainTextTextBox.pack(side="top", padx=10, pady=10, fill="x")

key =  Label(window,text="Enter Key (a-z): ",font = ("Arial",16))
key.pack(side = "top",anchor="w")

keyTextBox = Entry(window, font=("Arial", 14))
keyTextBox.pack(side="top", padx=10, pady=10, fill="x")

cipherText = Label(window,text= "Enter Cipher Text :  ",font = ("Arial",16))
cipherText.pack(side = "top",anchor = "w")

cipherTextTextBox = Entry(window, font=("Arial", 14))
cipherTextTextBox.pack(side="top", padx=10, pady=10, fill="x")

encryptButton = Button(window, text="Encrypt", command=encryptThis)
encryptButton.pack(side="top", pady=10)

window.mainloop()
