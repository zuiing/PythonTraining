# !/usr/bin/env/python3
# coding='utf-8'
# 通常开头写上上面两行，第一行为了告诉Linux/os x系统，这是一个python可执行程序，Windows会忽略这个注释
# 第二行是告诉python编译器，按照utf-8编码读取源代码，否则，在源代码中写的中文可能会有乱码
# 申明utf-8并不意味着.py文件就是utf-8编码的，必须要确保文本编辑器正在使用utf-8 without BOM编码

# -----------环境搭建--------------
# 编译环境使用的是pyCharm,因为之前就已经装好了，而且装了一些其他的库，
# 对anaconda不了解，等过两天不忙了自己再去配置下

#-------------python初体验----------
# 1)命令行模式下，可以执行pyhton进入Python交互式环境，可以执行.py文件(只能在命令行模式执行)
#   但交互式命令行程序可直接得到结果却无法保存
# 2)print & input
# print('This is a string, you can print whatever you want! ')
# print('Also,you can print the results of calculation directly,such as:',123*456)
# a=input('You can input a string and it will be saved in this variable\n')
# print('Now we can verify variable a has saved your string',a)
# print('The default coding in Python is tuf-8')


# ------------python基础----------------------
# 1)#注释单行  '''可注释多行'''
# 2)colon : 以：结尾时，缩进的语句视为代码块
# 3) dir() and help() import
#    dir()为python内置函数，不带参数时，返回当前范围内的变量、方法和定义的类型列表
#    不带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用
#    help()查看函数或模块用途的详细说明
#    import用于动态加载类和函数
# 4)pep8 Python编码规范
#

# -----------python数值基本知识---------------
# 1)数据类型
#   在python中能直接处理的数据类型有 int、long、float、complex、string、bool、none and bytes?
#   escape character \ is very useful
# print('I\'m \"OK\"')
# print('''line1
# ...line2
# ...line3''')
# python中 r'' 表示‘’内的字符默认不转义
# print(2!=2)
# 2) 变量 变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言
#    常量 在Python中，通常全部大写的变量名表示常量
# a = 100  # a is an integer
# print(a)
# a = 'abc'  # a becomes a string
# print(a)
# print('when you create a variable:s1='abc', python interpreter do two things:')
# print('在内存中创建了一个'abc'的字符串；在内存中创建了一个名为s1的变量，并把它指向'abc'。下面几句代码可以说明:')
# a='abc'
# b=a
# a='xyz'
# print(b)#b依然指向abc字符串
# 3) 运算符号 /除法(结果是浮点数) //地板除(结果永远是正数) %取余
# s1='hello,world'
# s2='hello,\'Adam\''
# s3=r'hello,"Bart"'
# s4=r'''Hello,
# Lisa'''
# print(s1,s2,s3,s4)

# ---------------string字符串------------------------
# 1)字符串是由数字、字母、下划线组成的一串字符，一般记为s=‘123abc_’
# 2)python字串索引有2种取值顺序
# s='123abc&*%_)'
# print(s[1:5]) # 从左到右默认从0开始索引
# print(s[-5:-1]) # 从右到左默认从-1开始，最大范围是字符串开头
# print(s[0],s[2],s[4])
# print(s[2:]) #从第二个字符开始输出
#print(str * 2) # 字符串的* 和+ 操作在命令行实现成功，但在交互式命令执行失败
#print(str+'connectString')
# 3)在python3中，字符串是以Unicode编码，支持多语言
# print(ord('0'))
# print(chr(48))
# print('\u4e2d\u6587')
# print(ord('中'))
# print(ord('文'))
# 4)python对bytes类型的数据用带b前缀的单引号或双引号表示
# s1=b'abc'
# print(s1)
# print(s1.decode('ascii'))
# s2=b'\xe4\xb8\xad\xe6\x96\x87'
# print(s2)
# print(s2.decode('utf-8')) #解码
# s3='中文abcd'
# print(len(s3))  #result：6
# print(len(s3.encode('utf-8'))) #result：10
# 中文字符经utf-8编码之后占3个字符，而一个英文字符占用1个字节
# 5)格式化输出字符串  %s会把任何数据类型转换为字符串
# print('%d-%d-%d,%s,%.2f'%(2019,1,26,'report',123.456))
# print('%s'%(123.456))
# 6)format()另一种格式化字符串的方法，会将传入的参数依次替换字符串内的占位符
# print('hello,{0},感谢你为我检查作业,下面检测小数输出{1:.1f}'.format('方同学',100.123))
# 7)str和bytes互相转换时，需要指定编码，最长用的编码是utf-8.
