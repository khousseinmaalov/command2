from tkinter import *
import threading
import socket
import time

hote = "127.0.0.1"
port = 15561


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.connect((hote, port))


print("Connection sur {}".format(port))


def debianeuf(event):

	olivier_de_carglasse = event.keysym
	if olivier_de_carglasse == "Down":
		socket.send("11".encode())
		print(olivier_de_carglasse)

	if olivier_de_carglasse == "Up":
		socket.send("12".encode())
		print(olivier_de_carglasse)
	if olivier_de_carglasse == "Right":
		socket.send("21".encode())
		print(olivier_de_carglasse)
	if olivier_de_carglasse == "Left":
		socket.send("22".encode())
		print(olivier_de_carglasse)



def rien():

	fenetre = Tk()
	frame = Frame(fenetre, width=100, height=100)
	canvas = Canvas(fenetre, width=500, height=500)
	canvas.focus_set()
	threading.Thread(target=canvas.bind,args=("<Key>", debianeuf)).start()
	canvas.pack()

	frame.pack()

	fenetre.mainloop()
rien()

socket.close
