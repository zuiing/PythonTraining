'''【Day 2】
基础
列表
标志
基本操作(创建，append( )，pop( ) ,del( ), 深浅拷贝）
列表相关方法
元组
标志
基本操作（创建及不可变性）
提升
序列类型，相互转换及方法
'''
# ---------------python基础 运算符----------------
# # 1）算数运算符 + - * / %  **(返回x的y次幂)  //取整除，向下取整
# a=2
# b=10
# print('%d的%d次幂为：%d'%(a,b,a**b))
# # 即使下面的代码中第三个占位符为%f得到的也是取整后的浮点数
# print('%d除以%d取整除数为：%d'%(9,2.0,9//2.0))
# # 2)比较运算符 == ！+ <> (类似于！=,但python3.6不支持该运算符) >= <=
# print(1!=2)
# # 3)赋值运算符 = += -= *= /= %= **= //=
# # 4）位运算符 & | ^ ~ << >>
# # 5)逻辑运算符 and or not
# c=1
# d=2
# if c and d:
#     print('c和d都为true')
# else:
#     print('c和d至少有一个不为true')
# c=0
# if not(c and d):
#     print('c和d至少有一个为false')
# else:
#     print('c和d都为true')
# # 6）成员运算符 in   not in 在指定序列中找到值
# a=10
# b=20
# list=[1,2,3,4,5,10]
# if a in list:
#     print('变量a在list中')
# else:
#     print('变量a不在list中')
# if b not in list:
#     print('变量b不在list中')
# else:
#     print('变量b在list中')
# # 7）身份运算符 is is not判断两个标识符是不是引用自一个（不同）对象
# #    注：id()函数用于获取对象内存地址
# # is用于判断两个引用对象是否为同一个，而==判断引用变量的值是否相同
# a=20
# if (a is b):
#     print('a和b有相同的标识')
# else:
#     print('a和b没有相同的标识')
# if (a is not b):
#     print('a和b没有相同的标识')
# else:
#     print('a和b有相同的标识')
# # 8）运算符优先级 太难记了 我还是乖乖地用小括号吧
# ---------------------列表--基本操作(创建、append()、pop()、del()、深浅拷贝)-------------------
# list是一种有序的集合 可以随时添加和删除其中的元素
classMates=['Alice','Bob','Berry']
print(classMates)
print('该列表的长度为',len(classMates))
# 用索引来访问list中每一个位置的元素，索引从0开始
# 还可以用-1做索引，直接获取最后一个元素 -2 -3一次类推
print('列表中第三个名字为：%s,倒数第一个为%s'%(classMates[2],classMates[-1]))
# list是一个可变的有序表，可以往list中追加元素到末尾
classMates.append('Adam')
# 也可以把元素插入到指定的位置，比如索引号为2
classMates.insert(2,'Jenny')
print(classMates)
# 用pop()函数删除末尾元素,用pop(i)删除索引为i的元素
classMates.pop(3)
# del删除列表的元素 貌似和pop()没啥区别，同样是能够删除指定元素
del classMates[0]
print(classMates)
# list脚本操作符  + *这两种操作符与字符串相似，用于组合和重复
print(len([1,2,3]+[4,5,6]))
L1=['Hi','you are so cute']*2
print(L1*2)
print('hi' in L1)
for x in [1,2,3,['a','b']]:
    print(x)
# list列表截取实例
L2=["Google","Zhifubao","Tencent"]
print(L2[2])
print(L2[-1])
print(L2[1:])
# 把某个元素替换成别的元素，可以直接赋值给对应的索引
classMates[2]='Jennnnnny'
print(classMates)
# list里的数据类型也可以不同，真是厉害了
list2=['apple',123,True]
print(list2)
# list元素也可以是list类型的值
list3=['python','java',classMates] # 简直就是个二维数组
print(list3)
print('list3列表里的classMates列表的第一个名字为：',list3[2][1])
# list函数&方法  cmp(list1,list2)这个方法不能用？
# print(cmp([1,2],[1,2]))
print(max([1,3,5]),min([1,3,5]))
seq = ('a','1',10.0)
# print(type(seq))
L3 = list(seq)
print(seq , L3)
# list方法
L4=[1]
print(L4)
L4.append('a')
print(L4)
# # -----------------------元祖-基本操作(创建及不可变性)---------------------------
# # tuple有序列表，与list类似，但是一旦初始化就不难修改，使用括号进行初始化
# classMates=('Bob','Alice')
# print(classMates)
# # 没有append() insert()这样的方法，但获取元素的方法和lisy一样，但不能被赋值为其他的元素
# # tuple意义：不可变，代码更安全
# t1=(1,2,3)
# print(t1)
# t2=() # 空的tuple
# print(t2)
# t3=(3)  # 这种写法定义的是3这个数
# t4=(2,) # 这种写法才是定义的才是含有一个元素的tuple变量
# print(type(t3),type(t4),"   t4里的元素为：",t4)
# t5=('a','bcd',[1,2])
# print(t5)
# t5[2][0]=100 # 其实说不能变的也不见得！
# t5[2][1]=200 # tuple变量中指向的list值可变，只是说tuple第三个元素保存的地址不能变了
# print(t5) # tuple中保存的只是地址或者说是确定的对象
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# print(L[0][0])
#
# # 疑问：为什么说list和tuple是有序集合，哪里有序了？？？
#
# Day2作业：
family=['巴巴','麻麻','哥哥','嫂嫂','大侄女儿','女朋友','男朋友']
print(family)
newElement=input('请输入要加入的成员')
family.insert(2,newElement)
print(family)
family.remove('男朋友')
print('把男朋友删除之后家庭成员还剩：',family)
