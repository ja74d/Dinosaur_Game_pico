from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import machine
import utime
import framebuf
import math

WIDTH = 128
HEIGHT = 64

buffer1 = bytearray(b"\x00\x00\x00\x00\x07\x80\x009\x00\x00?\xc0\x00/\x80\x009\xc0\x00\x1d\x00\x00\x18\x00 \xc8\x00\x016\x00\x1e8\x00'\xf8\x00\x07\xe8\x00\x1f\x80\x00\x02`\x00\x00 \x00\x01 \x00\x02 \x00\x030\x00\x00\x00\x00")
buffer2 = bytearray(b'\x00\x00\x00\x00|\x00\x00,\x00\x00|\x00\x06L\x00\x06|\x00\x0e|\x00\x05\xfc\x00\x07\xbc\x00\x03\xfc \x00>`\x00|`\x00| \x00}\xe0\x00}\xc0\x00p\x80\x00^\x00\x00|\x00\x00~\x00\x00\x00\x00')
buffer3 = bytearray(b'\x0c#\x00]\x03\x80\x1e\x03\xa0\xdc#\xa0\xdd\x83\xc0\xdd\xd7\xa0\xdf\xfb\xb0\xdd\xfb\xa0\xdd\xfb\xe0\x7f\xfb\xa0=\xfb\xa0\x1f\xbb\xb0\x1f\x9f\xd0\x1c\x8f\x80\\\x03\x80\x9c\x13\x80\x1c\x13\x80\x1cC\x80|\x03\x80<\x0b\x80')


fb1 = framebuf.FrameBuffer(buffer1, 20, 20, framebuf.MONO_HLSB)
fb2 = framebuf.FrameBuffer(buffer2, 20, 20, framebuf.MONO_HLSB)
fb3 = framebuf.FrameBuffer(buffer3, 20, 20, framebuf.MONO_HLSB)

potentiameter = machine.ADC(26)
conv = 3.3/(65535)



i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

oled = SSD1306_I2C(128, 64, i2c)

oled.fill(0)

#oled.blit(fb1, 0, 15)
#oled.blit(fb2, 0, 15)
oled.text("Lets GO", 37, 32)

oled.show()
utime.sleep(1)

i = 0

j = 110

k = 220

z = 330

while True:
    oled.fill(0)
    
    voltage = potentiameter.read_u16()*conv
    #print(voltage)
    
    sic = voltage*10 + 12

    i = int(i) + 1
    
    j = int(j) - 1
    
    k = int(k) - 1
    
    z = int(z) - 1
    
    #oled.text(str(i), 0, 0)
    
    oled.blit(fb1,32, int(sic))
    
    oled.blit(fb2,int(j), 45)
    
    oled.blit(fb2,int(k), 45)
    
    oled.blit(fb3,int(z), 45)
    
    
    #top
    #oled.text(str(voltage), 0, 0)
    oled.text("Dinosaur Game",8,4)
    #oled.text(str(sic), 0, 0)
    
    oled.hline(0,0,128,1)
    oled.hline(0,1,128,1)
    oled.hline(0,2,128,1)
    
    oled.hline(0,13,128,1)
    oled.hline(0,14,128,1)
    oled.hline(0,15,128,1)
    
    oled.vline(0,0,14,1)
    oled.vline(1,0,14,1)
    
    oled.vline(127,0,14,1)
    oled.vline(126,0,14,1)
    
    #cactos
    
    
    #floor
    oled.hline(0,63,127,1)
    
    if int(math.ceil(sic)) == 45 and int(j) == 46:
        oled.fill(0)
        oled.text("Game Over", 28, 32)
        oled.text("press F5", 30, 45)
        oled.show()
        break
    
    if int(math.ceil(sic)) == 45 and int(k) == 46:
        oled.fill(0)
        oled.text("Game Over", 28, 32)
        oled.text("press F5", 30, 45)
        oled.show()
        break
    
    if int(math.ceil(sic)) == 45 and int(z) == 46:
        oled.fill(0)
        oled.text("Game Over", 28, 32)
        oled.text("press F5", 30, 45)
        oled.show()
        break
    
    
    oled.show()
    utime.sleep(0.02)


