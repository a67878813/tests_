import ctypes
import os
import platform
import sys
from termcolor import colored
ALL_LOG_FILE   = "all.log"
ERROR_LOG_FILE = "error.log"

#region log
import logging
import logging.handlers
import datetime
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H-%M-%S"
#logging.basicConfig(filename= 'my.log',level= logging.DEBUG,format= LOG_FORMAT, datefmt=DATE_FORMAT)

# logging.debug("This is a debug log")
# logging.info("This is a info log")
# logging.warning("This is a warning log")
# logging.error("This is a error log")
# logging.critical("This is a critical log")
# logging.warning("Some one delete the log file.", exc_info=True, stack_info=True, extra={'user': 'Tom', 'ip':'47.98.53.222'})

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

rf_handler = logging.handlers.TimedRotatingFileHandler(ALL_LOG_FILE, 
                                                       when = 'midnight',
                                                       interval = 1,
                                                       backupCount=7,
                                                       atTime=datetime.time(0,0,0,0))
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s",datefmt = DATE_FORMAT))

f_handler = logging.FileHandler(ERROR_LOG_FILE)
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s",
                                         datefmt = DATE_FORMAT))

s_handler = logging.StreamHandler()
s_handler.setLevel(logging.INFO)
s_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s",
                                         datefmt = DATE_FORMAT))




logger.addHandler(rf_handler)# for every log
logger.addHandler(f_handler)# for error
logger.addHandler(s_handler)# for display

# examples
# logger.debug("This is a debug log")
# logger.info("This is a info log")
# logger.warning("This is a warning log")
# logger.error("This is a error log")
# logger.critical("This is a critical log")
# logger.warning("Some one delete the log file.", exc_info=True, stack_info=True, extra={'user': 'Tom', 'ip':'47.98.53.222'})

#endregion



print(platform.system())
#"Linux"
print("Main PID: ",os.getpid())
def get_free_space_GiB(folder):
    """ return folder/ drive free space(in GiB) """
    if platform.system() == "Windows":
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder),None,None, ctypes.pointer(free_bytes))
        return free_bytes.value/1024/1024/1024
    else:
        print(" script running at Linux platform...")
        st = os.statvfs(folder)
        return st.f_bavail * st.f_frsize/1024/1024/1024
        #   GiB


t_free_space = get_free_space_GiB(r'/mnt')
if t_free_space < 50 :
    print(colored(("	TOO SMALL free space in \mnt : " + str(round(t_free_space,1))    ),"red"))
    print("exit")
else:
    print(colored(("	          free space in \mnt : " + str(round(t_free_space,1))    ),"green"))


import time
# T1 = time.perf_counter()


# def my_process(x):
#     for i in range(10000000):
#         x +=1
#     return x


# my_process(1)
# T2 = time.perf_counter()
# print('    运行:%s毫秒' % ((T2 - T1)*1000))

