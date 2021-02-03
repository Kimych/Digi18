#!/usr/bin/env python3

import struct
from bin import Digi18Com_pb2
import serial
from inputimeout import inputimeout


def checksum(arr):
    checksum = 0
    for el in arr:
        checksum ^= el
    return checksum


# Wrap protobuf content into telegram
def wrap_content(content):
    header = bytearray()
    # [HEADER]=[0x1b (1 byte)]+[Protocol version (1 byte)]+[BODY size (2 bytes)]+[Checksum(1 byte)]
    header += b'\x1b'
    header += struct.pack('>B', Digi18Com_pb2.PROTOCOL_VERSION)
    checksum_size = 0
    # TODO comment next line to use PROTOCOL VERSION 4
    # checksum_size = 1
    header += struct.pack('>H', len(content) + checksum_size)
    header += struct.pack('>B', checksum(header))
    # [BODY] = [Content]+[Checksum (1 byte)]
    header += content
    header += struct.pack('>B', checksum(content))
    return header


def read_response(serial):
    # read start byte
    serial.read()
    # read version
    serial.read()
    # read telegram length
    length = struct.unpack('>H', serial.read(2))[0]
    # read XOR byte for the header
    serial.read()
    # read the BODY (payload + cs)
    s = serial.read(length)
    # remove checksum
    # TODO comment next line to use PROTOCOL VERSION 4
    # s = s[:-1]
    response = Digi18Com_pb2.Response()
    response.ParseFromString(s)
    return response


def send_program_cmd(serial, cmd):
    # request status data
    request = Digi18Com_pb2.Request()
    request.action_id = Digi18Com_pb2.PROGRAM_CMD
    request.program_cmd.type = cmd
    start = request.SerializeToString()
    # write to the COM
    serial.write(wrap_content(start))


def send_filter_cmd(serial, cmd):
    # request status data
    request = Digi18Com_pb2.Request()
    request.action_id = Digi18Com_pb2.FILTER_CMD
    request.filter_cmd.type = cmd
    start = request.SerializeToString()
    # write to the COM
    serial.write(wrap_content(start))


def send_status_req(serial):
    # request status data
    request = Digi18Com_pb2.Request()
    request.action_id = Digi18Com_pb2.SAMPLER_STATUS
    start = request.SerializeToString()
    # write to the COM
    serial.write(wrap_content(start))


while True:
    print(" s - start program; f - finish program; c - filter change; otherwise - status request")
    # default command is - STATUS request
    user_input = "st"
    try:
        user_input = inputimeout(prompt='>>', timeout=5)
    except:
        print("")

    ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)

    if user_input == "s":
        print("sending START...")
        send_program_cmd(ser, Digi18Com_pb2.ProgramCmd.START)
    elif user_input == "f":
        print("sending FINISH...")
        send_program_cmd(ser, Digi18Com_pb2.ProgramCmd.FINISH)
    elif user_input == "c":
        print("sending FILTER CHANGE...")
        send_filter_cmd(ser, Digi18Com_pb2.FilterCmd.CHANGE)
    else:
        print("sending STATUS request...")
        send_status_req(ser)

    # print response
    print(read_response(ser))
    ser.close()
