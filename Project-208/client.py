import socket
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import random
from PIL import ImageTk, Image

SERVER = None
PORT = 8050
IP_ADDRESS = "127.0.0.1"
BUFFER_SIZE=4096

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))
    musicScreen()

def musicScreen():
    windowm=Tk()
    windowm.title("Music Window")
    windowm.geometry("300x300")
    windowm.configure(bg="LightSkyBlue")

    sLabel=Label(windowm,text="Select a song!",bg='LightSkyBlue',font=("Calibri",8))
    sLabel.place(x=2,y=1)

    listbox=Listbox(windowm,heigh=10,width=39,activestyle="dotbox",borderwidth=2,font=("Calibri",10))

    windowm.mainLoop()

setup()

