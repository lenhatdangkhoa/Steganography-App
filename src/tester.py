import tkinter as tk
from settings import *
from PIL import ImageTk, Image
import os
from tkinter import filedialog as fd
import time


image = Image.open("assets/push.png")

for x in range(image.width):
    for y in range(image.height):
        if image.getpixel((x,y))[0] == 246 and image.getpixel((x,y))[1] == 246 and image.getpixel((x,y))[2] == 246:
            image.putpixel((x,y), (0,0,0))
#print(image.mode)
image.save("assets/push.png")
#word = "abc"
#binary_string = ""
#val = image.getpixel((0,0))

#print(val[0])
"""
for i in range(len(word)):
    char_ascii = ord(word[i])
    binary_string += "0" + bin(char_ascii)[2:]

for i in range(0,len(binary_string), 8):
    print(chr(int(binary_string[i:i+8], 2)))

"""
