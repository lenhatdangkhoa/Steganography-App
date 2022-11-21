import tkinter as tk
from settings import *
from PIL import ImageTk, Image

def encrypt(filepath, secret_message):
    image = Image.open(filepath)
    HIDDEN_MESSAGE = "$t3g0"
    HIDDEN_BIN = ""
    for i in range(len(HIDDEN_MESSAGE)):
        temp_bit_count = 8 - len(bin(ord(HIDDEN_MESSAGE[i]))[2:])
        for j in range(temp_bit_count):
            HIDDEN_BIN += "0"
        HIDDEN_BIN += bin(ord(HIDDEN_MESSAGE[i]))[2:]

    message = secret_message # Word to be encoded
    binary_string = "" # Binary representation of word
    arr = list(image.getdata()) # array of pixels (RGB)
    if image.mode == "RGBA":
        mode = 4
    else:
        mode = 3
    for i in range(len(message)):
        temp_bit_count = 8 - len(bin(ord(message[i]))[2:])
        for j in range(temp_bit_count):
            binary_string += "0"
        binary_string += bin(ord(message[i]))[2:]

    binary_string += HIDDEN_BIN # IMPORTANT!! Added the binary represenation of $t3g0 at the end 

    if len(binary_string) > len(arr) * mode:
        print("Message does not fit the image")
    else:
        image_lsb = ""
        for i in range(len(arr)):
            for value in arr[i]:
                image_lsb += bin(value)[-1]
        binary_string = list(binary_string)
        image_lsb = list(image_lsb)
        for i in range(len(binary_string)):
            if binary_string[i] != image_lsb[i]:
                image_lsb[i] = binary_string[i]
        
        if image.mode == "RGB":
            iteration = 0
            for x in range(image.width):
                for y in range(image.height):
                    r,g,b = image.getpixel((x,y))
                    r = list(bin(r))
                    g = list(bin(g))
                    b = list(bin(b))
                    if iteration == len(image_lsb): 
                        break
                    if r[-1] != image_lsb[iteration]:
                        r[-1] = image_lsb[iteration]
                    if g[-1] != image_lsb[iteration + 1]:
                        g[-1] = image_lsb[iteration + 1]
                    if b[-1] != image_lsb[iteration + 2]:
                        b[-1] = image_lsb[iteration + 2]
                    r = int("".join(r), 2)
                    g = int("".join(g), 2)
                    b = int("".join(b), 2)
                    image.putpixel((x,y), (r,g,b))
                    iteration += 3
        else:
            iteration = 0
            for x in range(image.width):
                for y in range(image.height):
                    r,g,b,a = image.getpixel((x,y))
                    r = list(bin(r))
                    g = list(bin(g))
                    b = list(bin(b))
                    a = list(bin(a))
                    if iteration == len(image_lsb): 
                        break
                    if r[-1] != image_lsb[iteration]:
                        r[-1] = image_lsb[iteration]
                    if g[-1] != image_lsb[iteration + 1]:
                        g[-1] = image_lsb[iteration + 1]
                    if b[-1] != image_lsb[iteration + 2]:
                        b[-1] = image_lsb[iteration + 2]
                    if a[-1] != image_lsb[iteration + 3]:
                        a[-1] = image_lsb[iteration + 3]
                    r = int("".join(r), 2)
                    g = int("".join(g), 2)
                    b = int("".join(b), 2)
                    a = int("".join(a), 2)
                    image.putpixel((x,y), (r,g,b,a))
                    iteration += 4

    return image
def decrypt(filepath):
    image = Image.open(filepath)
    encrypted_bin = ""
    if image.mode == "RGB":
        for x in range(image.width):
            for y in range(image.height):
                r,g,b = image.getpixel((x,y))
                encrypted_bin += bin(r)[-1] + bin(g)[-1] + bin(b)[-1]
    else:
        encrypted_bin = ""
        for x in range(image.width):
            for y in range(image.height):
                r,g,b,a = image.getpixel((x,y))
                encrypted_bin += bin(r)[-1] + bin(g)[-1] + bin(b)[-1] + bin(a)[-1]
    decoded_message = ""
    has_stego = False
    for i in range(0,len(encrypted_bin),8):
        decoded_message += chr(int(encrypted_bin[i:i+8], 2))
        if len(decoded_message) >= 5 and decoded_message[-5:] == "$t3g0":
            has_stego = True
            break
    if has_stego:
        decoded_message = decoded_message[0:len(decoded_message) - 5]
        return decoded_message
    else:
        return decoded_message[0:200]

