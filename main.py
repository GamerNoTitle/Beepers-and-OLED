from machine import Pin, PWM
import time
import ssd1306
import machine
import sys
import bilibilitv
from machine import I2C, Pin

def draw(pic,offset_x,offset_y):
    for y, row in enumerate(pic):
        for x, col in enumerate(row):
            if col == "1":
                display.pixel(x+offset_x, y+offset_y, 1)
i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.fill(0)

draw(bilibilitv.bilibilitv,0,0)
display.show()

tempo = 5
tones = {
 'c': 262,
 'd': 294,
 'e': 330,
 'f': 350,
 'q':369, 
 'g': 393,
 'a': 441,
 'b': 495,
 'C': 525,
 ' ': 0,
 'D':589,
 'E':661,
 'F':700,
 'G':786,
}
beeper = PWM(Pin(14, Pin.OUT), freq=440, duty=512)
melody = 'CDECaDbgebagcgedefCbCgfefqCbab CDECaDbgebagcgedefgfggegCEDEDCC'
rhythm = [32, 32, 16, 32, 16, 16, 16, 32,16,16,16,16,32,16,8,32,32,8,16,32,32,8,16,32,32,8,16,32,32,8,  32  ,32, 8, 16, 32, 16, 16, 16, 32,16,16,16,16,32,16,8,32,32,8,16,32,32,16,16,16,16,16,32,16,32,8]
for tone, length in zip(melody, rhythm):
 beeper.freq(tones[tone])
 time.sleep(tempo/length)
beeper.deinit()