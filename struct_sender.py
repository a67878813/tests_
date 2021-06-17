# -*- coding: utf-8 -*-

import socket
import time
import struct
from ctypes import *

class Data(BigEndianStructure):
    _pack_ = 1
    _fields_ = [("member_1", c_ubyte,4),
                ("member_2", c_long),
                ("member_3", c_float),
                ("member_4", c_longlong),
                ("member_5", c_long)]


'''
    def encode(self):
        return string_at(addressof(self), sizeof(self))

    def decode(self, data):
        memmove(addressof(self), data, sizeof(self))
        return len(data)
'''


data = Data()
data.member_1= 0xF2
data.member_2= 222111222
data.member_3= 125
data.member_4= 150
data.member_5= 0x0101
print(sizeof(data))
PORT = 8000
sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver_address = ("127.0.0.1", PORT)

ee = string_at(addressof(data), sizeof(data))
while 1:
    #start = time.time()
    #print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start)))
    data.member_2 +=1
    stream_bytes = string_at(addressof(data), sizeof(data))
    f = ''.join(['%02X ' % b for b in stream_bytes])  #bytes 转 16进制

    #print(f,end = '  \r')
    sender_socket.sendto(stream_bytes, receiver_address)
    #print('member_1: %d' % data.member_1, 'member_2: %d' % data.member_2, 'member_3: %.2f' % data.member_3, \
    #      'member_4: %.2f' % data.member_4, 'member_5: %d' % data.member_5,end = "\r")
    #time.sleep(0.0005)



