import tkinter as tk
from settings import *
from PIL import ImageTk, Image
import os
from tkinter import filedialog as fd

window = tk.Tk()

def openimage():
    return fd.askopenfilename(filetypes=(("png files", "*.png"), ("all files", "*.*")))

myimage = ImageTk.PhotoImage(Image.open(openimage()))
    
label = tk.Label(window, image=myimage).pack()

button = tk.Button(window, text="Open", width = 15, background="white", command=openimage).pack()



window.mainloop()