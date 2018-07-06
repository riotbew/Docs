#! /usr/bin/python
# -*- coding: UTF-8 -*-

import json
import requests
import math
import os
import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

root_path = os.getcwd()

headers = { "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
			"ktversion": "1.4.3",
			"Connection": "keep-alive",
			"ktproductid": "81",
			"Accept": "*/*",
			"User-Agent": "jiao yi shi/1.4.3 (iPhone; iOS 10.3.3; Scale/2.00)",
			"Accept-Language": "zh-Hans-CN;q=1, en-CN;q=0.9"}

token = 'token=244ce6fed3844f76b844e02643cd79b2';
f=open('./data/token.txt')
token = f.read()
url_only = 'http://message.ktkt.com/message/history/only';
url_history = 'http://message.ktkt.com/message/history';
post_data = 'origin=mobile&rid=1394202292180208&rtype=vip&teacher_id=1394202292180202&';
teacher_id = '1078328366' # uid
history_file_name = '/history.json'
history_file_dir = './data/'+str(time.strftime("%Y%m%d", time.localtime()))
TIPS = '''用户信息数据有问题，请重新填写
格式如下：
{
    "name":"user_name",
    "password":"user_pwd"
}'''

def get(_url):
	return requests.get(url = _url, headers=headers)

def post(_url, data, _headers = headers):
	headers['Content-Length'] = str(len(data))
	res = requests.post(_url, data=data, headers=_headers)
	result = res.json()
	if result.has_key('code') and result['code'] == 204119:
		login()
	return res
		

def update_history():
	update_pre(True)
	update_all()

count = 2
history_all = []

def update_pre(isUpdate=False):
	global history_all
	if os.path.exists(history_file_dir) == False:
		os.mkdir(history_file_dir)
	if os.path.exists(history_file_dir+history_file_name):
		try:
			history_file = open(history_file_dir+history_file_name)
			result = history_file.read()
			history_all = json.loads(result)
		except Exception as e:
			history_all = []
	if isUpdate:
		history_all = history_all[:len(history_all)/30*30]

def update_all():
	global count,history_all
	x = len(history_all)/30+1

	while True:
		result = post(url_history,post_data+token+'&page='+str(x)).text
		result = json.loads(result)
		print(result['info'])

		count = math.ceil(result['data']['count']/30.0)
		history_all = history_all + result['data']['list']
		print str(int(math.floor((x/count)*100)))+'%'
		if x >= count:
			break
		x += 1

	f = open(history_file_dir+history_file_name, 'w')
	f.write(json.dumps(history_all))

def main():
	login()
	if isLogin() == False:
		login()
	saveToFile()
	saveToFile(False)
	# update_history()
	# printOnly()
	# printOnly(True)

def isLogin():
	data = post_data+token+'&page=1'
	headers['Content-Length'] = str(len(data))
	res = requests.post(url_history, data=data, headers=headers)
	result = res.json()
	if result.has_key('code') and result['code'] == 204119:
		print result['info']
		return False
	else:
		return True
	

def login():
	global token
	user_info = open('./config/user_info.json').read()
	try:
		user_info = json.loads(user_info)
	except Exception as e:
		print(TIPS)
	_headers = {
		'Authorization': 'Bearer 9fc5d694943be1a757e350d486917e5e#Thu, 04 Jan 2018 10:07:22 GMT#dxapp',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Connection': 'Keep-Alive',
		'Accept-Encoding': 'gzip',
		'User-Agent': 'okhttp/3.9.1',
	}
	_url = 'http://mapi.ktkt.com/user/v1/signin'
	_data = 'origin=mobile&name='+user_info['name']+'&password='+user_info['password'];
	response = post(_url, _data, _headers)
	result = response.json()
	if result.has_key('token') == False:
		print result['message']
		exit(0)
	token = 'token='+result['token']['token']
	w = open('./data/token.txt','w')
	w.write('token='+result['token']['token'])
	w.close()	

def msgToStr(item):
	res = item['created_at']+'\n'
	if item['message_type'] == 'normal':
		if item['image_urls'] == '':
			res += item['username']+'\t'+item['content']+'\n'
		else:
			res += item['username']+'\t'+item['image_urls']+'\n'
	else:
		question_data = json.loads(item['content'])
		msg = question_data['q_message']
		res += 'Q --- '+msg['username']+':\t'+msg['content']+'\n'
		msg = question_data['a_message']
		res += 'A --- '+msg['username']+':\t'+msg['content']+'\n'
	res += '\n'
	return res

def saveToFile(onlyTeacher=True) :
	update_history()
	global history_all
	if onlyTeacher:
		name = history_file_dir+'/AOnly.txt'
	else:
		name = history_file_dir+'/AAll.txt'

	f = open(name,'w')

	if onlyTeacher:
		for x in history_all:
			if str(x['uid']) == teacher_id:
				f.write(msgToStr(x))
	else:
		for x in history_all:
			f.write(msgToStr(x))
			

def printOnly(printAll=False):
	global history_all
	update_pre()

	if printAll:
		for x in history_all:
			print msgToStr(x)
	else:
		for x in history_all:
			if str(x['uid']) == teacher_id:
				print msgToStr(x)


if __name__ == '__main__':
	main()