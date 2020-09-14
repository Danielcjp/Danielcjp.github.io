#	list是一种有序的集合，可以随时添加和删除其中的元素
#	list特点：	1.支持增删改查	2.列表中的数据是可以变化的【数据项可以变化，内存地址不会改变】
#				3.用[]表示list类型，数据项之间用逗号来分割，数据项可以是任何类型的数据
#				4.支持索引和切片来进行数据的处理

# append在列表后面追加元素
# count统计元素出现的次数
# extend扩展，相当于批量添加
# index获取指定元素索引号
# insert在指定位置插入
# pop删除最后一个元素
# remove移除左边找到的第一个元素
# reverse反转列表
# sort列表排序

aha = [1,2,3,"你好"]
print(aha)
print(len(aha))
print(type(aha))
str = '我喜欢python'
print(len(str))
print('--------------输出---------------------')
oho = ['wo',44,'c','jp',' !',True]
print(oho)              #   输出完整的列表
print(oho[1:4])         #   输出列表中第二个元素到第四个为止，左闭右开区间
print(oho*2)            #   输出两次列表的元素
print(oho[5:1:-1])      #   倒序输出列表中的元素
print('--------------添加---------------------')
oho.append(['niu','bi','6'])    #   append在列表后端再追加一个列表
print(oho)

oho.insert(1,'这是我刚插入到第二个位置的数据')      #   插入操作，在某个位置插入某元素
print(oho)

oho.extend([2,3,4,5])
print(oho)
#extend与append添加稍有不同，extend添加的是一个个元素
#append添加的是整个列表作为一个元素
print('--------------修改---------------------')
enne = ['a','tu','pu','you','123',False]
print('修改之前的enne:',enne)
enne[0] = 2333                      #   修改列表中的第一个元素
print('修改之后的enne:',enne)
print('--------------删除---------------------')
axi = ['shan','you','ga','t',123]
print('删除之前的axi:',axi)
del axi[0]                          # 删除列表中目标元素
print('删除之后的axi:',axi)
del axi[1:2]                        # 切片删除元素
print('删除第二个元素之后的axi:',axi)
axi.remove(123)                     # 删除列表中特定元素
print('删除123之后的axi:',axi)
axi.pop(1)                          # 删除特定位置的元素
print('删除之后的axi:',axi)         # 如若括号内不写位置，默认删除最后一个元素

print('--------------查找---------------------')
hhh = ['yi',2,'san',456]
print(hhh.index('san',0,3))             # 查找列表中某一元素的位置
                                        # 后面可用可不用写明查找范围






