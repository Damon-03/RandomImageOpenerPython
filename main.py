import random
import os

def imageSelect(dir):
    files = os.listdir(dir) #loads file in memory
    d = random.choice(files) #randomly selects file
    os.startfile("{}\{}".format(dir, d)) # opens file
loop = True
while loop:
    direct = input("Enter Folder number: ")

#D:\Refrences\Folder "x" is just on my computer feel free to edit it
    if direct == "1": # My program will randomly open a file from a folder you specify
        imageSelect("D:\Refrences\Folder 1")
    elif direct == "2":
        imageSelect("D:\Refrences\Folder 2")
    elif direct == "3":
        imageSelect("D:\Refrences\Folder 3")
    elif direct == "4":
        imageSelect("D:\Refrences\Folder 4")
    elif direct == "5":
        imageSelect("D:\Refrences\Folder 5")
    elif direct == "x":
        loop = False
    else:
        print("Directory not found: ")

