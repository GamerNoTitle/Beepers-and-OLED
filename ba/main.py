import fiveam
import bilibili
import time
from machine import Pin, PWM
import ssd1306
import machine
import sys
from machine import I2C, Pin
# draw a picture function
def draw(pic,offset_x,offset_y):
     for y, row in enumerate(pic):
          for x, col in enumerate(row):
               if col == "1":
                    display.pixel(x+offset_x, y+offset_y, 1)
i2c = I2C(sda=Pin(4), scl=Pin(5))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.fill(0)

draw(bilibili.bilibili,0,0)
display.show()
time.sleep(1.5)

display.fill(0)
draw(fiveam.fiveam,0,0)
display.show()
