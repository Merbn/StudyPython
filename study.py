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

# Python算术运算符
# a = 21
# b = 10
# c = 0
# c =a+b
# print "a+b的值：",c
# c=a-b
# print "a-b的值：",c
# c=a*b
# print "a*b的值",c
# c=a/b
# print "a/b",c
# #幂 - 返回x的y次幂
# a=3
# b=2
# c=a**b
# print "a**b的值：",c
# #取整除 - 返回商的整数部分
# a=10
# b=5
# c=a//b
# print "a//b的值：",c
# Python2.x 里，整数除整数，只能得出整数。如果:要得到小数部分，把其中一个数改成浮点数即可。

# Python比较运算符
# a=10
# b=20
# print "a==b:",a==b
# print "a!=b:",a!=b
# print "a<>b:",a<>b
# print "a>b:",a>b
# print "a<b:",a<b
# print "a>=b:",a>=b
# print "a<=b:",a<=b
# if(a<b):
#     print "a<b"
# else:
#     print "a!<b"

# Python赋值运算符
# a=10
# b=20
# c+=a
# print "c+=a",c# c= c+a
# c-=a
# print "c-=a",c# c= c-a
# c*=a
# print "c*=a",c
# c/=a
# print "c/=a",c
# c%=a
# print "c%=a",c
#
# #Python位运算符
# a=60
# b=13
# c=a&b
# print "a&b",c

# Python逻辑运算符
# a=10
# b=20
# if(a and b):
#     print "变量a 和b 都为true"
#
# #Python成员运算符
# a=10
# b=20
# list ={1,2,3,4,5,6}
# if(a in list):
#     print "a 在给定的列表list中"
# else:
#     print "a不在list中"
#
# if(a not in list):
#     print "a不在list"
# else:
#     print "a在列表"

# Python身份运算符
#	is 是判断两个标识符是不是引用自一个对象
# a=20
# b=20
# if(a is b):
#     print "a和b有相同的标识"
# else:
#     print "a和b没有相同的标识"
#
# if( a is not b):
#     print "a和b没有相同的标识"
# else:
#     print "a和b有相同的标识"
# b=30
# if(a is b):
#     print "a和b有相同的标识"
# else:
#     print "a和b没有相同的标识"
# is 与 == 区别：
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。

# 2017年11月9日00:20:06
# http://www.runoob.com/python/python-if-statement.html
# Python 条件语句
# flag =False
# name ='luren'
# if name=='python':
#     flag=True
#     print "welcome bosss"
# else:
#     print name

# num =5
# if num ==3:
#     print 'boss'
# elif num==2:
#     print 'user'
# elif num==1:
#     print 'worker'
# elif num<0:
#     print "error"
# else:
#     print "roadman"

# 由于 python 并不支持 switch 语句，所以多个条件判断，只能用 elif 来实现，
# 如果判断需要多个条件需同时判断时，可以使用 or （或），表示两个条件有一个成立时判断条件成功；
# 使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功。
#
# num =9
# if num>=0 and num<=10:
#     print "hello"
#
# num=10
# if num<0 or num>10:
#     print 'hello'
# else:
#     print 'undfine'
#
# num =8
# if(num>=0 and num<=5)or(num>=10 and num<=15):
#     print 'hello'
# else:
#     print 'undefing'
# # 当if有多个条件时可使用括号来区分判断的先后顺序，括号中的判断优先执行，
# # 此外 and 和 or 的优先级低于>（大于）、<（小于）等判断符号，
# # 即大于和小于在没有括号的情况下会比与或要优先判断。
#
# var =100
# if(var==100):print '变量var的值为100'
# print 'Good bye!'

# a=0
# b=1
# if(a>0) and(b/a>2):
#     print 'yes'
# else:
#     print "no"
# if(a>0) or(b/a>2):
#     print '报错不执行yes2'
# else:
#     print "报错不执行no2"

# 一个简单的条件循环语句实现汉诺塔问题
# def my_print(args):
#     print args
#
# def move(n, a, b, c):
#     my_print ((a, '-->', c)) if n==1 else (move(n-1,a,c,b) or move(1,a,b,c) or move(n-1,b,a,c))
#
# move (3, 'a', 'b', 'c')
#

# 2017年11月9日23:32:23
# http://www.runoob.com/python/python-loops.html
# Python 循环语句
# count =2
# while (count<9):
#     print 'the count is',count
#     count=count+1
# print 'Good bye!'

# continue 和 break 的用法
# i = 1
# while i < 10:
#     i += 1
#     if i % 2 > 0:  # 非双数时跳过输出
#         continue
#     print i  # 输出双数2、4、6、8、10
#
# i = 1
# while 1:  # 循环条件为1必定成立
#     print i  # 输出1~10
#     i += 1
#     if i > 10:  # 当i大于10时跳出循环
# #         break

# var =1
# while var==1:
#     num =raw_input('enter a number :')
#     print 'you input :',num
#
# print 'good bye！'

# 在 python 中，while … else 在循环条件为 false 时执行 else 语句块：
# count =0
# while count<5:
#     print count,' is less than 5'
#     count=count+1
# else:
#     print count,'is not less than 5'

# 类似 if 语句的语法，如果你的 while 循环体中只有一条语句，你可以将该语句与while写在同一行中
# flag =1
# while(flag):print 'given flag is really true !'
# print 'good bye~！'

