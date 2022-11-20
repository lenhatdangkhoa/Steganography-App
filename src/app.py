import tkinter as tk
from settings import *
from PIL import ImageTk, Image
from tkinter import filedialog as fd
from encryption import *


class Steganography:      
    def __init__(self):
        self.setting = Setting()
        self.window = tk.Tk()
        self.window.geometry(f"{self.setting.width}x{self.setting.height}")
        self.window.iconbitmap(self.setting.icon)
        self.window.title(self.setting.title)
        self.background_image = tk.PhotoImage(file=self.setting.background_image)
        self.background_image_label = tk.Label(self.window, background="black", image=self.background_image)
        self.background_image_label.place(x=0,y=0)
        self.define_app_content()


    def define_app_content(self):
        self.title_in_app = tk.Label(self.window, 
        text = self.setting.title, background="black", foreground="white",
        font=("Century Gothic", self.setting.title_font_size)).place(x=45,y=2)
        self.logo = ImageTk.PhotoImage(Image.open(self.setting.icon))
        self.logo_label = tk.Label(image=self.logo, borderwidth=0).place(x=7,y=4)
        self.button_image = ImageTk.PhotoImage(Image.open(self.setting.button_image))
        self.encrypt_button_image = Image.open(self.setting.encrypt_image).resize((33,38))
        self.encrypt_button_image = ImageTk.PhotoImage(self.encrypt_button_image)
        self.decrypt_button_image = Image.open(self.setting.decrypt_image).resize((30,35))
        self.decrypt_button_image = ImageTk.PhotoImage(self.decrypt_button_image)
        self.padlock_green = tk.Button(self.window, width = 30, height = 35, background="black", borderwidth=0, image = self.encrypt_button_image, activebackground="black")
        self.padlock_green.place(x=750,y=25)
        self.padlock_red = tk.Button(self.window, width = 65, height = 35, background="black", borderwidth=0, image = self.decrypt_button_image, activebackground="black")
        self.padlock_red.place(x=685,y=25)
        self.button = tk.Button(self.window, text="Open", width = 60, height=60, background="black", borderwidth=0, image=self.button_image, command=self.open_image)
        self.button.place(x=850,y = 15)
        self.padlock_red.bind("<Enter>")

    def run(self):
        self.window.mainloop()

    # Change color of button when cursor is on top
    def on_enter(self, e):
        self.button.config(background="black", foreground="black")

    # Change color of button back to normal when cursor leaves
    def on_leave(self, e):
        self.button.config(background="black", foreground="black")

    # Get file path from the user <3
    def open_image_path(self):
        self.image_path = fd.askopenfilename()
        prompt_label = tk.Label(self.window, text="Enter text to be encrypted",width= 58, background="white")
        prompt_label.place(x=500,y=100)
        if (not self.setting.has_path_label):
            self.path_label = tk.Label(text=self.image_path,background="black", foreground="white")
            self.path_label.place(x=5, y=45)
            self.setting.has_path_label = True
        else:
            self.path_label.destroy()
            self.path_label = tk.Label(text=self.image_path,background="black", foreground="white")
            self.path_label.place(x=5, y=45)
            self.setting.has_path_label = False
        return self.image_path
    
    def open_image(self):
        self.image_path = self.open_image_path()
        self.app_image = Image.open(self.image_path).resize((250,250))
        self.app_image = ImageTk.PhotoImage(self.app_image)
        self.image_label = tk.Label(self.window,image=self.app_image)
        self.image_label.config(highlightbackground="gray", highlightcolor="grey", highlightthickness=4)
        self.image_label.place(x=0,y=100)
        self.encrypt_button = tk.Button(self.window, text="Encrypt", background="white", width=58, height=2, command=self.encrypt_image)
        self.encrypt_button.place(x=500,y=305)
        self.get_user_input()

    def get_user_input(self):
        self.text_box = tk.Text(self.window, width=51, height=10)
        self.text_box.place(x=500,y=125)

    def encrypt_image(self):
        message = self.text_box.get(1.0,"end-1c")
        image_to_save = encrypt(self.image_path, message)
        filetypes = [("All Files", "*.*"), ("PNG Files", "*.png")]
        filename = fd.asksaveasfile(mode="w", defaultextension=".png", filetypes=filetypes)
        if not image_to_save:
            print("An error has occured when saving the image")
            return
        image_to_save.save(filename.name)

        



  


        




