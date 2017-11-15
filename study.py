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
# Python的元组与列表类似，不同之处在于元组的元素不能修改。

# tup1 =(50,)#元组中只包含一个元素时，需要在元素后面添加逗号
# 元组与字符串类似，下标索引从0开始，可以进行截取，组合
# 元组可以使用下标索引来访问元组中的值
# tup1=('phthone','chemistory',1997,2999)
# tup2 =(1,2,3,4,5,6,7);
# print 'tup1[0]:',tup1[0]
# print 'tup2[1:5]:',tup2[1:5]

# 修改元组
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
# tup1=(12,34.56)
# tup2=('abc','xyz')
# tup3 =tup1+tup2
# print tup3

# 删除元组
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
# tup =('pythons','chemisotry',1997,2000)
# print tup;
# del tup;
# print 'after deleting tup :'
# print tup

# 元组运算符
# 与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。

# 元组索引，截取
# 因为元组也是一个序列，所以我们可以访问元组中的制定位置的元素，也可以截取索引中的一段元素，
# L =('spam','Spam','SPAM!')
# print L[2]   读取第三个元素
# print L[-2]  反向读取；读取倒数第二个元素
# print L[1:] 截取元素

# 无关闭分隔符
# 任何无符号的对象，以逗号隔开，默认为元组
# print 'abc',-4.233,18+65.6j,'xyz';
# x,y =1,2;
# print 'valuse of x ,y :',x,y

# 元组内置函数
# cmp(tuple1,tuple2) 比较两个元组元素
# len(tuple) 计算元组元素个数
# max(tuple) 返回元组中元素最大值
# min（tuple) 返回元组中元素最小值
# tuple(seq) 将列表转换为元组

# Python字典（Dictionary）
# 字典是另一种可变容器模型，且可存储任意类型对象
# 字典的每个键值（key =》value）对用冒号（：）分割，每个对之间用逗号（，）分割，
# 整个字典包括在花括号({})中
# d={key1:value1,key2:value2}
# 键必须是唯一的，但值则不必
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组
# dict = {'Alice': '1234', 'Bech': '918', 'Cecil': '3258'}
# dict1 = {'abc': 456}
# dict2 = {'abc': 123, 98.6: 37}

# 访问字典里的值
# 把相应的键放入熟悉的放括弧
# dict= {'Name':'Zara','Age':7,'Class':'First'}
# print "dict['Name]:",dict['Name'];
# print "dict['Age']:",dict['Age'];

# 如果用字典里没有的键访问数据，会输出错误
# print "dict['xx']",dict['xyz']

# 修改字典
# 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对，
# dict = {'Name': 'Zare', 'Age': 7, 'Class': 'First'}
# dict['Name'] = 'Merbng'
# dict['Age'] = 8;
# dict['School'] = 'DPS School'
# print "dict['Name']:", dict['Name']
# print "dict['School']:", dict['School']
# print dict

# 删除字典元素
# 能删单一的元素也能清空字典，清空只需一项操作
# 显示删除一个字典用del命令
# dict ={'Name':'Merbng','Age':8,'Class':'First'}
# del  dict['Name']
# dict.clear();
# del dict;
# print "dict['Age']",dict['Age']
# print "dict['School']:",dict['School']

# 字典键的特性
# 字典值可以没有限制的取任何Python对象，既可以是标准的对象，也可以是用户定义的，但键不行，
# 两个重要的点要记住：
# 1.不允许同一个键出现两次，创建时如果一个键被赋值两次，后一个值会被记住，
# dict ={'Name':'Mebng','Age':9,'Name':'Manni'}
# print dict
# print dict['Name']
# 2.键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行
# dict ={['Name']:'Zera','Age':7}#运行报错
# print dict
# print "dict['Name']:",dict['Name']

# 字典内置函数&方法
# cmp(dict1,dict2) 比较两个字典元素
# len(dict) 计算字典元素个数，即键的总数
# str(dict) 输出字典可打印的字符串表示
# type(variable) 返回输入的变量类型，如果变量是字典就返回字典类型

# Python字典包含了以下内置方法：
# dict.ckear()删除字典内所有元素
#dict.copy() 返回一个字典的浅复制
# dict.fromkeys(seq[, val]) 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
# dict.get(key,default =None) 返回指定键的值，如果值不存在字典中返回default值
# dict.has_key(key)如果键在字典dict里返回true，否则返回false
# dict.items()以列表返回可遍历的（键，值）元组数组
# dict ={'Name':'Mebng','Age':9}
# dict2 ={'Name':'xx','Age':9}
# print dict.items();
# print dict.has_key('Name')
# print dict.get('Name','Mmm')
# print dict.keys()#以列表返回一个字典所有的键
# print dict.update(dict2) 把字典dict2的键/值对更新到dict里
# print dict.values() 以列表返回字典中的所有值
# print dict.pop('Name','vvv')删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
# print dict.popitem()随机返回并删除字典中的一对键和值。


