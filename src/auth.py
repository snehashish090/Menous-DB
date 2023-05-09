import json
from secrets import token_urlsafe
from pathlib import Path
import os
import getpass
import sys

if sys.platform == "darwin":
    if not os.path.exists("/Library/Caches/.menousdb"):
        os.mkdir("/Library/Caches/.menousdb")
    if not os.path.exists("/Library/Caches/.menousdb/authdata"):
        os.mkdir("/Library/Caches/.menousdb/authdata")
    if not os.path.exists("/Library/Caches/.menousdb/authdata/keys.json"):
        with open("/Library/Caches/.menousdb/authdata/keys.json", "w") as file:
            json.dump([], file)
    if not os.path.exists("/Library/Caches/.menousdb/authdata/login.json"):
        with open("/Library/Caches/.menousdb/authdata/login.json", "w") as file:
            json.dump({}, file)
    path = "/Library/Caches/.menousdb/authdata"


elif sys.platform == "win32":
    if not os.path.exists(os.getenv("APPDATA")+"\\MenoudDb"):
        os.mkdir(os.getenv("APPDATA")+"\\MenoudDb")
    if not os.path.exists(os.getenv("APPDATA")+"\\MenoudDb"+"\\authdata"):
        os.mkdir(os.getenv("APPDATA")+"\\MenoudDb\\authdata")
    path = os.getenv("APPDATA")+"\\MenoudDb"+"\\authdata"


def check_key(key):
    with open(path+'/keys.json') as file:
        data = json.load(file)

    if key in data:
        return True
    else:
        return False

def generate_key():
    with open(path+'/keys.json') as file:
        data = json.load(file)

    key = token_urlsafe(16)

    with open(path+'/keys.json', 'w') as file:
        data.append(key)
        json.dump(data, file, indent=4)

    return key

def signup():
    with open(path + "/login.json", "r") as file:
        data = json.load(file)
    
    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~WELCOME TO MENOUSDB~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        uname = input("ENTER A USERNAME: ")
        pw = getpass.getpass("ENTER PASSWORD: ")
        confirm = getpass.getpass("RE-ENTER PASSWORD: ")
        if pw == confirm:
            data[uname] = [pw, generate_key()]
            with open(path + "/login.json", "w") as file:
                json.dump(data, file, indent=4)
            exit()
        else:
            print("ERROR! PASSWORDS DO NOT MATCH! TRY AGAIN!\n")

def checksignup():
    with open(path + "/login.json", "r") as file:
        data = json.load(file)

    if data == {}:
        signup()

checksignup()