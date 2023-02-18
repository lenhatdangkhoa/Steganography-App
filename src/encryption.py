import tkinter as tk
from settings import *
from PIL import ImageTk, Image

"""
Encrypt a secret message into the given image.

Parameters
----------
filepath : str
    The relative or absolute path to the image.
secret_message: str
    The message the user wants to hide.

Returns
---------
image: Image
    A copy of the original image with the hidden message
"""


def encrypt(filepath, secret_message):
    image = Image.open(filepath)
    HIDDEN_MESSAGE = "$t3g0"  # A placeholder, put at end of string
    HIDDEN_BIN = ""
    # Convert HIDDEN_MESSAGE into binary
    for i in range(len(HIDDEN_MESSAGE)):
        temp_bit_count = 8 - len(bin(ord(HIDDEN_MESSAGE[i]))[2:])
        # Some characters will be less than 8 bits. Add 0s to the left if needed.
        for j in range(temp_bit_count):
            HIDDEN_BIN += "0"
        # bin(ord(...)) returns byte string that start with 0b. Must use [2:]
        HIDDEN_BIN += bin(ord(HIDDEN_MESSAGE[i]))[2:]
    message = secret_message  # Word to be encoded
    binary_string = ""  # Binary representation of word
    arr = list(image.getdata())  # list of tuples (R, G, B) or (R, G, B, A)
    if image.mode == "RGBA":  # A for alpha (transparency)
        mode = 4
    else:
        mode = 3

    # Convert each character into binary and add them to binary_string
    for i in range(len(message)):
        temp_bit_count = 8 - len(bin(ord(message[i]))[2:])
        for j in range(temp_bit_count):
            binary_string += "0"
        binary_string += bin(ord(message[i]))[2:]

    # IMPORTANT!! Added the binary represenation of $t3g0 at the end
    binary_string += HIDDEN_BIN

    # check if image is large enough to contain string
    if len(binary_string) > len(arr) * mode:
        print("Message does not fit the image")
    else:
        binary_string = list(binary_string)
        if image.mode == "RGB":
            iteration = 0
            for x in range(image.width):
                for y in range(image.height):
                    r, g, b = image.getpixel((x, y))
                    r = list(bin(r))
                    g = list(bin(g))
                    b = list(bin(b))
                    # stop iterating at the end of the binary_string
                    if iteration == len(binary_string):
                        break
                    # Change each least significant bit to the bit of binary string
                    if r[-1] != binary_string[iteration]:
                        r[-1] = binary_string[iteration]
                    if g[-1] != binary_string[iteration + 1]:
                        g[-1] = binary_string[iteration + 1]
                    if b[-1] != binary_string[iteration + 2]:
                        b[-1] = binary_string[iteration + 2]

                    # Convert rgb to base from base 2 to base 10
                    r = int("".join(r), 2)
                    g = int("".join(g), 2)
                    b = int("".join(b), 2)
                    # put the new pixel in the image
                    image.putpixel((x, y), (r, g, b))
                    iteration += 3
        else:
            iteration = 0
            for x in range(image.width):
                for y in range(image.height):
                    r, g, b, a = image.getpixel((x, y))
                    r = list(bin(r))
                    g = list(bin(g))
                    b = list(bin(b))
                    a = list(bin(a))
                    if iteration == len(binary_string):
                        break
                    # Change each least significant bit to the bit of binary string
                    if r[-1] != binary_string[iteration]:
                        r[-1] = binary_string[iteration]
                    if g[-1] != binary_string[iteration + 1]:
                        g[-1] = binary_string[iteration + 1]
                    if b[-1] != binary_string[iteration + 2]:
                        b[-1] = binary_string[iteration + 2]
                    if a[-1] != binary_string[iteration + 3]:
                        a[-1] = binary_string[iteration + 3]

                    # Convert rgba to base from base 2 to base 10
                    r = int("".join(r), 2)
                    g = int("".join(g), 2)
                    b = int("".join(b), 2)
                    a = int("".join(a), 2)
                    # put the new pixel in the image
                    image.putpixel((x, y), (r, g, b, a))
                    iteration += 4

    return image


"""
Decrypt the secret message from the given image.

Parameters
----------
filepath : str
    The relative or absolute path to the image.

Returns
---------
decoded_message: str
    The hidden message.
"""


def decrypt(filepath):
    image = Image.open(filepath)
    encrypted_bin = ""
    # Get all the least signficant bit of the image
    if image.mode == "RGB":
        for x in range(image.width):
            for y in range(image.height):
                r, g, b = image.getpixel((x, y))
                encrypted_bin += bin(r)[-1] + bin(g)[-1] + bin(b)[-1]
    else:
        encrypted_bin = ""
        for x in range(image.width):
            for y in range(image.height):
                r, g, b, a = image.getpixel((x, y))
                encrypted_bin += bin(r)[-1] + bin(g)[-1] + \
                    bin(b)[-1] + bin(a)[-1]
    decoded_message = ""
    has_stego = False  # contains $t3g0
    for i in range(0, len(encrypted_bin), 8):
        # convert 1 byte of encrypted_bin to a character
        decoded_message += chr(int(encrypted_bin[i:i+8], 2))
        # if reached $t3g0, stop iterating
        if len(decoded_message) >= 5 and decoded_message[-5:] == "$t3g0":
            has_stego = True
            break
    if has_stego:
        decoded_message = decoded_message[0:len(decoded_message) - 5]
        return decoded_message
    else:  # contains garbage random value
        return decoded_message[0:250]
