# 元组：一种不可变的序列，在创建之后不能做任何的修改
# 1. 不可变
# 2. 用 ()来创建元组类型，数据项用逗号来分割，可以是任何类型
# 3. 当元组中只有一个元素时，要加上逗号。否则解释器会当作整型来处理
# 4. 支持切片操作
tuple_A = (1,'a',3,'sadf',345,'qwer',True,['ad',234])
print(tuple_A)      # 元组一经创建，就无法修改
print('-----------------元组的查询-----------')
for item in tuple_A:
    print(item,end = ' ')       # for循环遍历显示
    pass
print('   ')
print(tuple_A[1:3])
print(tuple_A[4:2:-1])
print(tuple_A[::-2])            # 每隔一个取一次
print(tuple_A[-2:-1])           # 倒序取（最右边为-1开始，依次递减。如从右至左下标依次为：-1 -2 -3..）
print('-----------------元组中列表内的数据可修改-----------')
tuple_A[7][1] = 'ap'
print(tuple_A)

tuple_B = tuple(range(10))
print(tuple_B)
print(tuple_B.count(0))         #统计元组中特定数据出现的次数

