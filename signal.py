import ssd1306
import machine
import sys
import time
from machine import I2C, Pin
# draw a picture function
def draw(pic,offset_x,offset_y):
    for y, row in enumerate(pic):
        for x, col in enumerate(row):
            if col == "1":
               display.pixel(x+offset_x, y+offset_y, 1)
# init display
i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.fill(0)
# image data
testMap = [
'1111111111100000',
'1000010000100000',
'0100010001000000',
'0010010010000000',
'0001010100000001',
'0000111000000101',
'0000010000010101',
'0000010001010101',
'0000010101010101',
'0000010101010101',]
# draw image
draw(testMap,105,16)
display.show()