#!/usr/bin/env python3
import time
from smbus2 import SMBus

I2C_BUS = 1
ADDR    = 0x69      # your detected BMI160 address
CHIP_ID = 0x00
ACC_LSB = 0x12
GYRO_LSB= 0x0C

def read_i16(bus, reg):
    lo, hi = bus.read_i2c_block_data(ADDR, reg, 2)
    val = (hi << 8) | lo
    return val-65536 if val>32767 else val

with SMBus(I2C_BUS) as bus:
    cid = bus.read_byte_data(ADDR, CHIP_ID)
    print(f"Chip ID: 0x{cid:02X} (==0xD1?)")
    if cid != 0xD1:
        raise RuntimeError("BMI160 not found!")
    print("Reading accel & gyro. Move the board to see values change.")

    while True:
        ax = read_i16(bus, ACC_LSB)
        ay = read_i16(bus, ACC_LSB+2)
        az = read_i16(bus, ACC_LSB+4)
        gx = read_i16(bus, GYRO_LSB)
        gy = read_i16(bus, GYRO_LSB+2)
        gz = read_i16(bus, GYRO_LSB+4)
        print(f"Acc: X={ax:6d}, Y={ay:6d}, Z={az:6d}  |  "
              f"Gyro: X={gx:6d}, Y={gy:6d}, Z={gz:6d}")
        time.sleep(0.5)
