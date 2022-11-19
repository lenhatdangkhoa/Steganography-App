import tkinter as tk
from settings import *
from PIL import ImageTk, Image
import os
from tkinter import filedialog as fd

image = Image.open("assets/background.png")

image.putalpha(45)
image.save("assets/edited_background.png")
image.show()


