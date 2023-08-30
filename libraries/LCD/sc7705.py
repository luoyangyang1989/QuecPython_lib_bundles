import utime

#sc7705_800*1280
init_800X1280 = (
0xB9,0,3,0xF1,0x12,0x84,
0xBA,0,27,0x31,0x81,0x05,0xF9,0x0E,0x0E,0x20,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x44,0x25,0x00,0x91,0x0A,0x00,0x00,0x00,0x4F,0x01,0x00,0x00,0x37,
0xCC,0,1,0x0B,
0xB8,0,1,0xA6,
0xB3,0,8,0x00,0x00,0x00,0x00,0x07,0x0B,0x1E,0x1E,
0xC0,0,9,0x73,0x73,0x50,0x50,0x80,0x00,0x08,0x70,0x00,
0xBF,0,3,0x00,0x10,0x82,
0xBC,0,1,0x46,
0xB4,0,1,0x60,
0xB2,0,2,0x40,0x08,
0xE3,0,10,0x03,0x03,0x03,0x03,0x03,0x03,0x03,0x03,0x00,0x00,
0xB1,0,10,0x22,0x65,0x23,0x1E,0x1E,0x33,0x77,0x04,0x9B,0x0C,
0xB5,0,2,0x0A,0x0A,
0xB6,0,2,0x02,0x02,
0xE9,0,63,0x02,0x00,0x04,0x05,0x06,0x02,0xB1,0x12,0x31,0x45,0x3F,0x06,0x12,0xC1,0x3B,0x0C,0x00,0x80,0x09,0x00,0x00,0x00,
0x00,0x80,0x09,0x00,0x00,0x00,0x68,0x84,0xAB,0x82,0x08,0x64,0x82,0x00,0x88,0x88,0x88,0x78,0x85,0xAB,0x83,0x18,0x75,
0x83,0x11,0x88,0x88,0x88,0x00,0x00,0x00,0x01,0x00,0x12,0xC1,0x3B,0x00,0x00,0x00,0x00,0x00,
0xE9,0,63,0x02,0x00,0x04,0x05,0x06,0x02,0xB1,0x12,0x31,0x45,0x3F,0x06,0x12,0xC1,0x3B,0x0C,0x00,0x80,0x09,0x00,0x00,0x00,
0x00,0x80,0x09,0x00,0x00,0x00,0x68,0x84,0xAB,0x82,0x08,0x64,0x82,0x00,0x88,0x88,0x88,0x78,0x85,0xAB,0x83,0x18,0x75,
0x83,0x11,0x88,0x88,0x88,0x00,0x00,0x00,0x01,0x00,0x12,0xC1,0x3B,0x00,0x00,0x00,0x00,0x00,
0xEA,0,63,0x0B,0x1A,0x01,0x01,0x00,0x36,0x00,0x00,0x00,0x00,0x00,0x00,0x78,0x81,0xAB,0x81,0x38,0x13,0x85,0x75,0x88,0x88,
0x88,0x68,0x80,0xAB,0x80,0x28,0x02,0x84,0x64,0x88,0x88,0x88,0x23,0x10,0x00,0x00,0x00,0x50,0x00,0x00,0x00,0x00,0x00,
0x01,0x80,0x00,0x01,0x80,0x00,0x00,0x00,0x00,0x30,0x02,0xB1,0x00,0x00,0x00,0x00,0x01,0x09,
0xEA,0,63,0x0B,0x1A,0x01,0x01,0x00,0x36,0x00,0x00,0x00,0x00,0x00,0x00,0x78,0x81,0xAB,0x81,0x38,0x13,0x85,0x75,0x88,0x88,
0x88,0x68,0x80,0xAB,0x80,0x28,0x02,0x84,0x64,0x88,0x88,0x88,0x23,0x10,0x00,0x00,0x00,0x50,0x00,0x00,0x00,0x00,0x00,
0x01,0x80,0x00,0x01,0x80,0x00,0x00,0x00,0x00,0x30,0x02,0xB1,0x00,0x00,0x00,0x00,0x01,0x09,
0xE0,0,34,0x00,0x0B,0x0D,0x3A,0x3F,0x3F,0x3F,0x33,0x09,0x0D,0x0D,0x11,0x13,0x12,0x13,0x0B,0x11,
0x00,0x0B,0x0D,0x3A,0x3F,0x3F,0x3F,0x33,0x09,0x0D,0x0D,0x11,0x13,0x12,0x13,0x0B,0x11,
0x11,150,0,
# 0x21,50,0,
0x29,50,0,
)
#sc7705_800*1280
init_800X1280_2 = (
0xB9,0,3,0xF1,0x12,0x84,
0xBA,0,27,0x31,0x81,0x05,0xF9,0x0E,0x0E,0x20,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x44,0x25,0x00,0x91,0x0A,0x00,0x00,0x00,0x4F,0x01,0x00,0x00,0x37,
0xCC,0,1,0x0B,
0xB8,0,1,0xA8,
0xB3,0,8,0x00,0x00,0x00,0x00,0x07,0x0B,0x1E,0x1E,
0xC0,0,9,0x73,0x73,0x50,0x50,0x80,0x00,0x08,0x70,0x00,
0xBF,0,3,0x02,0x10,0x82,
0xBC,0,1,0x46,
0xB4,0,1,0x80,
0xB2,0,2,0x40,0x08,
0xE3,0,10,0x03,0x03,0x00,0x00,0x03,0x03,0x00,0x00,0x00,0xC0,
0xB1,0,10,0x43,0x54,0x23,0x1E,0x1E,0x22,0x77,0x04,0xDB,0x4C,
0xB5,0,2,0x0A,0x0A,
0xB6,0,2,0x44,0x44,
0xE9,0,63,0x02,0x00,0x04,0x05,0x06,0x02,0xB1,0x12,0x31,0x45,0x3F,0x06,0x12,0xC1,0x3B,0x0C,0x00,0x80,0x09,0x00,0x00,0x00,
0x00,0x80,0x09,0x00,0x00,0x00,0x68,0x84,0xAB,0x82,0x08,0x64,0x82,0x00,0x88,0x88,0x88,0x78,0x85,0xAB,0x83,0x18,0x75,
0x83,0x11,0x88,0x88,0x88,0x00,0x00,0x00,0x01,0x00,0x12,0xC1,0x3B,0x00,0x00,0x00,0x00,0x00,
0xEA,0,63,0x96,0x12,0x00,0x00,0x00,0x70,0x00,0x00,0x00,0x00,0x00,0x00,0x78,0x81,0xAB,0x81,0x38,0x13,0x85,0x75,0x88,0x88,
0x88,0x68,0x80,0xAB,0x80,0x28,0x02,0x84,0x64,0x88,0x88,0x88,0x23,0x10,0x00,0x00,0x00,0x50,0x00,0x00,0x00,0x00,0x00,
0x01,0x80,0x00,0x01,0x80,0x00,0x00,0x00,0x00,0x30,0x02,0xB1,0x00,0x00,0x00,0x00,0x01,0x09,
0xE0,0,34,0x00,0x0B,0x0D,0x3A,0x3F,0x3F,0x3F,0x33,0x09,0x0D,0x0D,0x11,0x13,0x12,0x13,0x0B,0x11,
0x00,0x0B,0x0D,0x3A,0x3F,0x3F,0x3F,0x33,0x09,0x0D,0x0D,0x11,0x13,0x12,0x13,0x0B,0x11,
0x11,150,0,
# 0x21,50,0,
0x29,50,0,
)
# 常用颜色定义
red = 0xF800            # 红色
green = 0x07E0          # 绿色
blue = 0x001F           # 蓝色
white = 0xFFFF          # 白色
black = 0x0000          # 黑色
purple = 0xF81F         # 紫色
yellow = 0xffe0         # 黄色
orange = 0xfa20         # 橙色
cyan = 0x867d           # 青色

