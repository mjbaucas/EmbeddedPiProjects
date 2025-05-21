import socket
import time
import sys
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
import time

import adafruit_pcd8544

BORDER = 5
FONTSIZE = 10

spi = busio.SPI(board.SCK, MOSI=board.MOSI)
dc = digitalio.DigitalInOut(board.D6)
cs = digitalio.DigitalInOut(board.CE0)
reset = digitalio.DigitalInOut(board.D5)

display = adafruit_pcd8544.PCD8544(spi, dc, cs, reset)

display.bias = 4
display.contrast= 60

backlight = digitalio.DigitalInOut(board.D13)
backlight.switch_to_output()
backlight.value = True

display.fill(0)
display.show()

image = Image.new("1", (display.width, display.height))

draw = ImageDraw.Draw(image)

def write_to_screen(text):
    # Clear screen
    display.fill(0)
	display.show()

    draw.rectangle((0, 0, display.width, display.height), outline=255, fill=255)

	draw.rectangle(
		(BORDER, BORDER, display.width - BORDER - 1, display.height - BORDER - 1),
		outline = 0,
		fill = 0,
	)
	
	(_, _, font_width, font_height) = font.getbbox(text)
	draw.text(
		(display.width // 2 - font_width // 2, display.height // 2 - font_height // 2),
		text,
		font = font,
		fill = 255,
	)

	display.image(image)
	display.show()


ip_addresses = [
    "10.12.210.205",
]

counter = 0
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 5000))
    s.listen(10)
    print('Server is now running.')
    connection, address = s.accept()
    print(address)
    if address[0] == ip_addresses[counter]:
        print(f"Connection from {address} has been established.")
        message = connection.recv(1024)
        write_to_screen(message.decod("utf-8"))
        connection.sendall(bytes("Message recieved", "utf-8"))
        counter+=1
        if counter >= len(ip_addresses):
            counter = 0
    else:
        connection.recv(1024)
        connection.sendall(bytes("", "utf-8"))
        
    print(counter)
    connection.close()