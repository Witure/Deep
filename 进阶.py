from functools import reduce
import copy

# # 元类
# def ptnum(self):
#     print("--%d--"%self.num)
# Test = type("Test",(),{"ptnum":ptnum})
# a = Test()
# a.num = 100
# a.ptnum()


# class Itcast(object):
#     def __init__(self,s):
#         self.s = s
#         self.d = "seagull"
#     # 属性访问拦截器
#     def __getattribute__(self, item):
#         if item == "s":
#             print("seagull is a good man")
#             return "hhhhhhhh python"
#         else:
#             return object.__getattribute__(self,item)
#
#     def show(self):
#         print("ssmy is a good man")
#
# s = Itcast("python")
# print(s.s)
# print(s.d)
#
# #map  and   functools.reduce
# a = map(lambda x,y:x*y,[1,3,6],[2,8,6])
# print(list(a))
#
# def f1(x,y):
#     return (x,y)
#
# l1 = ["asd","sea","gull"]
# l2 = [1,2,3]
# l3 = map(f1,l1,l2)
# print(list(l3))
# #filter
# q = filter(lambda s:s%2,[1,2,3,4,5,6])
# print(list(q))
# #reduce
# k = reduce(lambda x,y:x+y,[1,2,3,4,5,6])
# print(k)
#
# a1 = reduce(lambda x,y:x+y,["aa","bb","cc"],"dd")
# print(a1)
#
# # 集合
# a = "seagull"
# b = set(a)
# A = "selpxm"
# B = set(A)
# print(b&B,b|B,b-B)
#
#
# # 深浅拷贝
# a = [11,22,33]
# b = a
# print(id(a),id(b))
# c = copy.deepcopy(a)
# print(id(a),id(c))
# d = copy.copy(a)
# print(id(d),id(a))
# a.append(55)
# print(d)
# f = (11,22,33)
# g = copy.copy(f)
# print(id(f),id(g))
#
# # 深浅拷贝进阶
# #每个变量都有标识，类型和值。对象一旦创建，他的标识就不会改变；你可以把标识理解为对象在内存中
# #的地址。is运算符比较两个对象的标识，id()返回对象标识的整数表示
# #举个例子，a = [1,2,3]中，[1,2,3]是一个对象，标识为起在内存的地址，a是一个标签，是其的一个引用
#
#
# #位运算
# a = 3
# b = a << 5
# print(b)
# print(3*(2**5))
#
# #私有（假的私有，全是假的）
# class Test():
#     def __init__(self):
#         self.__num = 100
#
#     def setnum(self,newnum):
#         self.__num = newnum
#
#     def getnum(self):
#         return self.__num
#
# t = Test()
# print(t.__dict__)
# print(t._Test__num)
# # print(t.__num)
# print(t.getnum())
# t.setnum(200)
# print(t.getnum())
# print(t._Test__num)
#
#
# #垃圾回收
# #CPython中的垃圾回收机制，以引用计数为主，分代回收为辅
# a = [1,2,3,4,5]
# print(id(a))
# a.append(6)
# print(id(a))
# a = [1,2,3,4,5,6]
# #这时候原来的对象[1,2,3,4,5,6]不再有引用数而被垃圾回收
# print(id(a))
#
# #闭包（嵌套函数+自由变量）
# #函数名只是个变量名，指向函数体
# def ave():
#     a = []
#     def ll(x):
#         a.append(x)     #a为自由变量
#         p = sum(a)
#         b = p / len(a)
#         print(b)
#     return ll
#
# q = ave()
# q(1)
# q(6)
# q(5)
#
# #闭包2,
# def test(n):
#     def t(s):
#         return n + s
#     return t
# a = test(100)
# print(a)
# print(a(20))
# print(a(50))
#
# #闭包3，自由变量：由外面函数传来的变量，叫做自由变量，但是自由变量如果被赋值为不可变数据类型，就不再是自由变量了
# #nonlocal可以把变量标记为自由变量
# def test():
#     a = 0
#     def t(s):
#         a += s  #这里编译器已经提示有错误
#         return a
#     return t
#
# x = test()
# print(x(5))    #UnboundLocalError: local variable 'a' referenced before assignment
#
# def test():
#     a = []
#     def t(s):
#         a.append(s)  #这里编译器已经提示有错误
#         return a
#     return t
#
# x = test()
# print(x(5))  #这里输出[5]没毛病
#
# def test():
#     a = 0
#     def t(s):
#         nonlocal a #这句话作用是a是一个自由变量，去外面找去，这里没有你要的结果
#         a += s  #这里编译器已经提示有错误
#         return a
#     return t
#
# x = test()
# print(x(5))
#
#
#
#
# #property的使用，相当于把方法进行了封装，方便对对象的属性进行操作
# class Test():
#     def __init__(self):
#         self.__num = 100
#
#     def getNum(self):
#         return self.__num
#
#     def setNum(self, newnum):
#         self.__num = newnum
#
#
#     #如果是设置值则执行后面的函数，打印执行前面的函数
#     #里面函数的顺序取决于函数中是否有return，有return写在前面否则写在后面
#     s = property(getNum, setNum)
#
# a = Test()
# print(a.getNum())
# a.setNum(500)
# print(a.getNum())
#
# a.s = 300 #相当于调用了setNum(300)
# print(a.s) #相当于调用了getNum()
#
# 装饰器property
# class Test():
#     def __init__(self):
#         self.__num = 100
#
#     @property #写在get方法下面
#     def num(self):
#         return self.__num
#
#     @num.setter #写在设置方法下面
#     def num(self, newnum):
#         self.__num = newnum
#
# a = Test()
# a.num = 200
# print(a.num)
#
# # 迭代器以及可迭代对象
# #可迭代对象：1.集合数据类型：字符串，列表,元组，字典，集合，序列
# #            2.generator（生成器对象），包括生成器和带yield的generator function
# from collections import Iterable
# print(isinstance([1,2,3,4,5],Iterable))
# a = [1,2,3,4,5,6]
# print(iter(a))
# b = iter(a)
# print(b)
# print(id(iter(a)))
# print(id(b))
# print(id(a))
#
# # 装饰器
# def test(a):
#     def t():
#         print("----begin test----")
#         a()
#         print("----end test----")
#     return t
#
# @test #功能相当于pp = test(pp)
# def pp():
#     print("seagull is a good man")
#
# pp()
#
# #两个装饰器
# def w1(func):
#     print("++++++++++++")
#     def pp():
#         print("----w1----")
#     return pp
#
# def w2(func):
#     print("-------------")
#     def pp():
#         print("----w2----")
#     return pp
#
# #这里是先内后外，先执行@w2，也就是hello = w2(hello)，这里调用了w2,会有"-----"
# #的输出，然后执行@w1，也就是hello = w1(hello)，这里hello重新指向了新的对象，因此
# #会输出新的"+++++"，并且最终状态就是hello = w1(hello)，调用hello就等于调用w1的pp()
# @w1
# @w2
# def hello():
#     print("---hello----")
#
# def world():
#     print("---world----")
#
# hello()
#
# #当函数参数是不可变类型时，函数对其的改变实际上时开启了一个新的空间作为原对象的副本
# a = 100
# b = 200
# print(id(a),id(b))
# def addaa(x,y):
#     x += 10
#     y += 10
#
#     return x,y,id(x),id(y)
# addaa(a,b)
# print(addaa(a,b))
# print(a,b)
# print(id(a),id(b))
#
# #当函数参数时可变数据类型时，函数是直接对原对象进行操作
# q = [1,2,3,4]
# f = 5
# print(id(q))
# def sddd(x):
#     q.append(x)
#     return q,id(q)
# sddd(f)
# print(q)
# print(id(q))
# print(sddd(f))
#
#
#
# #作用域LEGB规则 locals（局部） -> enclosing function（外嵌） -> globals（全局） -> builtins（内建）
# num = 100
# def a():
#     # num = 200
#     def b():
#         # num = 300
#         print(num)
#     return b
# x = a()
# x()
#
# #动态语言添加属性
# #动态语言：可以在运行过程中修改代码
# #静态语言：编译时已经确定好代码，运行过程中不能修改
# class Rerson():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# a = Rerson("seagull",17)
# a.add = "a"
# b = Rerson("lopp",18)
# print(a.add)
# print(id(a))
# print(id(b))
#
# #动态语言添加方法
# import types
# class Rerson():
#     def __init__(self,name):
#         self.name = name
#
# def run(self):
#     print("-------%s-------"%self.name)
#
# #如果直接a.run = run，a无法作为参数self传递给run方法
# a = Rerson("asd")
# a.run = types.MethodType(run,a) #这里第一个参数是函数名，第二个参数是需要传递给函数的参数
# a.run()
#
# #__slots__用法：用于防止动态创建没有的属性
# import types
# class Rerson():
#     __slots__ = ("name","age")
#
# a = Rerson()
# a.name = "seagull"
# print(a.name)
# a.age = 17
# print(a.age)
# # a.addr = "hshsxhshsh"
# # print(a.addr)
#
# #生成器： 保存一种计算方式，在Python中一边循环一遍计算的机制成为生成器
# b = (x*2 for x in range(7))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
#
# def feibo():
#     print("----start----")
#     a, b = 0, 1
#     for i in range(5):
#         yield b    #代码执行到这里的时候会暂停，等待下一次调用
#         a, b = b, a + b
#     print("----stop----")
#
# x = feibo()   #这里的x是一个生成器对象
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# for num in x:
#     print(num)
#
# def test():
#     i = 0
#     while i < 5:
#         t = yield i  #前面按照正常顺序执行代码，当yield i的时候，程序等待下次调用
#         print(t)     #只要没有send传递值，t就一直为none而不是yield i，send本身不调用yield
#         i += 1
# g = test()
# print(next(g))
# print(next(g))
# g.send("seagull")
# g.send(None)   #可以直接调用而不再next之后在进行send调用，但是没啥意义
#
# # 这个好像也不是很有意义但是有时候可能会用到
# def test():
#     i = 0
#     while i < 5:
#         if i == 0:
#             t = yield i
#             print(t)
#         else:
#             yield i
#         i += 1
# g = test()
# g.__next__()
# g.send("seagull")
# print(next(g))
# print(next(g))
#
# #生成器多任务，看上去同时执行而已，协程
# def t1():
#     while True:
#         print("----1----")
#         yield None
#
# def t2():
#     while True:
#         print("----2----")
#         yield None
#
# te1 = t1()
# te2 = t2()
# while True:
#     te1.__next__()
#     te2.__next__()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
