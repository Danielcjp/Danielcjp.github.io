# 1.写函数：接收n个数字，求这些参数数字的和
def sum(*axiba):
	'''
	返回计数和
	:param axiba:
	:return:
	'''
	result = 0
	for item in axiba:
		result = result + item
		pass
	print('累加和为%d'%result)
	pass
sum(1,2,3)
# 2.写函数：找出传入列表或元组中的奇数位对应的元素，并返回一个新列表
print('-------第一种------')
def process_func1(container):
	'''
	处理列表信息，返回奇数位对应的元素
	:param container:
	:return:
	'''
	return container[::2]

	pass
print(process_func1([1,2,3,4,5,6,7]))

print('-------第二种------')
def process_func2(container):
	'''
	处理列表信息，返回奇数位对应的元素
	:param container:
	:return:
	'''
	list = []
	index = 1
	for i in container:
		if index % 2 == 1:
			list.append(i)
			pass
		index += 1
	return list

	pass
print(process_func2([1,2,3,4,5,6,7,8,9]))


# 3.写函数：检查传入字典的每一个value的长度，如果大于2，那么仅保留前两个长度的内容
# 并将新内容返回给调用者
def length(dict):
	'''
	处理字典类型的数据
	:param dict:
	:return:
	'''
	result = {}
	for key,value in dict.items():
		if len(value) > 2:
			result[key] = value[0:2]		#向字典去添加数据
			pass
		else:
			result[key] = value
			pass
	pass
	return result
diction = {'name':"小白哥",'hobby':["跳舞","画画","唱歌"],'pro':"EIE"}
print(length(diction))


