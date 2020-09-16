name = 'peter'
def changeGlobal():
    '''
    修改全局变量
    :return:
    '''
    global name
    name = '你爸爸'

    pass
changeGlobal()
print(name)
print('======')
#如果在函数中想要修改全局变量的话，必须使用global关键字进行声明才能修改
# ======================================================
# 传参不可变类型
a = 1
def func(x):
    print('x的地址：{}'.format(id(x)))  # x和a是对一个地址的引用，只是使用了不同的名字
    x = 2
    print('x修改后的地址：{}'.format(id(x)))       # x重新赋值以后，指向地址发生改变
    pass
print('a的地址：{}'.format(id(a)))
func(a)
print('======')
#========================================================
# 传参可变类型
li = []
def test(parms):
    li.append([1,2,3,4,5,6])
    print(id(parms))
    print('内部的{}'.format(parms))        #函数内部修改变量的值，可变类型的地址不发生改变
    pass
print(id(li))
test(li)
print('外部的变量对象{}'.format(li))
#========================================================
# 匿名函数lambda
# lambda 参数1，参数2，参数3：执行代码表达式
# 缺点：只能是单个表达式，只能实现一些简单函数的功能，仅仅能封装有限的逻辑
test = lambda x,y:x*y
print(test(1,2))        #通过变量调用匿名函数lambda
print(test(4,5))

age = 15
print('可以参军' if age > 18 else '继续学习')   # 用一行简单的写法替换传统双分支的写法

greater = lambda a,b:a if a > b else b
print(greater(1,2))

max1 = (lambda a,b,c:a if a > b and a > c else '不是a')(7,2,3)    #可以直接在lambda函数后直接调用传参

print(max1)
#========================================================
# 递归函数 函数内部调用自身，必须要有一个结束的条件，否则会无法结束
# 求阶乘
# 用循环的方式求解
# a = int(input('请输入数字：'))
# i = 1
# result = 1
# while i <= a:
#     result = result * i
#     i = i + 1
#     pass
# print('%d的阶乘为：%d'%(a,result))
# 用递归的方式求解
set_in = int(input('请输入数字：'))
def recursion(n):
    if n == 1:
        return 1
    else:
        return n * recursion(n - 1)
    pass
print('%d的阶乘为：%d'%(set_in,recursion(set_in)))
# print(recursion(set_in))
# 递归案例 模拟实现 树形结构的遍历
import os           #导入文件操作模块
def find_file(file_path):
    listRs = os.listdir(file_path)          # 得到该路径下所有的文件夹
    for fileitem in listRs:
        full_path = os.path.join(file_path,fileitem)    # 获取完整的文件路径
        if os.path.isdir(full_path):                    # 判断是否是文件夹
            find_file(full_path)                        # 如果是一个文件夹，再次去递归
            pass
        else:
            print(fileitem)
            pass
        pass
    else:
        return

    pass
find_file('E:\\python\\')