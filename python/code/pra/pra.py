#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 时间API练习 
# import time

# print time.localtime(time.time())
# print time.asctime(time.localtime(time.time()))

# print time.strptime('2016-11-28', '%Y-%m-%d')     #将时间字符串转化为时间元组

# print time.mktime(time.strptime('2016-11-28', '%Y-%m-%d'))    #接受一个时间元组转化为时间戳
# print time.localtime(time.mktime(time.strptime('2016-11-28', '%Y-%m-%d')))    #接受时间戳返回当下时间元组

# print time.strftime('%Y-%m-%d', time.localtime(time.mktime(time.strptime('2016-11-28', '%Y-%m-%d')))) #接受时间元组 返回格式化日期


s = set([name.lower() for name in ['Adam', 'Lisa', 'Bart', 'Paul']])
s = [name.lower() for name in ['Adam', 'Lisa', 'Bart', 'Paul']]
#print (s)

s = set(['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun','Jul','Aug','September','October','November','December'])

s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
# for value in s:
#     print (value)

def sum(list):
    result=0
    for value in list:
        result += value
    return result

input = []
for x in range(1,101):
    input.append(x**2)
print (sum(input))

def square_of_sum(L):
    result=0
    for value in L:
        result += value**2
    return result

print square_of_sum([1, 2, 3, 4, 5])
print square_of_sum([-5, 0, 5, 15, 25])

import math

def quadratic_equation(a, b, c):
    root = b**2 - 4*a*c
    if root > 0:
        return (-b+math.sqrt(root))/(2*a),(-b-math.sqrt(root))/(2*a)
    else :
        return

print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)

# 汉诺塔算法 move(n, a, b, c)表示的是有n个盘子在a柱子上，将要移到c柱子上面去
def move(n, a, b, c):
# 如果a柱子上面只有一个盘子，则直接移到c柱子上面去并输出路径，结束递归
    if n == 1:
        print a, '-->', c
        return
# 表示的是将n-1的盘子从a柱子上面移到b柱子上面去
    move(n-1, a, c, b)
# 输出最下面个盘子移从a移到c的路径
    print a, '-->', c
# 将b柱子上面的n-1个盘子移动到c柱子上面
    move(n-1, b, a, c)

move(2, 'A', 'B', 'C')

# 利用倒序切片对 1 - 100 的数列取出：
L = range(1,101)

print L[-10:]       #最后10个数
print L[-46::5]     #最后10个5的倍数。

# for value in range(1,101):
#     if value%7==0:
#         print value
#
# L = range(1, 100)[6::7]
# for value in L:
#     print value

# L = ['Adam', 'Lisa', 'Bart', 'Paul']
# for t in enumerate(L):
#     index = t[0]
#     name = t[1]
#     print index, '-', name

# L = ['Adam', 'Lisa', 'Bart', 'Paul']
# for index, name in zip(range(1, len(L)+1), L):
#     print index, '-', name

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for k, v in d.items():
    sum = sum + v
    print k,':',v
print 'average', ':', sum/len(d)


