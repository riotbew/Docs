#! /usr/bin/env  python
# -*- coding: UTF-8 -*-

import sys

colors = sys.argv
argvLen = len(colors)
obj = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']

def cal (var):
	tmp = int(var)/16
	if tmp > 0:
		return str(cal(tmp))+str(obj[int(var)%16])
	else :
		return obj[int(var)];


for x in range(1,argvLen):
	print (cal(colors[x]))

nextInput = input()
print (str(nextInput))