# print('-------------------')
from multiprocessing.pool import ThreadPool
import subprocess
from multiprocessing import Lock# as multip_Lock
from multiprocessing import Queue
# from multiprocessing 
from queue import Empty
from queue import Full
def work( _lock,_work_queue, _done_queue):

    logger.info("worker begin")
    
    
    try:
        line =  _work_queue.get(block=True,timeout=3)
    except Empty:
        logger.info("       _work_queue is empty and worker was killed")
        return 0
    try:
        ctime = os.path.getctime(line)
    except :
        return 1
    salt_ = random.randint(1000, 9000)
    print(colored("进行meta注入 = "+str(line),"green"))
    
    
    
    
    try:
    
        _pr1 = subprocess.Popen(["ping","127.0.0.1" , "-c" , "1"],#stderr=subprocess.STDOUT,
                                stdout = subprocess.PIPE,  encoding = 'utf-8')
        # print("         _pr1 pid = ",  _pr1.pid)
        logger.info(f"_pr1 pid = {_pr1.pid}")
        #_pr1.wait()
        #test_result = _pr1.communicate()[0]
        _result_1 ,_result_2 = _pr1.communicate()
        #te2 = _pr1.communicate()[1]
        _lock.acquire()
        #print("===================")
        logger.info(f"len_result_1 = {len(_result_1)}")
        #print(len(_result_1))
        if _result_2 == None:
            logger.info(f"_result_2 is null")
            
        else:
            print('error::::::::::::::::::::::')
            print(_result_2)
            logger.error(f"_result_2 = {_result_2}", exc_info=True, stack_info=True, extra={'user': 'Tom', 'ip':'47.98.53.222'})
        
        logger.info(f"_pr1.returncode = {_pr1.returncode}")
        
        #print(test_result)
        time.sleep(1)
        _mediate = _result_1.split('\n')
        for _ in _mediate:
            print(_)
        # print("     -1 done")
        logger.info(f" -- DONE -- _pr1 pid = {_pr1.pid}")
        #print("==============")
        _lock.release()
        
    except:
        print(colored("meta信息写入错误","red"))
        print(colored(line,"red"))
        return 1
    
    time.sleep(10)
    try:
        _pr2 = subprocess.Popen(["sleep","2"],stderr=subprocess.STDOUT)
        logger.info(f"_pr2 pid = {_pr2.pid}")
        # print("         _pr2 pid = ",  _pr2.pid)
        _pr2.wait()    #等待子进程结束，父进程继续
        #logger.info(f" -- DONE -- _pr2 pid = {_pr2.pid}")
        print("     -2 done")
        time.sleep(5)
        #os.utime(line, (ctime,ctime))
        print("     -change_time")
    except:
        print(colored("mv错误","red"))
        print(colored(line,"red"))
        return 1
    try:
        os.utime(line, (ctime,ctime))
    except:
        return 1
    
    try:
        _done_queue.put(line,block=True,timeout=10)
    except:
        return 1
    
    return 0




import os
import os.path
import json
import random
import pickle

def get_work_list():
    
    contents = "/mnt"
    s =[]
    for root, dirs, files in os.walk(contents):
        for name in files:
            s.append(os.path.join(root, name))
    end_list = []
    try:
        with open(contents+'/done_list.json', 'r') as r:
            done_list = json.load(r)

        
    except FileNotFoundError:
        print("donelist is not exist")
        done_list = []
        with open(contents+'/done_list.json', 'w') as f:
            f.write(json.dumps(done_list))
        
    for line in s:
    #未修复的flv文件，追加到end_list中
        if (".flv" in line) and (line not in done_list):
            end_list.append(line)
    print_list=end_list[:3]
    for i in print_list:
        print(i)
    print(colored(("	未添加meta数据的flv文件数 =  " + str(len(end_list))),"cyan"))

    #判断临时目录是否存在
    if os.path.isdir(contents+"/_temp"):
        pass
    else:
        os.mkdir(contents+"/_temp")
        print("临时目录已建立")
        
    return end_list

if __name__ == "__main__":
    try:
        my_lock = Lock()
        work_queue = Queue()
        done_queue = Queue()
        num = 2
        my_tp = ThreadPool(num)

        file_list  = get_work_list()

        print("Fiel_list's length  = ",len(file_list))
        for i in file_list:
            work_queue.put(i)
        print("work_queue's size =  ",work_queue.qsize())










        for sample in range(4):
            my_tp.apply_async(work,( my_lock,work_queue,done_queue))

        my_tp.close()#关闭进程池（pool），使其不在接受新的任务。
        my_tp.join()#主进程阻塞等待子进程的退出，join方法必须在close或terminate之后使用。
        
    except Exception:
        # print("have some error")
        logger.error("Exception", exc_info=True, stack_info=True, extra={'user': 'Tom', 'ip':'47.98.53.222'})
    except KeyboardInterrupt:
        logger.warning("KeyboardInterrupt")
    finally :
        print("finnal")
        print("finaaaaaaaaaaaaaaaaaaaaaaaa")
        print("done_queue's size =  ",done_queue.qsize())
        done_list = []
        while 1 :
            try:
                i = done_queue.get(block = False)
                done_list.append(i)
            except:
                break
        print("done_list 's length = ", len(done_list))
        print(done_list)
        
        logger.info("FINALLY")
        # write queue changes to file
        
        #process done_queue
        