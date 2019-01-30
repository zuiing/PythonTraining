"""【Day 4】
判断语句（要求掌握多条件判断）
循环语句
三目表达式
容器
可迭代对象
迭代器
生成器
--------------------------------------
"""
# -----------------判断语句---------------------
# 1）if判断语句  关系运算符和逻辑运算符（and or）
# age=int(input("请输入一个年龄"))
# if age >= 0 and age <= 14:
#     print("kid")
# elif(age<18):
#     print("teenager")
# else:
#     print("adult")
# 2）循环语句
# ***第一种是for...in循环，依次把list或tuple中的每个元素迭代出来
# classmates=["Alice",'Bob',"Berry"]
# print("班上同学有：")
# for name in classmates:
#     print(name)
# sum=0  #求1~100的和  需注意range(a,b)函数不包括b的值
# for x in range(1,101):
#     sum+=x
# print(sum)
# ***第二种循环while
# sum=0
# a=100
# while a>0:
#     sum+=a
#     a-=1
# print(sum)
# break 提前结束循环 continue跳过当前的这次循环，直接进入下一次循环
# -----------------三目表达式----------------
# 求两个数的较大值
# x=input("请输入第一个整数")
# y=input("请输入第二个整数")
# print("较大的那个数为：",x if x>=y else y)
# z=input("请输入第三个整数")
# print("三个数中的最大值为:",(x if x>y else y) if (x if x>y else y)>z else z)
# --------------容器 高级特性---------------------
# 1）切片 取list或tuple的前部分元素
# L1=["abc","def","hij",11,22,33]
# # 取前n个元素，可用索引0~n-1
# data=[]
# n=3
# for i in range(n):
#     data.append(L1[i])
# print(data)
# 但是用上面的循环比较繁琐 因此python提供了切片操作符
# data=L1[0:3] #slice同样支持倒数切片
# data2=L1[-3:] #取后三个  如果只有冒号就是取所有数
# print(data2)
# 2) 容器（containter）容器中的元素可以逐个迭代获取，可以用in not in判断是否在容器中
#   这类数据结构把所有的元素存储在内存中（也有特例，并不是将所有的元素放在内存，如迭代器和生成器对象）
# list=['a','b',1,2,[3,4]]
# tuple=['元素','不可变','没有','追加或插入','函数']
# dict={'name':'alice','age':18,'hobby':'painting'}
# set={1,2,3,3,4,5,'a','b','a','c'} #重复的元素会被自动过滤
# str="12345abcdefg"
# print(set)
# print("key值属于dict：",'name'in dict,"value值不是dict的元素：",'alice' in dict)
# 3)可迭代对象(iterable)：可直接用于for循环的对象统称为可迭代对象，上述容器都是可迭代对象，此外
# 处于打开状态的files、sockets等，但凡是可以返回一额迭代器的对象都是可迭代对象
# it=iter(list) #it是一个迭代器，内部持有一个状态没用于记录当前迭代所在位置，以便下次迭代的时候获取元素
# print(type(it))
# for elem in list:
#     print(it)
# 迭代器有一种具体的迭代器类型，如list_iterator,set_iterator 可迭代对象实现了__iter__方法
# 该方法返回一个迭代器对象
# 4)生成器generator：将列表元素按照某种算法推算出来
# L2=[x*x for x in range(10)]
# print(L2)
# g=(x*x for x in range(10))
# print(g) #打印的是当前元素所在位置
# print(next(g),next(g),next(g))
# print(next(g),next(g),next(g))
# for i in g:
#     print(i)
# ***定义一个fib（）函数
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n+=1
    return 'done'
# print(fib(5)) #调用fib()
def fib2(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n+=1
    return 'done'
g2=fib2(3)
# print(g2)
# print(next(g2),next(g2),next(g2),"迭代到此结束：")
# print("下面将出现报错：",next(g2))
# 总结：generator和函数执行流程不同，函数是顺序执行，而变成generator的函数。
# 在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
# 5）迭代器iterator 任何实现了__iter__和__next__()方法的对象都是迭代器
# 可使用isinstance()判断一个对象是否是iterable对象
# from collections import Iterable
# print(isinstance([],Iterable))
# print(isinstance('abc',Iterable))
# print(isinstance(100,Iterable))

# Day4作业
"""【作业构想】
学习代码200-300行
【作业构想】
学习代码200-300行
请对方输入一个0-9之间的数字，进行检查，若不是数字提示：您输入的不是数字，请输入0-9间的数字，若数字不在0-9范围内，提示用户输入0-9之间的数字，直至用户输入正确。
系统随机生成一个长度为3的数字列表，且列表中元素在0-9之间并且不相等。将用户输入与该列表进行比较，若为列表第一个元素，则荣获第一名，列表第二个元素，则荣获第二名，列表第三个名字，则荣获第三名，否则提示用户未得奖，
输入1重新开始游戏，输入2则结束游戏。
注意：每次游戏中列表中数字要求随机生成，每轮游戏都不相等。
-------------------------------------"""
import random
flag=True
while flag:
    # 1)输入0~0之间的数字
    while True:
        global a
        a = input("请输入一个0~9之间的数字：")
        if a.isdigit()==False:
            continue
        a=int(a)
        if a >= 0 and a <= 9:
            break
    # 2）随机生成长度为3的随机列表
    winlist = random.sample(range(0, 9), 3)
    print("随机产生的中奖号码为:", winlist)
    # 3)确定奖项
    if a in winlist:
        print("恭喜获得%d等奖" % (winlist.index(a) + 1))
    else:
        print("没有中奖")
    n=int(input("输入1重新开始游戏，输入2则结束游戏"))
    if n==2:
        print("游戏结束！")
        flag=False
