#! /usr/bin/python
# -*- coding: UTF-8 -*-

import requests

headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
            "Accept-Encoding":"gzip",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36" }

def get(_url):
	return requests.get(url = _url, headers=headers)
buy = 0
sell = 0
normal = 0

def get_detail(code, p=-1, to_new = False):
	global buy
	global sell
	global normal
	if code.startswith('60')== True:
		_code = 'sh'+code
	else:
		_code = 'sz'+code
	if p == -1:
		p = 0

	detail_url = 'http://stock.gtimg.cn/data/index.php?appn=detail&action=data&c='+_code+'&p='+str(p)
	result = get(detail_url).text
	if len(result) == 0:
		return
	content = result[result.find('"')+1:-2]
	print 'page: '+ str(p)
	for x in content.split('|'):
		item = x.split('/')
		print item[1],'\t',item[2],'\t',item[4],'  \t',item[6],'\t',item[5]
		if item[6] == 'B':
			buy = buy + int(item[4])
		elif item[6] == 'S' :
			sell = sell + int(item[4])
		else :
			normal = normal + int(item[4])

	if to_new == True:
		p = int(result[result.find('[')+1:result.find(',')])+1
		w = open('./data/mxp'+code+'.txt','w')
		w.write(str(p))
		w.close()
		get_detail(code, p=p, to_new=to_new)
		

def main():
	stock = ['600584']
	for x in stock:
		try:
			f = open('./data/mxp'+x+'.txt', 'r')
			_index = int(f.read())
		except Exception as e:
			_index = 0
		get_detail(x, _index, to_new = True)
		print '------'
		print ''
	print 'buy: ','\t',str(buy)
	print 'sell: ','\t',str(sell)
	print 'normal:','\t',str(normal)
	print 'all:','\t',str(buy+sell+normal)
	# result= result[result.find('"')+1:-2]
	# for item in result.split('|'):
	# 	for x in item.split('/'):
	# 		print x
	# 	print(" ")

if __name__ == '__main__':
	main()