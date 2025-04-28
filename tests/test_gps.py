#!/usr/bin/env python3
import serial
import time
import pynmea2

PORT = "/dev/ttyS0"   # or "/dev/serial0" if available
BAUD = 9600

print(f"Opening {PORT} @ {BAUD} baud…")
with serial.Serial(PORT, BAUD, timeout=1) as ser:
    print("Waiting for NMEA sentences. Move outdoors or near a window.")
    while True:
        line = ser.readline().decode("ascii", errors="ignore").strip()
        if line.startswith(("$GPRMC", "$GPGGA")):
            try:
                msg = pynmea2.parse(line)
                print(f"{msg.sentence_type}: Lat={msg.latitude} {msg.lat_dir}, "
                      f"Lon={msg.longitude} {msg.lon_dir}, "
                      f"Speed={getattr(msg, 'spd_over_grnd', 'N/A')}")
            except pynmea2.ParseError:
                pass
        time.sleep(0.1)
