#! /usr/bin/python
# -*- coding: UTF-8 -*-
# 数据表更新

import json
import time
import sqlite3
import random
import utils
import math
import os
import config as CONFIG
import sys
import threading

reload(sys)
sys.setdefaultencoding('utf-8')

# 初始化sqlite
conn = sqlite3.connect('./test.db')
conn.text_factory = str

def req_data(code):
	return utils.get_data(CONFIG.API_LIST[3]+str(code))

def request(url):
	return utils.get_data(url)

def init_db():
	print '初始化sqlite数据库'
	try:
		cursor = conn.execute("select * from ASTOCK")
		row = cursor.next()
	except Exception as e:
		try:
			conn.execute('''
				CREATE TABLE ASTOCK (
					ID integer PRIMARY KEY AUTOINCREMENT NOT NULL,
					NAME text NOT NULL,
					CODE varchar(6) NOT NULL,
					AREA varchar(4)
				)''')
		except Exception as e:
			pass

def get_stock_list():
	stock_list = conn.execute('SELECT NAME, CODE, AREA FROM ASTOCK')
	return stock_list.fetchall()

def delay(_time,_wait_time = 10):
	cur_time = time.time()
	if time.time()-_time>30:
		_time = cur_time
		wait = round(random.uniform(0,1),1)*_wait_time
		print '等待时间\t',wait,'\n'
		time.sleep(wait)
	print ''
	return _time

def get_day_data_rv(code):
	day_data = json.loads(utils.get(code))
	day_data.reverse()
	return day_data

up_x_data = []
def ma_nearby_x(code,index=0, x=24):
	day_data = get_day_data_rv(code)
	# return
	# print day_data
	sum=0;
	if len(day_data)<(x*2+index):
		return False
	for x in range(index,x+index):
		sum+=float(day_data[x][3])
		print day_data[x]
	print sum
	print x
	print sum/(x+1)
	return 
	newest_data = day_data[index][1:5]
	point = float(newest_data[2])
	point_x = sum/x
	if code[0] == '0' or code[0] == '3':
		_code = 'sz'+code
	else:
		_code = 'sh'+code
	res = utils.get_data(CONFIG.URL_CHECK_STOCK+_code)
	res = json.loads(res[23:len(res)-4])
	if float(res[0]) == 0:
		return False
	if (point-point_x)/point_x < 0.05:
		up_x_data.append([point_x,point,(point-point_x)/point_x,code])
		return True
	return False

def get_data_to_redis():
	index = int(utils.get('index'))
	if len(get_stock_list())-index<50:
		utils.set('index',0)
	stocks = get_stock_list()
	start_time = time.time()
	print index 
	try:
		if int(index) == len(stocks)-1:
			index = 0
			utils.set('index',0)
	except Exception as e:
		index = 0
		utils.set('index',0)
	
	_index = 0
	for x in range(int(index),len(stocks)):
		item = stocks[x]

		t = MYThread(target=save_stock_data, args=(item,x,), callback=CallBack)
		t.setDaemon(False)
		threads.append(t)


	while len(threadings.keys())<50:
		item = threads.pop(0)
		threadings[item.getName()] = item
		# start_time = delay(start_time)
	for v in threadings.values():
		v.start()

def save_stock_data(item,x):
	mutex.acquire()
	req = json.loads(req_data(item[2]+item[1]))
	result = req['record']
	utils.set(item[1], json.dumps(result))
	utils.set('index',x)
	print '收集',item[1],'完毕'
	mutex.release()


def update_stock_list():
	init_db()
	print '开始更新数据'
	for x in range(0, len(CONFIG.JH_STOCKS_URL)):
		index = 1
		def _insert_data(data):
			num = data['code']
			type = data['symbol'][:2]
			name = data['name']
			# 剔除B股品种
			if num[:3] == '900' or num[:3] == '200':
				return 
			row = conn.execute("SELECT count(*) from ASTOCK WHERE CODE == '%s' "%num).next()
			if row[0]:
				row = conn.execute("SELECT name,code from ASTOCK WHERE CODE == '%s' "%num).next()
				if row[0] != name:
					print '更新数据表: ',num 
					conn.execute("UPDATE ASTOCK SET NAME = ? WHERE CODE = ? ",(name, num))
			else :
				print '插入数据 ',num,'\n'
				conn.execute("INSERT INTO ASTOCK (NAME,CODE,AREA) VALUES(?,?,?)",(name,num,type))
			conn.commit()

		while True:
			res = json.loads(request(CONFIG.JH_STOCKS_URL[x]+str(index)))
			index += 1
			if res['error_code'] == 0:
				res = res['result']['data']
				for _index in range(0,len(res)):
					_insert_data(res[_index])
			else:
				print 'end'
				break;
	print '完成数据表更新'

