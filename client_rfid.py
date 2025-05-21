import socket
import time 
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

message = ""

while True:
    try:
        id, text = reader.read()
        #print(id)
        #print(text)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("10.12.240.116", 5000))
        s.sendall(bytes(str(id), "utf-8"))
        message = s.recv(1024).decode("utf-8")    
        print(message)
        s.close()
    except Exception as msg:
        print(msg)
        reset = 0
    finally:
        GPIO.cleanup()
