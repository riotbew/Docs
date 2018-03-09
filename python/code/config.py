#! /usr/bin/python
# -*- coding: UTF-8 -*-

#API接口
API_LIST = (
	"http://api.finance.ifeng.com/akmin?type=5&scode=",							#15分钟数据			0
	"http://api.finance.ifeng.com/akmin?type=30&scode=",							#30分钟数据			1
	"http://api.finance.ifeng.com/akmin?type=60&scode=",							#60分钟数据			2
	"http://api.finance.ifeng.com/akdaily?type=last&code=",						#日线数据				3
	"http://api.finance.ifeng.com/akweekly?type=last&code=",						#周线数据				4
	"http://api.finance.ifeng.com/akmonthly?type=last&code=",						#月线数据				5
	"http://api.finance.ifeng.com/ayear/?code=",									#年线数据				6
	"http://api.finance.ifeng.com/aminhis/?type=five&code=",						#最新五日分时数据		7
	"http://api.finance.ifeng.com/akmin?type=5&scode=",							#15分钟数据			0
	'http://app.finance.ifeng.com/data/stock/tab_zjlx.php?code='				#资金流向
)
URL_CHECK_STOCK = 'https://hq.finance.ifeng.com/q.php?l='
#A股列表数据列表 0：sz 1:sh
STOCKS_URL = (
	{'name':'sz','url':"http://app.finance.ifeng.com/hq/list.php?type=stock_a&class=sa"},
	{'name':'sh','url':"http://app.finance.ifeng.com/hq/list.php?type=stock_a&class=ha"},)
CHECK_STOCK = 'http://web.juhe.cn:8080/finance/stock/hs?key=7535581f3ef2dc147c812a62800f49cb&gid='

# 聚合数据股票列表
JH_STOCKS_URL = [
	"http://web.juhe.cn:8080/finance/stock/szall?key=7535581f3ef2dc147c812a62800f49cb&type=4&page=",
	"http://web.juhe.cn:8080/finance/stock/shall?key=7535581f3ef2dc147c812a62800f49cb&type=4&page="
];

# ths 数据源
THS_URL = [
	{'url':'http://www.iwencai.com/diag/block-detail?pid=10331&codes=002340','des':'压力位分析'},
	{'url':'http://www.iwencai.com/diag/block-detail?pid=11665&codes=002340','des':'重要新闻'},
	{'url':'http://www.iwencai.com/diag/block-detail?pid=10735&codes=002340','des':'财务指标'},
	{'url':'http://www.iwencai.com/diag/block-detail?pid=8043&codes=002340','des':'常用指标'},
	{'url':'http://www.iwencai.com/diag/block-detail?pid=10751&codes=002340','des':'近期重要事件'},
	{'url':'http://www.iwencai.com/diag/block-detail?pid=8153&codes=002340','des':'基本概况'},
]

# 下面包导入挺耗时间
# import matplotlib
# from numpy.random import randn
# import matplotlib.pyplot as plt
# from matplotlib.ticker import FuncFormatter
 
# def to_percent(y, position):
#     # Ignore the passed in position. This has the effect of scaling the default
#     # tick locations.
#     s = str(100 * y)
 
#     # The percent symbol needs escaping in latex
#     if matplotlib.rcParams['text.usetex'] == True:
#         return s + r'$\%$'
#     else:
#         return s + '%'
 

# if __name__ == '__main__':
	
# 	x = randn(5000)
	 
# 	# Make a normed histogram. It'll be multiplied by 100 later.
# 	plt.hist(x, bins=50, normed=True)
	 
# 	# Create the formatter using the function to_percent. This multiplies all the
# 	# default labels by 100, making them all percentages
# 	formatter = FuncFormatter(to_percent)
	 
# 	# Set the formatter
# 	plt.gca().yaxis.set_major_formatter(formatter)
	 
# 	plt.show()
