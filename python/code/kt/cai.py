#! /usr/bin/python
# -*- coding: UTF-8 -*-

import json
import requests
import time
import hashlib

_headers = {
	'Accept':'*/*',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.9',
	'authorization':'Bearer undefined',
	'Connection':'keep-alive',
	'Host':'www.cailianpress.com',
	'Referer':'https://www.cailianpress.com/',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}

def main():
	# print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()-10000000))
	_time = time.time()-100000
	print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(_time))
	last_time =  int(time.time())
	# last_time = int(time.time())
	getMsg(last_time)

def pollNewMsg():
	response = requests.get('https://www.cailianpress.com/nodeapi/roll/get_update_roll_list?last_time=1515045950&refresh_type=0&rn=20&sign=664206d4ec81f12c5cf441353a0501d4', headers=_headers)
	print json.dumps(response.json())

end_time = time.time()
def getMsg(_time):
	global end_time
	content = 'last_time='+str(_time)+'&refresh_type=1&rn=20'
	sign = hashlib.md5(hashlib.sha1('last_time='+str(_time)+'&refresh_type=1&rn=20').hexdigest())
	sign = sign.hexdigest()
	_url = 'https://www.cailianpress.com/nodeapi/telegraphs?'+content+'&sign='+sign
	response = requests.get(_url, headers = _headers)
	result = response.json()
	content = result['data']['roll_data']
	for item in content:
		print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item['sort_score']))
		print item['content']
		
	if len(content) != 0 and end_time != content[len(content)-1]['sort_score']:
		end_time = content[len(content)-1]['sort_score']
		getMsg(content[len(content)-1]['sort_score'])

if __name__ == '__main__':
	main()