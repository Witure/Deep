import threading
import time
import queue
import random


#多线程执行多任务
def run():
    print("ssmy is a good man --- %s"%(threading.current_thread().name))
    #实现线程功能
    time.sleep(2)
    print("------sssssssss------")
    time.sleep(2)
    print("ssmy is a nice man --- %s" % (threading.current_thread().name))

if __name__ == "__main__":
    # 任何程序默认就会启动一个线程，称为主线程，主线程可以启动新的子线程

    # current_thread():返回当前线程实例
    print("seagull is a good man --- %s"%(threading.current_thread().name))
    t = threading.Thread(target=run)
    t.start()
    print("seagull is a nice man --- %s" % (threading.current_thread().name))


#所有线程间所有数据共享（也是和多进程最大的区别
num = 100

def run(n):
    global num
    for i in range(1000000):
        num = num + n
        num = num - n

if __name__ == "__main__":
    t1 = threading.Thread(target=run, args=(6,))
    t2 = threading.Thread(target=run, args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(num)

#线程锁的使用,解决数据混乱
num = 100
# 锁对象
lock = threading.Lock()
def run(n):
    global num
    for i in range(1000000):
        # 锁
        # 确保了这段代码只能由一个线程从头到尾执行
        # 阻止了多线程的并发执行，包含了锁的代码段实际上只能由单线程执行
        #由于可以存在多个锁，不同线程之间有不同的锁，并试图获取其他的锁，可能造成死锁，导致多个线程挂起。只能靠操作系统强制终止
        lock.acquire()
        try:
            num = num + n
            num = num - n
        finally:
            #修改完一定要释放锁，不然会造成死锁
            lock.release()
if __name__ == "__main__":
    t1 = threading.Thread(target=run, args=(6,))
    t2 = threading.Thread(target=run, args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(num)

#降低死锁几率（with）
num = 100
lock = threading.Lock()
def run(n):
    global num
    for i in range(1000000):
        # lock.acquire()
        # try:
        #     num = num + n
        #     num = num - n
        # finally:
        #     #修改完一定要释放锁，不然会造成死锁
        #     lock.release()
        with lock:
            num = num + n
            num = num - n

if __name__ == "__main__":
    t1 = threading.Thread(target=run, args=(6,))
    t2 = threading.Thread(target=run, args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(num)

#threadlocal
num = 100
#创建一个全局的threadLocal对象
#每个线程有独立的存储空间
#每个线程对threadlocal对象都可以读写，但是互不影响
local = threading.local()

def run(x, n):
    x = x + n
    x = x - n

def fun(n):
    local.x = num
    for i in range(1000000):
        run(local.x, n)
    print(threading.current_thread().name,local.x)

if __name__ == "__main__":
    t1 = threading.Thread(target=fun, args=(6,))
    t2 = threading.Thread(target=fun, args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(num)


# 信号量控制线程数量
sem = threading.Semaphore(3)
def run():
    with sem:
        for i in range(10):
            print(threading.current_thread().name,i)
            time.sleep(1)

if __name__ == "__main__":
    for i in range(5):
        threading.Thread(target=run).start()

#凑够一定数量才能一起执行
bar = threading.Barrier(3)
def run():

        print(threading.current_thread().name,"seagull")
        time.sleep(2)
        bar.wait()
        print(threading.current_thread().name, "ssmy")

if __name__ == "__main__":
    for i in range(5):
        threading.Thread(target=run).start()


#定时线程
def run():
    print("seagull is a good man")

#延时执行线程
t = threading.Timer(5,run)
t.start()
t.join()
print("父进程结束")

#线程通信
def func():
    #事件对象
    event = threading.Event()
    def run():
        for i in range(5):
            #阻塞，等待事件的触发
            event.wait()
            #重置
            event.clear()
            print("seagull is a good man %d"%(i))
    t = threading.Thread(target=run).start()
    return event

e = func()
for i in range(5):
    time.sleep(2)
    #可以让该次阻塞无效
    e.set()

#生产者与消费者
def product(id,q):
    while True:
        num = random.randint(0,1000)
        q.put(num)
        print("-----------%s-------------%s"%(id,num))
        time.sleep(3)
    q.task_done()

def customer(id,q):
    while True:
        item = q.get()
        if item is None:
            break
        print("===========%s====%s"%(id,item))
        time.sleep(2)


if __name__ == "__main__":
    #消息队列
    q = queue.Queue()

    #启动生产者
    for i in range(4):
        threading.Thread(target=product, args=(i,q)).start()
    #启动消费者
    for i in range(3):
        threading.Thread(target=customer, args=(i,q)).start()


#线程调度（非常难）！
cond = threading.Condition()
def run1():
    with cond:
        for i in range(0, 10, 2):
            print(threading.current_thread().name,i)
            time.sleep(1)
            cond.wait()
            cond.notify()
def run2():
    with cond:
        for i in range(1, 10, 2):
            print(threading.current_thread().name,i)
            time.sleep(1)
            cond.notify()
            cond.wait()

threading.Thread(target=run1).start()
threading.Thread(target=run2).start()

