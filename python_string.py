# 序列：在python中，序列就是一组按照顺序排列的值【数据集合】
# 在python中，存在三种内置的序列类型：
# 字符串、列表、元组

# 序列的优点：可以支持索引和切片的操作
# 特征：第一个正索引为0，指向的是左端；第一个索引为负数的时候，指向的是右端

# 切片是指截取字符串中的其中一段内容。切片使用语法：[起始下标：结束下标：步长]
# （[start:end:step]step默认是1）
# 切片截取的内容不包含结束下标对应的数据，步长指的是隔几个下标获取一个字符

# 字符串常用函数
# 1.	首字母变大写:		capitalize()
# 2.	是否 x结束/开始：		endswith()/startswith()
# 3.	检测x是否在字符串中：		find()/index()
# 4.	判断是否是字母和数字：	isalnum()
# 5.	判断是否是字母： 	        isalpha()
# 6.	判断是否是数字：          isdigit()
# 7.	判断是否是小写：			islower()
# 8.	循环取出所有值用xx去连接：	join()
# 9.	大小写转换：				lower()/upper()
# 10.	大写变小写，小写变大写：	swapcase()
# 11.	移除左/右/两侧空白：		istrip/retrip/strip
# 12.	切割字符串：				split()
# 13.	把每个单词的首字母变成大写：		title()
# 14.	old被换字符串，new替换字符串，count换多少个。
# 	无count表示全部替换:	replace(old,new,count=None)
# 15.	统计出现的次数：	count()
test = '  python_YggFU s    '
#print(type(test))
# print('获取第一个字符:%s'%test[0])
# print('获取第二个字符%s'%test[1])
# for item in test:
# 	print(item,end = ' ')
print(test.capitalize())    # 首字母变大写,其他都变小写
print(test.upper())         # 全部变大写
print(test.count('g'))      # 统计字符串中某一字符出现的次数
print(test.find('y'))       # 返回字符串中某一字符第一次出现的位置,如果未找到，直接返回-1
                            #index()函数未找到，直接报异常
print(test.strip())         #同时去除字符串中左右两端的空格，lstrip()只删除左端空格，rstrip()只删除右端
a = 'hello_cjp'
print('a的内存地址%d'%id(a))     #id()函数可以查看一个对象的内存地址
b = a                            #在此处只是把a的内存地址赋给了b
print('b的内存地址%d'%id(b))     #直接复制字符串，相当于两个名字都对同一个地址的变量进行引用
print(test.endswith(' '))        #判断是否以某字符结尾

str = 'Hello World'
# slice[start:end:stop]          #左闭右开区间
print(str[2:4])                  #输出字符串中第二个和第五个之间的字符
print(str[2:])                   #输出字符串某一字符后面所有的字符
print(str[::-1])                 #-1：倒序输出字符串






