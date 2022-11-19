import tkinter as tk
from settings import *
from PIL import ImageTk, Image
import os
from tkinter import filedialog as fd


class Steganography:      
    def __init__(self):
        self.setting = Setting()
        self.window = tk.Tk()
        self.window.geometry(f"{self.setting.width}x{self.setting.height}")
        self.window.iconbitmap(self.setting.icon)
        self.window.title(self.setting.title)
        self.define_app_content()


    def define_app_content(self):
        self.title_in_app = tk.Label(self.window, 
        text = self.setting.title, 
        font=("Century Gothic", self.setting.title_font_size)).place(x=40,y=2)
        self.logo = ImageTk.PhotoImage(Image.open(self.setting.icon))
        self.logo_label = tk.Label(image=self.logo).place(x=7,y=4)
        self.button = tk.Button(self.window, text="Open", width = 15, background="white", command=self.open_image)
        self.button.bind("<Enter>", self.on_enter)
        self.button.bind("<Leave>", self.on_leave)
        self.button.place(x=850,y = 15)

    def run(self):
        self.window.mainloop()

    # Change color of button when cursor is on top
    def on_enter(self, e):
        self.button.config(background="black", foreground="white")

    # Change color of button back to normal when cursor leaves
    def on_leave(self, e):
        self.button.config(background="white", foreground="black")

    # Get file path from the user <3
    def open_image_path(self):
        image_path = fd.askopenfilename()
        if (not self.setting.has_path_label):
            self.path_label = tk.Label(text=image_path,background="black", foreground="white")
            self.path_label.place(x=5, y=45)
            self.setting.has_path_label = True
        else:
            self.path_label.destroy()
            self.path_label = tk.Label(text=image_path,background="black", foreground="white")
            self.path_label.place(x=5, y=45)
            self.setting.has_path_label = False
        return image_path
    
    def open_image(self):
        self.image_path = self.open_image_path()
        self.app_image = ImageTk.PhotoImage(Image.open(self.image_path))
        self.app_image.height = self.setting.max_image_height
        self.app_image.width = self.setting.max_image_width
        self.image_label = tk.Label(self.window,image=self.app_image).place(x=0,y=100)



  


        




