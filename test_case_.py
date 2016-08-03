# coding=utf-8
import os
# 列出某个文件夹下的所有 case,这里用的是 python，
# 所在 py 文件运行一次后会生成一个 pyc的副本

caselist = os.listdir('D:\\py\\test\\test_case')
for a in caselist:
	s=a.split('.')[1]
	if s=='py':
		os.system('D:\\py\\test\\test_case\\%s 1>>log.txt 2>&1'%a)