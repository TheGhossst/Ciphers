from tkinter import *
from encrypt import encrypt
from decrypt import decrypt

def encryptThis():
    plain_text = plainTextTextBox.get()
    key = keyTextBox.get()
    cipher_text = encrypt(plain_text, key)
    cipherTextTextBox.delete(0, END)  
    cipherTextTextBox.insert(0, cipher_text)
    
def decryptThis():
    cipher_text = cipherTextTextBox.get()
    key = keyTextBox.get()
    plain_text = decrypt(cipher_text, key)
    plainTextTextBox.delete(0, END)  
    plainTextTextBox.insert(0, plain_text)

window = Tk()
window.title("Vigenere Cipher")
window.geometry("800x400")

heading = Label(window, text= "Vigenere Cipher",font = ("Arial", 25,"bold","underline"))
heading.pack(side = "top")

plainText = Label(window, text="Enter Plain Text: ",font =  ("Arial",16))
plainText.pack(side = "top",  anchor ="w")

plainTextTextBox = Entry(window, font=("Arial", 14))
plainTextTextBox.pack(side="top", padx=10, pady=10, fill="x")

keyLabel =  Label(window,text="Enter Key (a-z): ",font = ("Arial",16))
keyLabel.pack(side = "top",anchor="w")

keyTextBox = Entry(window, font=("Arial", 14))
keyTextBox.pack(side="top", padx=10, pady=10, fill="x")

cipherText = Label(window,text= "Enter Cipher Text :  ",font = ("Arial",16))
cipherText.pack(side = "top",anchor = "w")

cipherTextTextBox = Entry(window, font=("Arial", 14))
cipherTextTextBox.pack(side="top", padx=10, pady=10, fill="x")

encryptButton = Button(window, text="Encrypt", command=encryptThis)
encryptButton.pack(side="top", pady=10)

decryptButton = Button(window, text="Decrypt", command=decryptThis)
decryptButton.pack(side="top", pady=10)

window.mainloop()
