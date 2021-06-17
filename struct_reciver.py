# -*- coding: utf-8 -*-

import socket
import time
import struct
from ctypes import *


#timeCheck = time.time()
#time.sleep(0.5)
#fps = 0



class My_struct_test(BigEndianStructure):  #明文传输结构
    #大端的数据结
    _pack_=1

    _fields_ = [('uSpeedLevel',c_ubyte,2),#传送速度等级
        ('u_over_buffer_lock',c_ubyte,1),#越过缓冲 加锁 位
        ('u_peddle_unlock',c_ubyte,1), #脚踏解锁位
        ('u_switch_kalmann_filter',c_ubyte,1), #本地卡尔曼滤波 标志位
        ('u_switch_reserve1',c_ushort,1),


        ('ulong_counter',c_ulong),#60hz 刷新率，最长连接时间2.1年。120hz 刷新，最长1年。
        #('ulong_ping',c_uint,10),# 返回包 与同时发送包差值 ，延迟
        ('angle_index',c_ubyte,4),#角度调节组 共16组  共16*3 = 48 关节
        ('angle_1',c_ulong,10),#10bit 1024级区分  12bit 4096区分 /0.08度 14bit 16384区分 0.022度 1.31 arcmin
        ('angle_2',c_ulong,10),
        ('angle_3',c_ulong,10),
        ('angle_1_force_limit',c_ulong,6),# 6bit 64级区分 力量（电流）限制，到达则改变 平衡点
        ('angle_2_force_limit',c_ulong,6),
        ('angle_3_force_limit',c_ulong,6),

        #受力条件下位移极限，6bit 64级区分
        ('angle_1_distance_limit',c_ulong,6),# 6bit 64级区分 力量（电流）限制，到达则改变 平衡点
        ('angle_2_distance_limit',c_ulong,6),
        ('angle_3_distance_limit',c_ulong,6),




        #('uSpeed',c_ushort,15),
        #('uReserve',c_ubyte,1),
        #('ulong_calculate',c_ulong),# 60hz 刷新率，最长连接时间2.1年。120hz 刷新，最长1年。
        #('ulong_calculate2',c_longlong),
        #('ulong_calculate3',c_longlong),
        ('crc32_value',c_uint32,32),
        ]

class Data(BigEndianStructure):#测试结构            udp effects  at  30K pps 
    _pack_ = 1
    _fields_ = [("member_1", c_ubyte,4),
                ("member_2", c_long),
                ("member_3", c_float),
                ("member_4", c_longlong),
                ("member_5", c_long)]
'''
#data = Data()
##PORT = 8000
#receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#address = ("127.0.0.1", PORT)
#receiver_socket.bind(address)
'''
'''
while True:
        
        #print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(now)))
        message, client = receiver_socket.recvfrom(1024)
        memmove(addressof(data), (message), sizeof(Data))
        #fps = int(1/(time.time() - timeCheck))
        
        print('member_1: %d' % data.member_1, 'member_2: %0.6d' % data.member_2, 'member_3: %.2f' % data.member_3, \
              'member_4: %d' % data.member_4, 'member_5: %d' % data.member_5 ,end = '   \r')  #'fps: %0.5d'  %fps  ,
        #print(f'fps = {fps}', end= '  \r')
        #timeCheck = time.time()
        
'''
#initial socket 
# #data
data = Data()
PORT = 8000
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ("127.0.0.1", PORT)
receiver_socket.bind(address)



import threading , time, signal
class GetResultThread (threading.Thread):
    def __init__(self, _threadName, _data_isntance ,_data_CLASS, _receiver_socket, _threadLock = None):

        #_data_CLASS 可省略？
        threading.Thread.__init__(self)


        self.name = _threadName
        self.data_isntance = _data_isntance
        self.data_CLASS = _data_CLASS
        self.threadLock = _threadLock
        self.receiver_socket = _receiver_socket
        #self.lock = lock
        self.daemon = True
        
    def run(self):
        #start 自动运行
        #print ("开始线程：" + self.name)
        # 获取锁，用于线程同步
        #self.lock.acquire()
        #self.speak()
        # 释放锁，开启下一个线程
        #self.lock.release()
        #print ("结束线程：" + self.name)
        #while 1 :
        self.begin_recieve()

    def begin_recieve(self):

        while 1:
            
            #print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(now)))
            message, client = self.receiver_socket.recvfrom(1024)
            #print(message)
            #print(client)
            #if self.threadLock != None:
                    
                    
                    #_data_CLASS 可省略？                              self.data_isntance
            memmove(addressof(self.data_isntance), (message), sizeof(self.data_CLASS))
            #fps = int(1/(time.time() - timeCheck))
            
            print('member_1: %d' % data.member_1, 'member_2: %0.6d' % data.member_2, 'member_3: %.2f' % data.member_3, \
                'member_4: %d' % data.member_4, 'member_5: %d' % data.member_5 ,end = '   \r')  #'fps: %0.5d'  %fps  ,
            #print(f'fps = {fps}', end= '  \r')
            #timeCheck = time.time()

    '''
    def speak(self):
        #
        #播报线程 threadName, 播放str， 延迟
        #
        time.sleep(1)
        #print()
        print ("'speaking' %s" % ( time.ctime(time.time())))
        mystr = str(self.speak_str)
        engine = pyttsx3.init()
        engine.say(mystr.replace('\n',""))
        engine.runAndWait()
    '''

import sys
def quit(signum, frame):
    print('')
    print('You choose to stop me.')
    sys.exit()


#try:

if __name__ == '__main__':
    signal.signal(signal.SIGINT, quit)
    signal.signal(signal.SIGTERM, quit)


    slot1 = GetResultThread('slot1',data , Data,receiver_socket   )

    slot1.setDaemon(True)
    slot1.start()
    #slot1.join()
    while 1 :
        time.sleep(100)
        pass
#except:
    #print('')
    #exit()
#    pass

#endregion












#if __name__=='__main__':
#    freeze_support()
##    printGreen(f'开启服务器 {IP_str}:{port_int}')
#   printGreen(f'开启服务器 {IP_str2}:{port_int2}')
#    server_mode()

