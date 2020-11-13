#!/usr/bin/env python3

import time
import datetime
import struct
from bin import Digi18Com_pb2
import serial

def checksum( arr ):
   checksum = 0
   for el in arr:
       checksum ^= el
   return checksum

while True:

    print('%s' % datetime.datetime.now(), "Sending SAMPLER_STATUS request...")

    ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)
    # request status data
    response = Digi18Com_pb2.Response()
    response.action_id = Digi18Com_pb2.SAMPLER_STATUS
    body = response.SerializeToString()

    header = bytearray()
    header += b'\x1b'
    header += struct.pack('>B', Digi18Com_pb2.PROTOCOL_VERSION)
    header += struct.pack('>H', len(body))
    header += struct.pack('>B', checksum(header))
    header += body
    header += struct.pack('>B', checksum(body))

    # send to the COM
    ser.write(header)

    # read response
    print("Reading response...")
    # read header
    ser.read()
    # read version
    print("PROTOCOL=", struct.unpack('>B', ser.read())[0])
    # read telegram length
    length = struct.unpack('>H', ser.read(2))[0]
    # read XOR byte for the header
    ser.read()

    # read the BODY (payload + cs)
    s = ser.read(length)
    # remove checksum
    s[:-1]
    input = Digi18Com_pb2.Response()
    input.ParseFromString(s)
    print(input);

    ser.close()
    time.sleep(1)