# Python 日期和时间
# 2017-11-14 14:49:59
# http://www.runoob.com/python/python-date-time.html

# import time
# ticcks =time.time()
# print '当前时间戳喂：',ticcks#时间间隔是以秒为单位的浮点小数。
#序号	 属性	         值
# 0	  tm_year	        2008
# 1	  tm_mon	        1 到12
# 2	  tm_mday	        1 到31
# 3	  tm_hour	        0 到23
# 4	  tm_min	        0 到59
# 5	  tm_sec	        0 到61 (60或61 是闰秒)
# 6	  tm_wday	        0到6(0是周一)
# 7	  tm_yday	        1 到366(儒略历)
# 8	  tm_isdst        	-1, 0, 1, -1是决定是否为夏令时的旗帜
# localtime =time.localtime(time.time())
# print '本地时间喂：',localtime

# 获取格式化的时间
# localtime =time.asctime(time.localtime(time.time()))
# print '本地时间为：',localtime

# 格式化日期
# 格式化成2016-03-20 11:45:39形式
# print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

# 格式化成Sat Mar 28 22:24:24 2016形式
# print time.strftime("%a %b %d %H:%M:%S %Y",time.localtime())

# 将格式字符串转换为时间戳
# a= "Sat Mar 22 22:22:22 2015"
# print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

# python中时间日期格式化符号：
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身

# 打印某月的月历
# import calendar
# cal =calendar.month(2015,1)
# print "以下输出2015年1月份的日历："
# print cal

# Time模块
# 日历（Calendar）模块
# 星期一是默认的每周第一天，星期天是默认的最后一天。

# 使用datetime模块来获取当前的日期和时间
# import datetime
#
# i =datetime.datetime.now()
# print ("当前的日期和时间是 %s"%i)
# print ("ISO格式的日期和时间是%s"%i.isoformat())
# print ("当前的年费是%s"%i.year)
# print ("当年的月份是%s"%i.month)
# print ("当前的日期是 %s"%i.day)
# print ("dd/mm/yyyy 格式是 %s/%s/%s"%(i.day,i.month,i.year))
# print ("当前小时是：%s"%i.hour)
# print ("当前分钟是：%s"%i.minute)
# print ("当前秒是： %s"%i.second)

# Python函数
# 语法
# def functionname(parameters):
#     "函数_文档字符串"
#     function_suite
#     return [expression]
# 参数值和参数名称是按函数声明中定义的的顺序匹配起来的。

# def printme(str):
#     "打印传入字符串到标准显示设备上"
#     print str
#     return
# printme("我要调用用户自定义函数")
# printme("再次调用同一个函数")

# python传不可变对象
# def ChangeInt (a):
#     a=10
#     return
#
# b=2
# ChangeInt(b)
# print b;
#
# # 传可变对象
# def changeme(mylist):
#     "修改传入的列表"
#     mylist.append([1,2,4,3,4])
#     print "函数内取值：",mylist
#     return
#
# mylist =[10,20,30]
# changeme(mylist)
# print "函数外取值:",mylist

#关键字参数
# def printme(str):
#     "打印任何传入的字符串"
#     print str;
#     return ;
#
# printme(str ="my string !")

# def printinfo(name ,age ):
#     "打印任何传入的字符串"
#     print "Name",name
#     print "Age",age
#     return ;
# printinfo(age =8,name ="hhahh")#关键字参数顺序不重要

# 缺省参数
# def printinfo(name,age= 355):
#     "打印任何传入的字符串"
#     print "name:",name
#     print "age",age
#     return
#
# printinfo("merbng",age =10);
# printinfo("Mbv")
#
# # 不定长参数
# def printinfo(arg1,*vartuple):
#     "打印任何传入的参数"
#     print "输出："
#     print arg1
#     for var  in vartuple:
#         print var
#     return
# printinfo(10,20)
# printinfo(3,12,4,5,6)

# 匿名函数
# Python使用lambda来创建匿名函数
# sum =lambda arg1,arg2:arg1+arg2;
# print "相加后的值喂：",sum(10,20)
# print "相加后的值为：",sum(20,33)

# def sum(arg1,arg2):
#     "返回两个参数的和"
#     total =arg1+arg2
#     print "函数内：",total
#     return total
# total =sum(10,20)

# 全局变量、局部变量
# total =0;#这是一个全局变量
# def sum(arg1,arg2):
#     total=arg1+arg2;#total在这里是局部变量
#     print "函数内是局部变量：",total
#     return total;
# sum(10,30)
# print "函数外是全局变量:",total

