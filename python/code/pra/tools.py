#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

argv = ''

def test():
	print hex(30),hex(5888)
	print hex(118)
	print hex(205)

def main():

	global argv
	argv = sys.argv

	if len(argv) < 2:
		test()
	elif argv[1] == 'rgb':
		rgbs = argv[2].split(',')
		result = 0;
		for x in range(0,len(rgbs)):
			digit = (len(rgbs)-x-1)*2
			result += int(rgbs[x])*(16**digit)
		print hex(result)



if __name__ == '__main__':
	main()