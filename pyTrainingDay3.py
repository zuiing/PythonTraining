"""【Day 3】
【dict字典】
定义
创建
字典的相关方法
-----------------------------------
【set集合】
特性
创建
方法
-------------------------------------
【file文件读取】
 打开文件方式（读写两种方式）
文件对象的操作方法
*学习对excel及csv文件进行操作*
**内容为选做内容，可根据自己基础决定是否做此内容
--------------------------------------
【作业构想】
学习代码200-300行
读取一个文件【文件将在之后给出】，将文件中转换为字典，key值为学习项目，
value值为一个负责人列表，并判断字典中是否有负责人负责多个学习项目。"""
# ------------------dict字典---------------------
# 1）python内置字典，在其他语言中也称map，使用（key-value)存储，具有极快的查找速度
# names=['Alice','Bob','Tracy']
# scores=[99,90,59]
# a=input('请输入你想查询的同学的名字')
# a_index=names.index(a)
# print("%s的成绩为：%d"%(a,scores[a_index]))
# 用dict实现，只需一个 名字：成绩的对照表
# d1={'Alice':99,'Bob':90,'Tracy':59}
# # a=input('请输入你想查询的同学的名字')
# # print("%s的成绩为：%d"%(a,d1[a]))
# # 2)操作：存：可直接初始化或通过key值放入
# d1['Berry']=100
# # 3）key值不可重复，如果key不存在，dict会报错，判断key是否存在的方法
# #  通过in判断、通过dict提供的get()方法，若不存在返回none或自己指定的值
# print("第一种判断：",'alice' in d1,"   第二种判断：",d1.get('alice'))
'''总结：dict内部存放的顺序和可以、放入的顺序无关
和list相比：
  1、查找和插入的速度极快，不会随key值的增加而变慢
  2、需要占用大量的内存，内存浪费多
而list相反。
dict是空间换时间的一种方法，哈希表需要额外的内存记录映射关系
谨记：dict的key必须是不可变对象，key值计算位置的算法称为哈希算法
在python中，字符串、整数都是不可变的，因此可作为key，而list可变，不能作为key值  
'''
# -----------------set-----------------
# 和dict类似，也是一组key的集合，但不存储value，key值不重复
# # 1）set创建，需要提供一个list作为输入集合
# s1=set([1,2,3.0])
# print("类型：",type(s1),"  s1内部元素：",s1)
# s2=set(['a','b','c'])
# print("类型：",type(s2),"  s2内部元素：",s2)
# s3=set([1,2.0,'a'])
# print("类型：",type(s3),"  s3内部元素：",s3)
# 显示的{‘a',1，2.0}只是告诉你set内部有1，2，3这三个元素，显示的顺序也不表示是有序的
# # 2）重复元素在set中被自动过滤
# s4=set([1,2,2,2,3])
# print("s4的元素",s4)
# # 3)add()  remove()方法
# s4.add(2)
# s4.add(6)
# s4.remove(2)
# print(s4)
# 4）set可看成数学意义上的无序和无重复元素的集合，两个set可做交集、并集等操作
# s5=set(['a','b','c'])
# s6=set([1,2,3])
# print("s5和s6交集：",s5&s6,"  s5和s6并集：",s5|s6)
# 5）dict和set区别
# set没有存储对应的value，但是，set和dict原理一样，因此，不可放入可变对象
# -------------再议不可变对象-------------
# str是不可变，list是可变
# 1）对于可变对象list1，对list进行操作，list内部的内容会变化
# L1=[1,2,0]
# L1.sort()
# print("排序后：",L1)
# 2)对于不可变对象str
# s1="abcd"
# s2=s1.replace('a','A')
# print("替换之后的结果：",s2,"原来的字符串：",s1)
# s1=s2
# print("让s1重新指向另一个对象的结果：",s1)
"""上述现象解释：s1是变量，'abcd'是对象，s1指向的是对象(字符串常量)'abcd',
replace()方法会创建一个新字符串'Abcd',可以将定义s2指向新串
因此，对于不变对象来说，调用对象自身的任意方法，也不会改变自身的内容，
相反这些方法会创建新的对象并返回，保证变量本身不可变
"""
# ------------拓展-------------------
# tuple是不可变对象
# t1=(1,2,3)
# t2=(1,[2,3])
# s7=set(t1)
# s8=set(t2)
# print("成功示例：",s7,"不成功示例：",s8)
# 现象解释：t1的对象不可变，能成功，但t2的第二个元素指向一个list，而该list可变
# --------------file文件读写-----------------------
# 1)第一种读取方式：读取的是非UTF-8编码的文件时，要加上encoding=utf-8，读取的是文本文件
# f=open("homework.txt","r",encoding='UTF-8')
# print("1、全部读取：",f.read()) # 会将txt的全部内容一次性读取，如果文件太大，内存就会爆炸
# f.close()
# ***用try...finally能够保证无论是否出错都能正确的关闭文件
# try:
#     f=open("homework.txt","r",encoding='UTF-8')
#     print("2、只读10字节：",f.read(10)) #可以用read(size)方法读取size个字节
# finally:
#     if f:
#         f.close()
# # # ***引入with自动调用close()方法
# with open("homework.txt","r",encoding='UTF-8') as f:
#     print("3、只读一行：",f.readline())
# with open("homework.txt","r",encoding='UTF-8') as f:
#     L1=f.readlines()
# print("4、按行读取，将读取的内容放到list中：",L1)
# L2=[]
# for line in L1:
#     L2.append(line.strip())
# print("5、将末尾的\\n去掉",L2)
# 第二种读取方式：读取二进制文件。如图片、视频等，用‘rb’模式打开文件
# f=open("bg.jpg","rb")
# # print(f.read())  #读取的是像素值，以二进制进行读取的，为解码
# f.close()
# 2) 文件的写操作
# fo=open("output.txt","a")
# fo.write("先写入一个字符串")
# fo.writelines(['abc','123']) # list元素的类型只有是str时才能写入
# 3)拓展练习 读取csv文件（编码格式可以是ANSI或GB2312）及写入
import csv
# with open("input.csv",'r',encoding='ANSI') as csvfile:
#     read=csv.reader(csvfile)
#     # next(csvfile, None)
#     print(read)
#     for i in read:
#         print(i)
dic={"姓名":'Alice',"年龄：":'永远18'}
csvfile=open("input.csv",'w',newline='')
writer=csv.writer(csvfile)
for key in dic:
    writer.writerow([key,dic[key]])
csvfile.close()

# Day2作业
# 1、读取多行保存到L1列表
with open("homework.txt","r",encoding='UTF-8') as f:
    L1=f.readlines()
# 2、将每行以空格隔开，第一项作为字典的key值，第二、三项作为value
L=[] # 临时变量
L_all=[] #存储所有负责人的姓名
d={}
for line in L1:
    L=line.split()
    d[L[0]]=[L[1],L[2]]
    L_all.append(L[1])
    L_all.append(L[2])
# 3、判断是否有负责人负责多个集训
s=set(L_all)
# print("L_all长度：",len(L_all))
# print("去重后的长度：",len(s))
if len(L_all)>len(s):
    print("存在有负责人负责多个集训")
else:
    print("不存在负责人负责人负责多个集训")