# 全局变量想作用于函数内，需加 global
# globvar =0
# def set_globvvar_to_one():
#     global globvar
#     globvar =1
#
# def print_globvar():
#     print (globvar)
#
# set_globvvar_to_one()
# print globvar
# print_globvar()

# 2017-11-14 22:57:14
# Python 模块
# http://www.runoob.com/python/python-modules.html

# 命名空间和作用域
# 一个Python表达式可以访问局部命名空间和全局命名空间里的变量，
# 如果一个局部变量和一个全局变量重名，则局部变量会覆盖全局变量
# 如果要给函数内的全部局部变量赋值，必须使用global语句
#
# Money=2000
# def AddMoney():
#     global Money
#     Money=Money+1
#
# print Money
# AddMoney()
# print Money

# dir()函数 一个排好序的字符串列表，内容是一个模块来定义过的名字
# 返回的列表容纳了模块里定义的所有的模块，变量和函数
# import math
# content =dir(math)
# print content

# globals()和locals()函数
# 根据调用地方不同，globals（）和locals（）函数可被用来返回全局和局部命名空间里的名字，
# 如果在函数内部调用locals（），返回的是所有能在该函数里访问的命名。
#如果在函数内部调用globasl（），返回的是所有在该函数里能访问的全局名字
# 两个函数的返回类型都是字典，所以名字们能用keys（）函数摘取

# reload（）函数
# 如果一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次，
# 因此，如果你想要重新执行模块里顶层部分的代码，可以用reload()函数，
# 该函数会重新导入之前导入过的模块

# from package_runoob.runoob1 import runoob1
# from package_runoob.runoob2 import runoob2
# runoob1()
# runoob2()

# Python文件I/O
# 打印到屏幕
# print "Python是一个非常棒的语言，不是吗？？"

# 读取键盘输入
# raw_input([prompt]) 函数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）：
# str =raw_input("请输入：");
# print "你输入的内容是：",str

# input函数
# input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回。
# str =input("请输入：")     #[x*5 for x in range(2,10,2)]
# print "你输入的内容是：",str

# 打开和关闭文件
# 你必须先用Python内置的open()函数打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写
# file object =open(file_name[,access_mode][,buffering])
#
# file_name：file_name变量是一个包含了你要访问的文件名称的字符串值。
# access_mode：access_mode决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
# buffering:如果buffering的值被设为0，就不会有寄存。如果buffering的值取1，访问文件时会寄存行。
# 如果将buffering的值设为大于1的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。
fo =open("foo.txt","wb")
print "文件名：",fo.name
print "是否已关闭:",fo.closed
print "访问模式：",fo.mode
print "末尾是否强制加空格：",fo.softspace
fo.close()

# write()方法 可将任何字符串写入一个打开的文件。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。
# fileObject.write(string)

# fo =open("foo.txt","wb")  #以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# fo.write("www.runoob.com! \n good site!\n")
# fo.close()
#
# # read()方法  从一个打开的文件中读取一个字符串。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。
# fo =open("foo.txt","r+") #打开一个文件用于读写。文件指针将会放在文件的开头。
# str =fo.read(10)
# print "读取的字符串是：",str
# fo.close()
#
# # 文件定位
# fo   = open("foo.txt","r+")
# str =fo.read(10)
# print "读取的字符串是：",str
#
# # 查找当前位置
# position =fo.tell()
# print "当前文件位置：",position
#
# # 把指针再次重新定位到文件开头
# position =fo.seek(0,0)
# str =fo.read(10)
# print "重新读取字符串：",str
# # 关闭打开的文件
# fo.close()

# 重命名和删除文件
# Python的os模块提供了执行文件处理操作的方法，比如重命名和删除文件
import  os
# os.rename("foo2.txt","foo2.txt")
# os.remove("foo2.txt")

# Python里的目录：
# 可以使用os模块的mkdir()方法在当前目录下创建新的目录们。你需要提供一个包含了要创建的目录名称的参数。
import os
# os.mkdir("test")

# chdir()方法
# 可以用chdir()方法来改变当前的目录。chdir()方法需要的一个参数是你想设成当前目录的目录名称。
# # 将当前目录改为"/home/newdir"
# os.chdir("/home/newdir")
# getcwd()方法显示当前的工作目录。
# print os.getcwd()

# rmdir()方法删除目录，目录名称以参数传递。
# 在删除这个目录之前，它的所有内容应该先被清除。
# os.rmdir('dirname')

# Python File(文件) 方法
# 2017-11-15 23:04:27
# http://www.runoob.com/python/file-methods.html