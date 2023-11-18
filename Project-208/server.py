import socket
from tkinter import *
from  threading import Thread
import random
from PIL import ImageTk, Image

SERVER = None
PORT = 8050
IP_ADDRESS = "127.0.0.1"
BUFFER_SIZE=4096
clients={}

def acceptConnections():
    global SERVER
    global clients
    while True:
        client,addr=SERVER.accept()
        print(clients.addr)


def setup():
    print("\n\t\t\t\t\t\t IPMUSIC APP \n")
    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS,PORT))
    SERVER.listen(100)

    print("\t\t\t\tAWAITING INCOMING CONNECTIONS...")
    print("\n")

    acceptConnections()
    
setup_thread=Thread(target=setup)
