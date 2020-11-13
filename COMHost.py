#!/usr/bin/env python3

import serial
import time
import struct
from bin import Digi18Com_pb2


while True:

    print("Sending STATUS request...")
    ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)
    # request status data
    response = Digi18Com_pb2.Response()
    response.action_id = Digi18Com_pb2.SAMPLER_STATUS
    body = response.SerializeToString()

    header = [b'\x1b', b'\x02', 3, 4, 5]

    print("Sending=", header)
    ser.write(header)

    # read response
    print("Reading response...")
    print("HEADER=", ser.read(10))
    print("PROTOCOL=", ser.read())

    # read telegram length
    s = ser.read(2)
    # read XOR byte for the header
    print("LENGTH=", s)
    length = struct.unpack('>H', s)[0]
    print(length)
    # read xor for header
    print(ser.read())

    # read the rest of telegram
    s = ser.read(length)
    print("BODY=", s)
    ser.close()
    time.sleep(1)
    # response.ParseFromString(s)
    # print(response)