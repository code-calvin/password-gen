from tkinter import *
import random
import pyperclip

def gen_pass():
    length = int(input_.get())
    characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g' 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '`', '!', '@', "#", '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '<', '>', '/', '"', ';', ':', '|']
    pass_ = []
    
    for x in range(length):
        char = random.choice(characters)
        pass_.append(char)
    Pass.config(text=''.join(pass_))
    pyperclip.copy(''.join(pass_))
    Pass.grid(row=1, column=0)

if __name__ == "__main__":

    # Create Main Window
    root = Tk()
    root.title("Password Generator Tutorial")
    root.geometry("800x600")

    # Create Labels and Widgets

    # Question Label. How many characters should this password have
    # Entry widget take the number of characters
    # Button to generate a password
    # Label to display password
    Label(root, text="How many characters should this password be?", fg="red").grid(row=0, column=0)
    input_ = Entry(root, fg="red")
    gen_btn = Button(root, text="Generate Pass", fg="red", command=gen_pass)
    Pass = Label(root)

    input_.grid(row=0, column=1, padx=15)
    gen_btn.grid(row=1, column=1)

    root.mainloop()