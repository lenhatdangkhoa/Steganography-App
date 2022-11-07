import tkinter as tk
from settings import *

class Steganography:
    def __init__(self):
        self.setting = Setting()
        self.window = tk.Tk()
        self.window.geometry(f"{self.setting.width}x{self.setting.height}")
 

    def run(self):
        self.window.mainloop()