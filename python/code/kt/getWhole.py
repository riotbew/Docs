#! /usr/bin/python3
# -*- coding: UTF-8 -*-

import json
import requests

def main():
	data = {
		'name':'365376833@qq.com',
		'password':'18682324080'
	}
	print json.dumps(data)
	# print t_cost(65, 65.18, 400)

def sell_commission(price, much, rate = 0.00025):
	price = type_verify(price)
	much = type_verify(much)
	rate = type_verify(rate)
	return buy_commission(price, much) + price * much * 0.001

def buy_commission(price, much, rate = 0.00025):
	price = type_verify(price)
	much = type_verify(much)
	rate = type_verify(rate)
	_result = price * much * rate
	if _result < 5:
		_result =  5 
	return _result

def t_cost(buy_price, sell_price, much, rate = 0.00025):
	return buy_commission(buy_price, much) + sell_commission(sell_price, much)

def type_verify(data, _type = float):
	try:
		return _type(data)
	except Exception as e:
		print _type.__name__ + '类型转换出错'
		exit(1)

if __name__ == '__main__':
	main()