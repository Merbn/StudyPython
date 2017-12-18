# -*- coding: UTF-8 -*-
# Python 练习实例1
# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j)and(i!=k)and(j!=k):
                print i,j,k
#原答案没有指出三位数的数量，添加无重复三位数的数量
d=[]
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if (a!=b) and (a!=c) and (c!=b):
                d.append([a,b,c])
print "总数量：", len(d)
print d
#将for循环和if语句综合成一句，直接打印出结果
list_num =[1,2,3,4]
list =[i*100+j*10+k for i in list_num for j in list_num for k in list_num if(j!=i)and (i!=k)and (j!=k)]
print list

from itertools import permutations
for i in permutations([1,2,3,4],3):
    print i


for i in permutations([1,2,3,4],3):
    k =''
    for j in range(0,len(i)):
        k =k+str(i[j])
    print (int(k))

[(x,y,z) for x in range(1,5) for y in range(1,5) for z in range(1,5) if(x!=y)and(x!=z)and(y!=z)]
 