d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
tds = [generate_tr(name, score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'

def toUppers(L):
    return [x.upper() for x in L if isinstance(x,str)]

print toUppers(['Hello', 'world', 101])

print [x**2 for x in range(1,6)]

#利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。

print [ 100*x+10*y+x for x in range(1,10) for y in range(10) for z in range(10) if x == z]

def format_name(s):
    s = s.lower()
    return s[:1].upper()+s[1:]

print map(format_name, ['adam', 'LISA', 'barT'])

def f(x, y):
    return x + y

print reduce(f, [1, 3, 5, 7, 9], 100)

def prod(x, y):
    return x*y

print reduce(prod, [2, 4, 5, 7, 12])

import math

def is_sqr(x):
    return math.sqrt(x)%1 == 0

print filter(is_sqr, range(1,101))

# 排序函数
# 输入：['bob', 'about', 'Zoo', 'Credit']
# 输出：['about', 'bob', 'Credit', 'Zoo']
def cmp_ignore_case(s1, s2):
    return cmp(s1.lower(),s2.lower())

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

# 请编写一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积。
def calc_prod(lst):
    def result():
        return reduce(lambda x,y:x*y,lst)
    return result

f = calc_prod([1, 2, 3, 4])
print f()


# 希望一次返回3个函数，分别计算1x1,2x2,3x3:
def count():
    fs = []
    for i in range(1, 4):
        def f(x):
            return lambda : x**2
        fs.append(f(i))
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()

def new_f(func):
    def fn(x):
        print 'call ',func.__name__,'(',x,')'
        return func(x)
    return fn

@new_f
def f(x):
    return x**2

f(2)

import time

def performance(f):
    def fn(x):
        begin = time.time()
        result = f(x)
        end = time.time()
        print 'call ',f.__name__,'() ','in ',(end-begin)
        return result
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)


print time.strftime('%Y-%m-%d',time.localtime(time.time()))

#带参装饰器的例子
import time
import functools

def performance(unit):
    def performance_decorator(f):
        @functools.wraps(f)
        def wrap(*args, **kw):
            begin = time.time()
            res = f(*args,**kw)
            end = time.time()
            if unit == 'ms':
                print 'call '+f.__name__+'()',(end-begin)
            elif unit == 's':
                print 'call '+f.__name__+'()',(end-begin)/1000
            return res
        return wrap
    return performance_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial.__name__

print factorial(10)

L = ['bob', 'about', 'Zoo', 'Credit']
# 排序 偏函数重写
import functools

sorted_ignore_case = functools.partial(sorted, cmp = lambda x,y : cmp(x.lower(),y.lower()))

print sorted_ignore_case(L)

test = functools.partial(sorted,key=str.lower)
print test(L)

import functools

sorted_ignore_case = functools.partial(sorted,key=str.lower)

print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])

print sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower)

try:
    import json
except ImportError:
    import simplejson as json

print json.dumps({'python':2.7})

class Person(object):
    pass

p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
# L2 = sorted(L1, cmp = lambda x,y:cmp(x.name.lower(),y.name.lower()))
L2 = sorted(L1, key = lambda x:x.name)

print L2[0].name
print L2[1].name
print L2[2].name

class Person(object):
    def __init__(self,name,gender,birth,**kw):
        self.name = name
        self.gender = gender
        self.birth = birth
        self.__dict__.update(kw)

# 第二种做法
# class Person(object):
#     def __init__(self, name, gender, birth, **kw):
#         self.name = name
#         self.gender = gender
#         self.birth = birth
#         for k, v in kw.iteritems():
#             setattr(self, k, v)

xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')

print xiaoming.name
print xiaoming.job

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

p = Person('Bob', 59)

print p.name
# print p.__score

class Person(object):
    count = 0
    def __init__(self,name):
        self.name=name
        Person.count += 1

p1 = Person('Bob')
print Person.count

p2 = Person('Alice')
print Person.count

p3 = Person('Tim')
print Person.count

#python中类属性和实例属性
class Person(object):

    __count = 0

    def __init__(self, name):
        self.name = name
        Person.__count += 1
        print Person.__count

p1 = Person('Bob')
p2 = Person('Alice')

try:
    print Person.__count
except AttributeError:
    print AttributeError.__name__
#    print 'attributeerror'



class Person(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B-及格'
        else :
            return 'C-不及格'

p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print p1.get_grade()
print p2.get_grade()
print p3.get_grade()


class Person(object):
    count = 0
    @classmethod
    def how_many(cls):
        return cls.count
    def __init__(self, name):
        self.name = name
        Person.count = Person.count + 1

print Person.how_many()
p1 = Person('Bob')
print Person.how_many()


#继承
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    """docstring for Student"""
    def __init__(self, name, gender, school, score):
        super(Student, self).__init__(name, gender)
        self.school = school
        self.score = score

#更新类的属性
class Person(object):

    def __init__(self, name, gender, **kw):
        self.name = name
        self.gender = gender
        ##self.__dict__.update(kw)
        for k,v in kw.items():
            setattr(self,k,v)

p = Person('Bob', 'Male', age=18, course='Python')
print p.age
print p.course

#property的用法
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score

s = Student('Bob', 59)
s.score = 78
print s.score

