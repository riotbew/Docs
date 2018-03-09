#! /usr/bin/python
# -*- coding: UTF-8 -*-

import os
import subprocess
import json
import sys

root_path = os.getcwd()

def test():
	global modules
	f = open('./modules.json','r')
	modules = json.loads(f.read())

	tmp = []
	for key,value in modules['sub'].items():
		keys = key.split('/')
		if len(keys) == 3:
			tmp.append({'key':key,'value':value})
		elif len(keys) == 2:
			tmp.append({'key':key,'value':value})
		elif len(keys) == 1:
			init_sub(value['repo'], keys[0], get_pos(value), root_path)
			pass
	for x in tmp:
		keys = x['key'].split('/')
		if len(keys) == 3:
			init_sub(x['value']['repo'],keys[2],get_pos(x['value']),root_path+'/'+('/').join(keys[:2]))
			pass
		elif len(keys) == 2:
			init_sub(x['value']['repo'],keys[1],get_pos(x['value']),root_path+'/react_native')
			pass

# def init_rn():
def rm_all() :
	global modules
	f = open('./modules.json','r')
	modules = json.loads(f.read())

	def rm_item(repo,name,branch,_cwd=root_path):
		command2 = 'rm -rf '+root_path+'/'+name
		s = subprocess.Popen([command2],shell=True,cwd=_cwd)

	tmp = []
	for key,value in modules['sub'].items():
		keys = key.split('/')
		if len(keys) == 3:
			tmp.append({'key':key,'value':value})
		elif len(keys) == 2:
			tmp.append({'key':key,'value':value})
		elif len(keys) == 1:
			rm_item(value['repo'], keys[0], get_pos(value), root_path)
			pass

def get_pos(value):
	return value.keys().count('tag') == 1 and value['tag'] or value['branch']


def init_sub(repo,name,branch,_cwd=root_path):
	command = 'git clone '+repo+' '+name+' -b '+branch
	command2 = 'rm -rf '+root_path+'/'+name

	s = subprocess.Popen([command],shell=True,cwd=_cwd)
	if name == 'react_native':
		s.wait()

def update_sub(repo,name,branch,_cwd=root_path):
	command = 'git add . && git stash && git checkout '+branch
	s = subprocess.Popen([command],shell=True,cwd=_cwd)
	s.wait()

def update():
	global modules
	f = open('./modules.json','r')
	modules = json.loads(f.read())

	tmp = []
	for key,value in modules['sub'].items():
		keys = key.split('/')
		if len(keys) == 3:
			tmp.append({'key':key,'value':value})
		elif len(keys) == 2:
			tmp.append({'key':key,'value':value})
		elif len(keys) == 1:
			update_sub(value['repo'], keys[0], get_pos(value), root_path+'/'+keys[0])
			pass
	for x in tmp:
		keys = x['key'].split('/')
		if len(keys) == 3:
			update_sub(x['value']['repo'],keys[2],get_pos(x['value']),root_path+'/'+('/').join(keys[:3]))
			pass
		elif len(keys) == 2:
			update_sub(x['value']['repo'],keys[1],get_pos(x['value']),root_path+'/react_native/'+keys[1])
			pass

def main():
	argv = sys.argv
	if len(argv) == 1:
		print 'rm, init, update'
	elif len(argv) == 2:
		if argv[1] == 'rm':
			rm_all()
		elif argv[1] == 'init':
			test()
		elif argv[1] == 'update':
			update()

	# pass

if __name__ == '__main__':
	main()