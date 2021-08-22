# Importing

import os
import time
import colorama
import webbrowser as wb
import ctypes

# Variables

normal = "\u001b[0m"

red = "\u001b[31m"
green = "\u001b[32m"
yellow = "\u001b[33m"
blue = "\u001b[34m"
purple = "\u001b[35m"
cyan = "\u001b[36m"

# Function

def cprint(string):
    print(yellow + ":: " + normal + string)
# ---------------------------------------------
def scprint(string):
    print(yellow + "    - " + normal + string)
# ---------------------------------------------
def cerror(string):
    print(red + "#: " + normal + string)
# ---------------------------------------------
def scerror(string):
    print(red + "    #- " + normal + string)
# ---------------------------------------------
def cinfo(string):
    print(blue + "?> " + normal + string)
# ---------------------------------------------
def scinfo(string):
    print(blue + "    ?> " + normal + string)
# ---------------------------------------------
def cinput(string):
    input(yellow + ":: " + normal + string)
# ---------------------------------------------
def scinput(string):
    input(yellow + "    - " + normal + string)
# ---------------------------------------------
def cmdinput(string):
    input(green + ">> " + normal + string)
# ---------------------------------------------
def cls():
    os.system("cls")
# ---------------------------------------------
def wait(string): # lol just in case i get mixed up with lua
    time.sleep(string)

# Check

def get_user():
    return os.getenv('USER', os.getenv('USERNAME', 'user'))

def filexists(filePathAndName):
    return os.path.exists(filePathAndName)

if filexists("C:/Users/"+get_user()+"/Desktop/Files/Python/Python/Projects/advanced/hacking_tools/data_folder-main/data_folder-main/data_folder/.py"):
    print("attempting to open file")
    time.sleep(.5)
    os.startfile("C:/Users/"+get_user()+"/Desktop/Files/Python/Python/Projects/advanced/hacking_tools/data_folder-main/data_folder-main/data_folder/.py")
elif filexists("C:/Users/"+get_user()+"/Desktop/Files/Python/Python/Projects/advanced/hacking_tools/data_folder-main/data_folder-main/data_folder/ .py"):
    print("attempting to open file")
    time.sleep(.5)
    os.startfile("C:/Users/"+get_user()+"/Desktop/Files/Python/Python/Projects/advanced/hacking_tools/data_folder-main/data_folder-main/data_folder/ .py")
else:
    print("installing file")
    wb.open("https://github.com/buuinstalls/data_folder/archive/refs/heads/main.zip", "C:/Users/"+get_user()+"/Desktop/Files/Python/Python/Projects/advanced/hacking_tools/")
    time.sleep(.5)