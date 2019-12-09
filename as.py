

"""
子程序/函数：在所有语言中都是层级调用，比如A调用B，在B执行的过程中又可以调用C，C执行完毕返回，B执行完毕返回，最后是A执行完毕。是通过栈实现的，一个线程就是执行一个子程序，子程序调用总是一个入口，一次返回，调用的顺序是明确的
协程：看上去也是子程序，但是执行过程中，在子程序内部可中断，然后转而执行别的子程序，不是函数调用，有点类似CPU中断,执行效率极高,因为只有一个线程，不存在同时写变量的冲突，在协程中共享资源不加锁，只需要判断状态

"""
#子程序
def a():
    print("A------start")
    b()
    print("A------end")


def b():
    print("B------start")
    c()
    print("B------end")


def c():
    print("C------start")
    d()
    print("C------end")


def d():
    print("D------start")
    print("D------end")

a()

#协程（功能看起来像是多线程，其实是一个线程）Python对协程的支持是通过generator实现的
def run():
    print(1)
    yield 10
    print(2)
    yield 20
    print(3)
    yield 30

m = run()
print(next(m))
print(next(m))
print(next(m))

#数据传输
def run():
    #空变量，存储的作用data始终为空
    data = ""
    r = yield data
    print(1,r,data)
    r = yield data
    print(2,r,data)
    r = yield data
    print(3,r,data)
    r = yield data

m = run()
#启动m
print(m.send(None))
print(m.send("a"))
print(m.send("b"))

#生产者与消费者
def pro(c):
    c.send(None)
    for i in range(5):
        print("生产者产生数据%s"%i)
        r = c.send(str(i))
        print("seagull is a good man %s"%(r))
    c.close()

def cus():
    data = ""
    while True:
        n = yield data
        if not n:
            return
        print("消费者消费了%s"%(n))
        data = "200"

c = cus()
pro(c)







































