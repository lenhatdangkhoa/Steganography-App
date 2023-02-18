from PIL import ImageTk, Image
import tkinter as tk
from PIL import Image

"""
This is the setting class and it is the default setting of the app.
This helps making changes easier.
"""


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
        # check whether of not the user has picked a path to the image
        self.has_path_label = False
        self.max_image_width = 200
        self.max_image_height = 200
        self.encrypt_mode = True  # check which mode the user is on