def printLastData(code,length = 10):
	print code
	if length == None:
		length = 10
	data = get_day_data_rv(code)
	for x in range(0,length>len(data)and len(data) or length):
		item = data[x]
		print item[0],'\t',item[3],'\t',str(item[14]+'%'),'\t',str(float(item[6]))+'%'
	print ''

#自定义多线程管理类，支持callback回调 TODO 完成封装、线程管理
threads = []
threadings = {}
mutex = threading.Lock()
class MYThread(threading.Thread):
	def __init__(self, name=None, target=None,args=(),callback=None):
		super(MYThread, self).__init__(name=name,)
		self.__target = target
		self.__args = args
		self.__callback=callback

	def run(self):
		if self.__target!=None:
			if self.__callback !=None:
				self.__callback(self.name,self.__target(*self.__args))
			else:
				self.__target(*self.__args)			

def CallBack(name, result):
	# print 'current threads: ',len(threadings.keys())
	mutex.acquire()
	del threadings[name]
	addThreads()
	mutex.release()
	# threadings
def addThreads(): 
	if len(threads)>0:
		item = threads.pop(0)
		item.start()
		threadings[item.getName()] = item
	else:
		print len(threadings.keys())
		if len(threadings.keys()) == 1:
			f = open('tmp.txt', 'w')
			f.write(json.dumps(_count_list))
		return

#测试函数，用于测试功能
cal_flag = 'abs'
def cal_data(x):
	item = json.loads(utils.get(x[1]))
	item.reverse()
	_length = 3
	if len(item) < _length :
		_length = len(item)
	_sum = 0
	def func(_x):
		return float(_x)		
	_cal_value = func
	if cal_flag == 'abs':
		_cal_value = lambda __x : abs(func(__x))
	for y in range(0,_length):
		sub_item = item[y]
		# _sum += float(sub_item[7])
		# abs(float(sub_item[7]))
		_sum += _cal_value(sub_item[7]) 
	mutex.acquire()
	print 'finsh',x[1]
	_count_list.append({'code':x[1],'value':_sum, 'len':len(item)})
	# print 'finsh ',x[1]
	mutex.release()

_count_list = []
test_flag = 1
def test():
	# stocks = get_stock_list()
	# for x in stocks:
	# 	item = get_avg_price_rate(x[1],4,1)
	# 	if item['len'] > 15:
	# 		_count_list.append(item)
	# f = open('tmp.txt', 'w')
	# f.write(json.dumps(_count_list))
	stocks = get_stock_list()
	item = stocks[0]
	print req_data(item[2]+item[1])

	return 

	if test_flag ==0:
		f = open('tmp.txt', 'r')
		result = json.loads(f.read())
		result = sorted(result, key=lambda i : i['value'])

		for x in result:
			if x['len'] > 40:
				print x['code'],'\t',x['value'],'\t',x['len']
	else:
		stocks = get_stock_list()
		for x in stocks:
			t = MYThread(target=cal_data, args=(x,), callback=CallBack)
			t.setDaemon(False)
			threads.append(t)

		while len(threadings.keys())<1000:
			item = threads.pop(0)
			threadings[item.getName()] = item
		for v in threadings.values():
			v.start()

def get_avg_price_rate(code='000001',length=20, flag=0):
	result = json.loads(utils.get(code))
	result.reverse()
	_sum = 0
	if len(result) < length:
		length = len(result)
	for x in range(0,length):
		item = result[x]
		if flag == 0:
			_sum += abs(float(item[7]))
		else:
			_sum += float(item[7])
	# print code,'\t',_sum/length
	return {'code':code, 'value':round(_sum/length,2),'len':len(result)}

def main():
	start = time.time()
	
	argv = sys.argv

	if len(argv) < 2:
		test()
		return 
	# 更新数据
	if argv[1] == 'update':
		if len(argv) > 2 and argv[2] == 'list':
			update_stock_list()
		else:
			get_data_to_redis()
	# 重置数据更新的位置
	elif argv[1] == 'reset':
		utils.set('index',0)
	elif argv[1] == 'day':
		if len(argv) > 2 :
			printLastData(argv[2],int(argv[3]))
	elif argv[1] == 'ap':
		if len(argv) == 5:
			get_avg_price_rate(argv[2],argv[3],argv[4])
		elif len(argv) ==4 :
			get_avg_price_rate(argv[2],length=argv[3])
		elif len(argv) ==3 :
			get_avg_price_rate(code=argv[2])
	else:
		test()

	print '耗时： ' + str(time.time() - start)

if __name__ == '__main__':
	main()
