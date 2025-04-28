#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
from luma.core.interface.serial import spi
from luma.lcd.device import st7789

# --- Adjust these if your wiring differs ---
GPIO_DC  = 25   # Data/Command
GPIO_RST = 24   # Reset
GPIO_BL  = 18   # Backlight PWM (via MOSFET)
SPI_PORT = 0
SPI_DEV  = 0

# Initialize SPI display
serial = spi(port=SPI_PORT, device=SPI_DEV,
             gpio_DC=GPIO_DC, gpio_RST=GPIO_RST, gpio_BL=GPIO_BL)
device = st7789(serial, width=320, height=480, rotate=0)

# Draw test image
img = Image.new("RGB", (device.width, device.height), "black")
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()

draw.rectangle((0, 0, device.width-1, device.height-1), outline="white")
draw.line((0, 0, device.width-1, device.height-1), fill="white")
draw.text((10, 10), "Display Test OK", font=font, fill="white")

device.display(img)
print(">> Display should show a test pattern. Close by Ctrl+C.")
