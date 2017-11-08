# -*- coding: UTF-8 -*-
# print ("哈哈哈");
# ''''多行注释，使用单引号'''
# """多行注释，，使用双引号"""
# raw_input("\n\n执行后就会等待用户输入，按回车键后就会退出.\n");

# import sys;x='runoob';sys.stdout.write(x+'\n');
# 不换行输出
# x = "a";
# print x,
# 不换行输出
# y = 'b';
# print y;
# if True:
#     print "Answer"
#     print "True"
# else:
#     print "Answer"
#     print "False"
# 2017年11月6日23:51:34
# http://www.runoob.com/python/python-basic-syntax.html
# 多个语句构成代码组
# 在python里标识符由字母、数字、下划线组成、
# 在Python里，，所有标识符可以包含英文、数字以及下划线、但不能以数字开头
# Python中的标识符是区分大小写的
# 以下划线开头的标识符是有特殊意义的。以单下划线开头_foo的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用from xxx import *而导入
# 以双下划线开头的__foo代表类的私有成员，
# 以爽下划线开头和结尾的__foo__代表Python里特殊方法专用的标识，如__init__()代表类的构造函数
# Python可以同一行显示多条语句，方法是用分号；分开，  print 'hello';print 'merbng'
# python的保留字符，不能用作常数或变数，或任何其他标识符名称。所以Python的关键字只包含小写字母
# and exec not assert finally or break for pass class from print
# continue global raise def if return del import try elif
# in while except lambda yidld
# 学习 Python 与其他语言最大的区别就是，Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。python 最具特色的就是用缩进来写模块。
# 因此，在; Python  的代码块中必须使用相同数目的行首缩进空格数。
# 建议你在每个缩进层次使用单个制表符或两个空格或四个空格, 切记不能混用
# Python语句中一般以新行作为语句的结束符。但是我们可以使用斜杠\ 将一行的语句分为多行显示
# """
# total =item_one +\
#  item_two+\
#  item_three
#  """
# counter =100 #赋值整数型变量
# miles =1000.0 #浮点型
# name = "John" #字符串
# print counter
# print miles
# print name

# Python允许你同时为多个变量赋值。例如：
# a =b =c =1
# print a,b,c

# Python有五个标准的数据类型：
# Numbers(数字)
# String(字符串)
# List(列表)
# Tuple(元组)
# Dictionary(字典)

# Python支持四种不同的数字类型：
# int(有符号整形)
# long(长整形，也可以代表八进制和十六进制)
# float(浮点型)
# complex(复数)

# s ='ilovepython'
# s[1,5] 的结果是love

# 加号（+）是字符串连接运算符，星号（*）是重复操作。
# str = 'Hello world!'
# print str
# print str[0]           # 输出字符串中的第一个字符
# print str[2:5]         # 输出字符串中第三个至第五个之间的字符串
# print str[2:]          # 输出从第三个字符开始的字符串
# print str*2            # 输出字符串两次
# print str +"TEST"      # 输出连接的字符串

# list =['merbng',786,2.22,'john',77.2]
# tinylist =[123,'john']

# print list                   # 输出完整列表
# print list[0]                # 输出列表的第一个元素
# print list[1:3]              # 输出第二个至第三个元素
# print list[2:]               # 输出从第三个开始至列表末尾的所有元素
# print tinylist*2             # 输出列表两次
# print list+tinylist          # 打印组合的列表

# 元组是另一个数据类型，类似于List（列表）。
# 元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
# tuple =('merbng',766,2.34,'john',70.2)
# tinytuple =(134,'john')
# print tuple               # 输出完整元组
# print tuple[0]            # 输出元组的第一个元素
# print tuple[1:3]          # 输出第二个至第三个的元素
# print tuple[2:]           # 输出从第三个开始至列表末尾的所有元素
# print tinytuple * 2       # 输出元组两次
# print tuple + tinytuple   # 打印组合的元组

# tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
# list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
# tuple[2]=1000 # 元组中是非法应用
# list[2]=1000 # 列表中是合法应用

# 字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。
# 两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
# dict ={}
# dict['one']='this is one'
# dict[2] ='this is two'
# tinydict ={'name':'john','code':113,'dept':'sales'}
# print dict['one']
# print dict[2]
# print tinydict
# print tinydict.keys()
# print tinydict.values()

# 2017年11月7日23:53:08
# http://www.runoob.com/python/python-operators.html

#Python算术运算符
a = 21
b = 10
c = 0
c =a+b
print "a+b的值：",c
c=a-b
print "a-b的值：",c
c=a*b
print "a*b的值",c
c=a/b
print "a/b",c
#幂 - 返回x的y次幂
a=3
b=2
c=a**b
print "a**b的值：",c
#取整除 - 返回商的整数部分
a=10
b=5
c=a//b
print "a//b的值：",c
#Python2.x 里，整数除整数，只能得出整数。如果:要得到小数部分，把其中一个数改成浮点数即可。

#Python比较运算符
a=10
b=20
print "a==b:",a==b
print "a!=b:",a!=b
print "a<>b:",a<>b
print "a>b:",a>b
print "a<b:",a<b
print "a>=b:",a>=b
print "a<=b:",a<=b
if(a<b):
    print "a<b"
else:
    print "a!<b"

#Python赋值运算符
a=10
b=20
c+=a
print "c+=a",c# c= c+a
c-=a
print "c-=a",c# c= c-a
c*=a
print "c*=a",c
c/=a
print "c/=a",c
c%=a
print "c%=a",c

#Python位运算符
a=60
b=13
c=a&b
print "a&b",c

#Python逻辑运算符
a=10
b=20
if(a and b):
    print "变量a 和b 都为true"

#Python成员运算符
a=10
b=20
list ={1,2,3,4,5,6}
if(a in list):
    print "a 在给定的列表list中"
else:
    print "a不在list中"

if(a not in list):
    print "a不在list"
else:
    print "a在列表"

#Python身份运算符
#	is 是判断两个标识符是不是引用自一个对象
a=20
b=20
if(a is b):
    print "a和b有相同的标识"
else:
    print "a和b没有相同的标识"

if( a is not b):
    print "a和b没有相同的标识"
else:
    print "a和b有相同的标识"
b=30
if(a is b):
    print "a和b有相同的标识"
else:
    print "a和b没有相同的标识"
#is 与 == 区别：
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。

#2017年11月9日00:20:06
#http://www.runoob.com/python/python-if-statement.html



