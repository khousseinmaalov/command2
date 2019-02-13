#-*-coding:LATIN-1-*

import serial
import threading
import sys
import time
import RPi.GPIO as GPIO
import socket
from sys import exit

acces = False


def attente():
        global acces
        global debianeuf

        debianeuf = client.recv(2)

        acces = False
        time.sleep(0.1)
        if len(debianeuf) < 1:
                socket.close
                client.close
                exit()
        acces = True


def rotation():
        global acces
        global debianeuf
    
        while 1:

                attente()
                threading.Thread(target=choix).start()


def choix():
                                 
        global acces
        global debianeuf

        if debianeuf[0] == "1":
                craterope = -1
        else:
                craterope = 1
        threading.Thread(target=serv, args=(6, 13, 19, 26, craterope)).start()


        if debianeuf[1] == "1":
                craterope = -1
        else:
                craterope = 1
        threading.Thread(target=serv, args=(17, 22, 23, 24, craterope)).start()        

            
def serv(a, b, c, d, pas):

        global acces
        global debianeuf

        GPIO.setmode(GPIO.BCM)
 
        StepPins = [a,b,c,d]

        for pin in StepPins:
                GPIO.setup(pin,GPIO.OUT)

        Seq = [[1,0,0,1],
               [1,0,0,0],
               [1,1,0,0],
               [0,1,0,0],
               [0,1,1,0],
               [0,0,1,0],
               [0,0,1,1],
               [0,0,0,1]]
                
        StepCount = 8
        
        a = 0
        
        StepCounter = 1
        
        while acces == True:
            
                a = a+1
                
                StepCounter += pas
                
                if (StepCounter>=8):
                        StepCounter = 0
                if (StepCounter<0):
                        StepCounter = 8+pas


                for pin in range(0, 4):
                        xpin = StepPins[pin]
                
                        if Seq[StepCounter][pin]!=0:

                                GPIO.output(xpin, True)
                        else:

                                GPIO.output(xpin, False)
                                     
                time.sleep(0.001)
                

socket = socket.socket()
socket.bind(('', 15561))
socket.listen(1)
client, address = socket.accept()


rotation()
