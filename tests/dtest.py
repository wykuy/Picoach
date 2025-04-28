cat <<'EOF' > ~/test_st7796.py
#!/usr/bin/env python3
import time, digitalio, board
from PIL import Image, ImageDraw
import adafruit_rgb_display.st7796 as st7796

# SPI bus & control pins
spi = board.SPI()                          # SCLK=GPIO11, MOSI=GPIO10
cs  = digitalio.DigitalInOut(board.CE0)    # GPIO8
dc  = digitalio.DigitalInOut(board.D23)    # your DC pin (BCM 23)
rst = digitalio.DigitalInOut(board.D24)    # your RST pin (BCM 24)
bl  = digitalio.DigitalInOut(board.D18)    # your BL pin (BCM 18)

# Backlight on
bl.direction = digitalio.Direction.OUTPUT
bl.value     = True

# Initialize the ST7796 driver
display = st7796.ST7796(
    spi, cs=cs, dc=dc, rst=rst,
    width=320, height=480,
    baudrate=24000000
)

# Draw a red square and green circle
img   = Image.new("RGB", (display.width, display.height), "black")
draw  = ImageDraw.Draw(img)
draw.rectangle((10, 10, 100, 100), fill="red")
draw.ellipse((150, 10, 300, 160), fill="green")
display.image(img)
display.show()

# Keep it on for 10s
time.sleep(10)
EOF

chmod +x ~/test_st7796.py
