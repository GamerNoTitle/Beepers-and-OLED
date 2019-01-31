'''
Beeper demo more complex
Hardware connection: Please make sure the wire is connected as follows:
 Beeper esp8266
 + <--> D5
 Hx <--> G
'''
from machine import Pin, PWM
import time
tempo = 5
tones = {
     'c': 262,
     'd': 294,
     'e': 330,
     'f': 349,
     'g': 392,
     'a': 440,
     'b': 494,
     'C': 523,
     ' ': 0,
     '!':131,
     '@':147,
     '#':165,
     '$':175,
     '*':196,
     '^':221,
     '&':248,
     'D':589,
     'E':661,
     'F':700,
     'G':786,
     'H':882,
     'I':990,
}
beeper = PWM(Pin(14, Pin.OUT), freq=440, duty=512)
melody = 'ccceaaageeee&&&*'
rhythm = [8, 8, 8, 8, 8, 8, 8, 8,8,8,8,8,8,8,8,8,]
for tone, length in zip(melody, rhythm):
 beeper.freq(tones[tone])
 time.sleep(tempo/length)
beeper.deinit()