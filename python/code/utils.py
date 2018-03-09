#! /usr/bin/python
# -*- coding: UTF-8 -*-
# 网络请求封装

import urllib2
import json

BASE = './data/'

def get_data(url):
	req= urllib2.Request(url) 
	response = urllib2.urlopen(url)
	result = response.read()
	return result

def get_config(config, name='./config.json'):
	f = open(name,'r')
	res = json.loads(f.read())
	return res[config]

def save_config(config, data, name='./config.json'):
	f = open(name,'r')
	res = json.loads(f.read())
	if data == None:
		try:
			res.pop(config)
		except Exception as e:
			pass
	else:
		res[config] = data
		f.close()
	w = open(name, 'w')
	w.write(json.dumps(res))


def get(key):
	try:
		f = open(BASE+key+'.txt','r')
		result = f.read()
		f.close()
	except Exception as e:
		result = None
	finally:
		return result
	
def set(key,value):
	try:
		w = open(BASE+key+'.txt', 'w')
		w.write(str(value))
		w.close
	except Exception as e:
		print e


def init():
	import subprocess
	try:
		import redis
		r = redis.StrictRedis(host='localhost', port=6379, db=0)
		r.get('index')
		global get,set
		get = r.get
		set = r.set
	except Exception as e:
		print 'utils init err: ',e
		if e.message.find('Connection refused') != -1:
			command = '/Users/Tauren/Documents/tool/redis-3.2.6/src/redis-server'
			s = subprocess.Popen([command],shell=True)

init()

def main():
	
	pass

if __name__ == '__main__':
	main()
