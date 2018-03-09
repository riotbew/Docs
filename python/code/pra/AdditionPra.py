#! /usr/bin/python
# -*- coding:UTF-8 -*-

# if 基本用法 loop and addition

flag = False
name = 'luren'
if (name == 'python'):
    flag = True
    print('welcome!')
else:
    print(name)

# 例2 if elif


# Loop

# 两种循环 while for 
# 循环控制 break、continue、pass

for letter in 'python':
    if(letter == 'h'):
        pass
        print('这是pass块')
    print ('当前字母：' +letter)

print('end')

#通过序列索引迭代

fruits = ['banana','apple','mango']
for index in range(len(fruits)):
    print('当前水果:'+ fruits[index])
# 上面实例使用了内置函数len()和range()，函数len()返回列表的长度，即元素的个数。range返回一个序列的数。
print('End')
print(len(fruits))
print(range(len(fruits)))

# 循环使用else语句
'''
在python中，for...else：for和其他语言的循环没有什么区别，else语句会在循环正常执行完(即for不是通过break跳出而中断)的情况下执行，while...else也是如此
'''

for num in range(10,20):
    for i in range(2,num):
        if num%i == 0:
            j = num/i
            print('%d 等于 %d * %d'%(num,i,j))
            break
    else:
        print(num,'是一个质数')


