import tkinter as tk
from settings import *
from PIL import ImageTk, Image

class Steganography:
    def __init__(self):
        self.setting = Setting()
        self.window = tk.Tk()
        self.window.geometry(f"{self.setting.width}x{self.setting.height}")
        self.window.iconbitmap(self.setting.icon)
        self.window.title(self.setting.title)
        self.define_app_content()

    def run(self):
        self.window.mainloop()

    def define_app_content(self):
        self.title_in_app = tk.Label(self.window, 
        text = self.setting.title, 
        font=("Century Gothic", self.setting.title_font_size)).place(x=40,y=2)
        self.logo = ImageTk.PhotoImage(Image.open(self.setting.icon))
        self.logo_label = tk.Label(image=self.logo).place(x=7,y=4)
        self.button = tk.Button(self.window, text="Open", width = 15, command=None)
        self.button.bind("<Enter>", self.on_enter)
        self.button.bind("<Leave>", self.on_leave)
        self.button.place(x=850,y = 15)

    def on_enter(self, e):
        self.button.config(background="red", foreground="black")

    def on_leave(self, e):
        self.button.config(background="SystemButtonFace", foreground="black")




