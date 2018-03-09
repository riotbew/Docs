#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Python 运算符

'''
|运算符     |描述                   |   实例                    |
|:----      |:----                  |:-----                     |
|<>         |不等于                 |与!=的作用相同             |
|//         |取整除(取商的整数部分) |9//2 =4, 9.0//2.0 = 4.0    |
|**         |幂运算                 |2**3 = 8                   |
|^          |异或运算               |位运算                     |
|and        |x and y                |a=10,b=20.a and b = 20     |
|or         |x or y                 |a or b = 10                |

'''
a = 10
b = 20

if ( a and b ):
   print "1 - 变量 a 和 b 都为 true"
else:
   print "1 - 变量 a 和 b 有一个不为 true"

if ( a or b ):
   print "2 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
   print "2 - 变量 a 和 b 都不为 true"

# 修改变量 a 的值
a = 0
if ( a and b ):
   print "3 - 变量 a 和 b 都为 true"
else:
   print "3 - 变量 a 和 b 有一个不为 true"

if ( a or b ):
   print "4 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
   print "4 - 变量 a 和 b 都不为 true"

if not( a and b ):
   print "5 - 变量 a 和 b 都为 false，或其中一个变量为 false"
else:
   print "5 - 变量 a 和 b 都为 true"

# Python 成员运算符
'''
|运算符 |描述                                               |实例                               |
|:----  |:------                                            |:-----                             |
|in     |如果在指定的序列中找到值返回True，否则返回False    |x在y序列中，如果x在y序列中返回True |
|not in |如果在指定的序列中没有找到值返回True               |与上面相反                         |
'''
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];

if ( a in list ):
   print "1 - 变量 a 在给定的列表中 list 中"
else:
   print "1 - 变量 a 不在给定的列表中 list 中"

if ( b not in list ):
   print "2 - 变量 b 不在给定的列表中 list 中"
else:
   print "2 - 变量 b 在给定的列表中 list 中"

# 修改变量 a 的值
a = 2
if ( a in list ):
   print "3 - 变量 a 在给定的列表中 list 中"
else:
   print "3 - 变量 a 不在给定的列表中 list 中"


# Python 身份运算符
# 身份运算符用于比较两个对象的存储单元

'''
|运算符 |描述                                       |实例                               |
|:----  |:-----                                     |:----                              |
|is     |is是判断两个标识符是不是引用自同一个对象   |x is y,如果id(x)==id(y) is返回结果1|
|is not |is not是判断两个标识符是不是引用同一个对象 |与上面相反                         |
'''

a = 20
b = 20

if ( a is b ):
   print "1 - a 和 b 有相同的标识"
else:
   print "1 - a 和 b 没有相同的标识"

if ( id(a) == id(b) ):
   print "2 - a 和 b 有相同的标识"
else:
   print "2 - a 和 b 没有相同的标识"

# 修改变量 b 的值
b = 30
if ( id(a) is id(b) ):
   print "3 - a 和 b 有相同的标识"
else:
   print "3 - a 和 b 没有相同的标识"

if ( a is not b ):
   print "4 - a 和 b 没有相同的标识"
else:
   print "4 - a 和 b 有相同的标识"


# Python 运算符优先级
'''
运算符	描述
** 	指数 (最高优先级)
~ + - 	按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % // 	乘，除，取模和取整除
+ - 	加法减法
>> << 	右移，左移运算符
& 	位 'AND'
^ | 	位运算符
<= < > >= 	比较运算符
<> == != 	等于运算符
= %= /= //= -= += *= **= 	赋值运算符
is is not 	身份运算符
in not in 	成员运算符
not or and 	逻辑运算符
'''