# 九九乘法表
# i=1
# while i:
#     j=1
#     while j:
#         print j,'*',i,'=',i*j,' ',
#         if i==j:
#             break
#         j+=1
#         if j>10:
#             break
#
#     print '\n'
#     i+=1
#     if i>=10:
#         break

# 摇筛子游戏
# import random
# import sys
# import time
#
# result =[]
# while True:
#     result.append(int(random.uniform(1,7)))
#     result.append(int(random.uniform(1,7)))
#     result.append(int(random.uniform(1,7)))
#     print result
#     count=0
#     index =2
#     pointStr =""
#     while index>=0:
#         currPoint =result[index]
#         count+=currPoint
#         index -=1
#         pointStr +=" "
#         pointStr+=str(currPoint)
#     if count<=11:
#             sys.stdout.write(pointStr+' -> '+'小'+'\n')
#             time.sleep(1)
#     else:
#             sys.stdout.write(pointStr+' ->'+'大'+'\n')
#             time.sleep(1)
#     result=[]

# 猜拳小游戏
# import random
# while 1:
#     s =int(random.randint(1,3))
#     if s==1:
#         ind ='石头'
#     elif s==2:
#         ind ='剪刀'
#     elif s==3:
#         ind ='布'
#     m=raw_input('输入 石头、剪刀、布，输入"end"结束游戏：')
#     blist=['石头','剪刀','布']
#     if(m not in blist)and(m!='end'):
#             print '输入错误，清重新上输入！'
#     elif (m not in blist)and (m=='end'):
#             print '\n游戏退出中...'
#             break
#     elif m==ind:
#             print '电脑出了：'+ind+',平局！'
#     elif (m=='石头'and ind=='剪子')or(m=='剪子'and ind =='布')or (m=='布'and ind =='石头'):
#             print '电脑出了：'+ind+',你赢了！'
#     elif (m=='石头'and ind =='布')or(m=='剪子'and ind =='石头')or (m=='布'and ind =='剪刀'):
#             print '电脑出了：'+ind+'，你输了!'

# 猜大小的游戏
# import random
# s =int(random.uniform(1,10))
# print s
# m=int(input('输入整数：'))
# while m!=s:
#     if m>s:
#         print '大了'
#         m=int(input('输入整数：'))
#     if m<s:
#             print '小了'
#             m=int(input('输入整数：'))
#     if m==s:
#              print 'ok'
#              break

# 2017年11月12日01:16:12
# Python for 循环语句
# http://www.runoob.com/python/python-for-loop.html
# Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
# for letter in 'Python':
#     print '当前字母：',letter
#
# fruits =['bananaa','apple','mango']
# for fruit in fruits:
#     print '当前水果：',fruit
#
# print 'good bye!'

# 通过序列索引迭代(len() 返回列表的长度，即元素的个数。 range返回一个序列的数)
# fruits =['banana','apple','mango']
# for index in  range(len(fruits)):
#     print '当前水果：',fruits[index]
# print 'good bye!'

# 循环使用 else 语句
# for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完
# for num in range(10, 20):
#     for i in range(2, num):
#         if num % i == 0:
#             j = num / i
#             print '%d 等于 %d * %d' % (num, i, j)
#             break
#     else:
#             print num, '是一个质数'

# Python 循环嵌套
# 允许在一个循环体里面嵌入另一个循环。

# Python for 循环嵌套语法：
# for iterating_var in sequence:
#     for interating_var in sequence:
#         statements(s)
#     statements(s)

# Python while 循环嵌套语法：
# while expression:
#     while expression:
#         statements(s)
#     statements(s)
# 可以在循环体内嵌入其他的循环体，如在while循环中可以嵌入for循环， 反之，你可以在for循环中嵌入while循环。

# 嵌套循环输出2~100之间的素数：
# i =2
# while (i<100):
#     j=2
#     while(j<=(i/j)):
#         if not(i%j): break
#         j=j+1
#     if(j>i/j):print i,' 是素数'
#     i=i+1
# print 'good bye!'

# 2017年11月12日21:49:01
# http://www.runoob.com/python/python-strings.html
# Python 字符串Python 字符串
# var1 ='Hellow WORLD!'
# var2='Python Runoob'
#
# print 'var1[0]:',var1[0]
# print 'var2[1:5]:',var2[1:5]

# var1 ='Hello World!'
# print '更新字符串：-',var1[:6]+'Runboo!'

# 在需要在字符中使用特殊字符时，python用反斜杠(\)转义字符

# Python 字符串格式化
# print 'my name is %s and weight is %d kg!' %('merbng',21)

# python中三引号可以将复杂的字符串进行复制:
# hi ='''hi
# there'''
# hi
# 'hi\nthere'
# print hi

# hi
# there

# Unicode 字符串
# u'Hello World!'
# print u'Hello world!'
# print u'Hello\u0020world!'

# Python 列表(List)
# 访问列表中的值
# list1 =['pytsics','cchemistor','1992',22,999]
# list2= [1,2,3,4,5,6,7,8]
# print 'list1[0]:',list1[0]
# print 'list2[1:5]：',list2[1:5]
# 更新列表
# print 'value available at index 2:'
# print list1[2]
# list1[2]=2001
# print 'new value avaliable at index 2:'
# print list1[2]
# # 删除列表元素
# del list1[0]
# print list1

# 2017年11月14日00:05:02
# Python 元组
# http://www.runoob.com/python/python-tuples.html











