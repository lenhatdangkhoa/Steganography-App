from PIL import ImageTk, Image
import tkinter as tk
from PIL import Image

class Setting():
    def __init__(self):
        self.width = 1000
        self.height = 750
        self.background_image = "assets/edited_background.png"
        self.icon = "assets/hackingicon.ico"
        self.title = "Steganography Encryption"
        self.button_image = "assets/push.png"
        self.encrypt_image = "assets/redlock.png"
        self.decrypt_image = "assets/greenlock.png"
        self.title_font_size = 20
        self.has_path_label = False
        self.max_image_width = 200
        self.max_image_height = 200
        self.toggle_on = True
        
        

    