from multiprocessing import Process,Pool,Queue
import time
import os
import random


#开启一个子进程
def run(str):
    while True:
        print("seagull is a %s man --- %s --- %s"%(str,os.getpid(),os.getppid()))
        time.sleep(1.2)
if __name__ == "__main__":
    print("father processing --- %s"%(os.getpid()))
    p = Process(target=run, args=("good",))
    p.start()
    while True:
        print("seagull is a nice man--- %s"%(os.getpid()))
        time.sleep(1)


#等待子进程
def aa():
    print("seagull is a good man")
    time.sleep(3)
    print("seagull is a nice man")

if __name__ == "__main__":
    print("ssmy is a good man")
    p = Process(target=aa,)
    p.start()
    p.join()
    print("ssmy is a nice man")


#不同进程之间全局变量不共享
num = 100
def sun():
    print("start")
    global num
    num += 1
    # time.sleep(1)
    print("end")
    print(num)
    print(id(num))

if __name__ == "__main__":
    print("父进程开始")
    p = Process(target=sun)
    p.start()
    p.join()
    #在子进程中修改全局变量对父进程没有影响,多个进程中依然如此
    #可以近似理解为个毫无关系的代码
    print(id(num))
    print("父进程结束 --- %s"%(num))



#启动大量子进程(多进程)
def son(i):
    print("%s号子进程启动%s"%(os.getpid(),i))
    time.sleep(random.randint(1,3))
    print("%s号子进程结束%s" %(os.getpid(),i))
def run1():
    pass
def run2():
    pass
def run3():
    pass
if __name__ == "__main__":
    print("fall in love with seagull")
    pp = Pool(4) #进程池
    for i in range(5):
        pp.apply_async(son,args=(i,))

    pp.apply_async(run1)
    pp.apply_async(run2)
    pp.apply_async(run3)
    #调用join之前必须调用close，调用close之后不能再添加新的进程
    pp.close()
    pp.join()
    print("fall in love with ssmy")


#拷贝文件 普通方法
def copy(p1, p2):
    f1 = open(p1,"rb")
    f2 = open(p2,"wb")
    text = f1.read()
    f2.write(text)
    f1.close()
    f2.close()


if __name__ == "__main__":
    a = time.time()
    path1 = r"C:\Users\Administrator.PC-20171021MQVA\Desktop\file"
    path2 = r"C:\Users\Administrator.PC-20171021MQVA\Desktop\tofile"
    s = os.listdir(path1)
    # print(s)
    for i in s:
        ss = os.path.join(path1,i)
        dd = os.path.join(path2,i)
        copy(ss,dd)
    b = time.time()
    print(b - a)


#拷贝文件 多进程方法
def copy(p1, p2):
    f1 = open(p1,"rb")
    f2 = open(p2,"wb")
    text = f1.read()
    f2.write(text)
    f1.close()
    f2.close()

if __name__ == "__main__":
    a = time.time()
    path1 = r"C:\Users\Administrator.PC-20171021MQVA\Desktop\file"
    path2 = r"C:\Users\Administrator.PC-20171021MQVA\Desktop\tofile"
    s = os.listdir(path1)
    p = Pool()
    # print(s)
    for i in s:
        ss = os.path.join(path1,i)
        dd = os.path.join(path2,i)
        p.apply_async(copy,args=(ss,dd))
    p.close()
    p.join()
    b = time.time()
    print(b - a)

#二次封装
class seagullProcess(Process):
    def __init__(self,name):
        super.__init__(self)
        self.name = name


#进程间通讯
def write(q):
    print("启动写子进程----%s"%(os.getpid()))
    for char in ["A","B","C","D","E"]:
        # 写进队列
        q.put(char)
        time.sleep(1)
    print("结束写子进程----%s" % (os.getpid()))


def read(q):
    print("启动读子进程----%s"%(os.getpid()))
    while True:
        # 从队列中拿出来
        value = q.get(True)
        print("value = " + value)
    print("结束读子进程----%s" % (os.getpid()))


if __name__ == "__main__":
    # 创建一个队列
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()

    pw.join()
    pr.terminate()

    print("父进程结束")



