#! /usr/bin/python
# -*- coding: UTF-8 -*-
# 数据表更新

import config as CONFIG
import utils
import sqlite3
import json

# 初始化sqlite和redis连接器
conn = sqlite3.connect('./test.db')
conn.text_factory = str


#条件筛选
def datafilter(param):
	if param.find('<li><a href="http://finance.ifeng.com/app/hq/stock/')>0 and param.find('</a></li>') >0 and (param.find('sh')>0 or tmp.find('sz')>0) :
		return True
	return False

# 检查当前数据是否有效
def check_stock(code):
	if code[0] == '0':
		code = 'sz'+code
	elif code[0] == '6':
		code = 'sh'+code
	result = request('http://finance.ifeng.com/app/hq/stock/'+code+'/index.shtml')
	if result.find('退市') == -1:
		return False
	else:
		return True

# 将数据保存到sqlite中
def saveInSqlite(name,num,type):
	if name == '发行测试' :
		return;
	row = conn.execute("SELECT count(*) from ASTOCK WHERE CODE == '%s' "%num).next()
	if row[0]:
		row = conn.execute("SELECT name,code from ASTOCK WHERE CODE == '%s' "%num).next()
		if row[0] != name:
			print '更新数据表: '+num 
			conn.execute("UPDATE ASTOCK SET NAME = ? WHERE CODE = ? ",(name, num))
	else :
		result = json.loads(request(CONFIG.CHECK_STOCK+type+num))
		if result['error_code'] !=0 :
			print '无效数据不添加\t',num,'\n'
		else:
			if float(result['result'][0]['dapandata']['nowPic']) == 0 and check_stock(num):
				print '该数据已退市 无效不添加\t',num,'\n'
			else:
				print '插入数据'+num,'\n'
				conn.execute("INSERT INTO ASTOCK (NAME,CODE,AREA) VALUES(?,?,?)",(name,num,type))
	conn.commit()



def request(url):
	return utils.get_data(url)

def update_stock_list():
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
	print '请求列表数据'
	for index in range(0,len(CONFIG.STOCKS_URL)):
		w = open('./data/'+str(CONFIG.STOCKS_URL[index]['name'])+'.txt','w')
		result = request(CONFIG.STOCKS_URL[index]['url'])	
		w.write(result)
		w.close()
	print '更新列表'
	for index in range(0, len(CONFIG.STOCKS_URL)):
		f = open('./data/'+str(CONFIG.STOCKS_URL[index]['name'])+'.txt', 'r')
		tmp = 'init'
		while len(tmp) > 0 :
			tmp = f.readline()
			flag = CONFIG.STOCKS_URL[index]['name']
			if datafilter(tmp):
				saveInSqlite(tmp[tmp.find('">')+2:tmp.find('(')], tmp[tmp.find(flag)+2:tmp.find(flag)+8], flag)

		print '更新'+CONFIG.STOCKS_URL[index]['name']+'成功'
		#删除临时文件
		os.remove('./data/'+str(CONFIG.STOCKS_URL[index]['name'])+'.txt')

update_stock_list()