from machine import LCD
from machine import Pin


def fill(lcd, x_s, y_s, x_e, y_e, color):
    tmp = color.to_bytes(2, 'little')
    count = (x_e - x_s + 1) * (y_e - y_s + 1)

    color_buf = tmp * count

    lcd.lcd_write(color_buf, x_s, y_s, x_e, y_e)


gpio1 = Pin(Pin.GPIO27, Pin.OUT, Pin.PULL_PU, 1)
gpio2 = Pin(Pin.GPIO8, Pin.OUT, Pin.PULL_PU, 1)
gpio3 = Pin(Pin.GPIO11, Pin.OUT, Pin.PULL_PU, 1)

mipilcd = LCD()
mipilcd.mipi_init(initbuf=bytearray(init_800X1280), width=800, hight=1280, DataLane=2, VBP=140, VFP=156, HSync=120, VSync=113, HBP=140, HFP=140)
# mipilcd.mipi_init(initbuf=bytearray(init_800X1280), width=800, hight=1280)

mipilcd.lcd_clear(red)
# fill(mipilcd,0,0,800,160,white)
# fill(mipilcd,0,160,800,320,red)
# fill(mipilcd,0,320,800,480,orange)
# fill(mipilcd,0,480,800,640,yellow)
# fill(mipilcd,0,640,800,800,green)
# fill(mipilcd,0,800,800,960,cyan)
# fill(mipilcd,0,960,800,1120,blue)
# fill(mipilcd,0,1120,800,1280,purple)

