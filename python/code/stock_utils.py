#! /usr/bin/python
# -*- coding: UTF-8 -*-
import sqlite3
import json
import utils
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 聚合数据股票列表
JH_STOCKS_URL = [
	"http://web.juhe.cn:8080/finance/stock/szall?key=7535581f3ef2dc147c812a62800f49cb&type=4&page=",
	"http://web.juhe.cn:8080/finance/stock/shall?key=7535581f3ef2dc147c812a62800f49cb&type=4&page="
];

URL_DETAIL = "http://hqdigi2.eastmoney.com/EM_Quote2010NumericApplication/CompatiblePage.aspx?Type=OB&Reference=json&limit=0"

# 初始化sqlite
conn = sqlite3.connect('./test.db')
conn.text_factory = str

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
					AREA varchar(4),
					ABB	 varchar(15)
				)''')
		except Exception as e:
			pass

def update_stock_list():
	from xpinyin import Pinyin
	p = Pinyin()
	init_db()
	print '开始更新数据'
	for x in range(0, len(JH_STOCKS_URL)):
		index = 1
		def _insert_data(data):
			num = data['code']
			type = data['symbol'][:2]
			name = data['name']
			pin = p.get_initials(name)
			if pin[0] == '*':
				pin = pin[2:]			
			abb = ''.join(pin.split('-'))
			abb = abb.replace(' ', '')
			# 剔除B股品种
			if num[:3] == '900' or num[:3] == '200':
				return 
			row = conn.execute("SELECT count(*) from ASTOCK WHERE CODE == '%s' "%num).next()
			if row[0]:
				row = conn.execute("SELECT name,code from ASTOCK WHERE CODE == '%s' "%num).next()
				if row[0] != name:
					print '更新数据表: ',num 
					conn.execute("UPDATE ASTOCK SET NAME = ?,ABB=? WHERE CODE = ? ",(name, abb, num))
			else :
				print '插入数据 ',num,'\n'
				conn.execute("INSERT INTO ASTOCK (NAME,CODE,AREA,ABB) VALUES(?,?,?,?)",(name,num,type,abb))
			conn.commit()

		while True:
			res = json.loads(request(JH_STOCKS_URL[x]+str(index)))
			index += 1
			if res['error_code'] == 0:
				res = res['result']['data']
				for _index in range(0,len(res)):
					_insert_data(res[_index])
			else:
				print 'end'
				break;
	print '完成数据表更新'

def get_stock_list():
	stock_list = conn.execute('SELECT NAME, CODE, AREA, ABB FROM ASTOCK')
	return stock_list.fetchall()

def search_stock(abb='-1'):
	stocks = get_stock_list()
	abb = abb.upper()
	result = []
	for x in stocks:
		if x[3].find(abb) != -1:
			result.append(x)
	if len(result) == 0:
		return False
	else:
		return result

def test():
	update_stock_list()

import time
#将固定格式时间转成时间戳
def time_format(data, format):
	return time.mktime(time.strptime(data,format))


def MA(data,length=5):
	result = []
	_len = len(data)
	_sum = 0
	print data
	if _len > length:
		_sum = sum(data[-length::])
	result.append(fdiv(_sum,length))
	if _sum == 0:
		return [0 for x in data]
	for i in range(length,_len)[::-1]:
		_sum -= data[i]
		_sum += data[i-length]
		result.append(fdiv(_sum,length))
	for i in range(1,length)[::-1]:
		_sum -= data[i]
		result.append(fdiv(_sum,i))
	return result[::-1]

def fdiv(a,b,digit=3):
	return round(a/b,digit)

def get_day_data_rv(code):
	day_data = json.loads(utils.get(code))
	day_data.reverse()
	return day_data

def printLastData(code,length = 10):
	print code
	if length == None:
		length = 10
	data = get_day_data_rv(code)
	length = length > len(data) and len(data) or length
	for x in range(0, length):
		item = data[x]
		_flag = ''
		if float(item[7]) > 0:
			_flag = '+'
		print item[0],'\t',item[3],'\t',str(_flag+str(round(float(item[7]),1))+'%'),'\t',str(_flag+str(float(item[6])))
	print ''

def get_detail_new(code='601011'):
	if code[2:] == '60':
		code += '1'
	else:
		code += '2'

	# 初始数据处理
	_page = utils.get(code+'_page')
	if _page == None:
		_page = 1
		utils.set(code+'_page', _page)
	# 请求数据
	url = URL_DETAIL + '&stk='+code + '&page=' +str(_page)
	result = request(url)
	_index = int(result[result.find(':')+1:result.find(',')])
	# 页码处理
	if _index > int(_page):
		_page = _index
		utils.set(code+'_page', _page)
		url = URL_DETAIL + '&stk='+code + '&page=' +str(_page)
		result = request(url)
	# 数据处理
	result = result[result.find('[')+1:result.find(']')].split('",')
	_pack_data = []
	for item in result:
		item = item[1:].split(',')
		_pack_data.append(item)
	for item in _pack_data:
		print item

def search_stock(name):
	name = name.upper()
	result = []
	stocks = get_stock_list()
	for item in stocks:
		if item[3].find(name) != -1:
			result.append(item)
	for item in result:
		print item[1],item[0]
	else:
		print 'can not find'

def main():
	argv = sys.argv
	if len(argv) < 2:
		test()
		return
	if argv[1] == 'update':
		update_stock_list()
	elif argv[1] == 'search' and len(argv)>2:
		search_stock(argv[2])
	else:
		test()


if __name__ == '__main__':
	main()
