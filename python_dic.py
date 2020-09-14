# 字典：字典是有 键值对 组成的集合，通常使用 键 来访问数据，效率非常高，和list一样，支持对数据的添加、修改、删除
# 特点：
# 		1. 不是序列类型，没有下标的概念，是一个无序的 键值集合，是内置的高级数据类型
# 		2. 用{}来表示字典对象，每个键值对用逗号分隔
# 		3. 键 必须是不可变的类型，【元组、字符串】值可以是任意的类型
# 		4. 每个键必定是唯一的，如果存在重复的键，后者会覆盖前者
dict_A = {}     # 空字典
dict_A = {'pro':'艺术','school':'CUGB'}
dict_A['name'] = 'Emma Watson'         # key:value
dict_A['age'] = 23
dict_A['pos'] = '帅哥'


print(dict_A)               # 输出完整的字典
# print(type(dict_A))
print(len(dict_A))
print(dict_A['name'])       # 通过键获取对应的值
dict_A['name'] = '李沁'     # 修改键对应的值
print(dict_A)

#获取所有的键
print(dict_A.keys())
#获取所有的值
print(dict_A.values())
#获取所有的键值对
print(dict_A.items())
for item in dict_A.items():
    print(item)
    pass
for key,value in dict_A.items():
    print('%s is %s'%(key,value))
    pass

dict_A.update({'height':'170cm'})       # 如果update的键在原字典中有，则直接修改
                                        # 若没有，则在update后，在字典中添加新的键值对
print(dict_A)

#删除操作
del dict_A['name']              #del 和 pop 都可以删除指定项
dict_A.pop('pos')
print(dict_A)
#字典排序 按照key排序
print(sorted(dict_A.items(),key = lambda d:d[0]))
#lambda d:d[0]代表按key排序，d:d[1]代表按value排序
# print(sorted(dict_A.items(),key = lambda d:d[1]))
# lambda 函数可以接收任意多个参数 (包括可选参数) 并且返回单个表达式的值。
# lambda 函数不能包含命令，包含的表达式不能超过一个。

# 共有操作 + * in
stra = '人生苦短'
strb = '我用python'
print(stra + strb)      # 两数据合并+操作适用于string list tuple
print(stra * 2)         # 两数据复制*操作适用于string list tuple

print('python' in strb)     # 查找是否存在某一项并返回布尔类型
# 查找in操作适用于string list tuple dictionary



