#!/usr/bin/python3
def uppercase(str):
    char = ""
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            char += chr(ord(letter) - 32)
        else:
            char += letter
    print("{}".format(char))
