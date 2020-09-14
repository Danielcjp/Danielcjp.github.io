# 函数：一系列python语句的组合，可以在程序中运行一次或多次，一般是完成具体的独立的功能
# 使用函数的原因：代码的复用最大化以及最小化冗余代码，整体代码结构清晰，问题局部化
# 函数定义：def + 关键字 + 小括号 + 冒号 + 换行缩进 + 代码块 定义一个函数
# def 函数名():
	# 代码块

# 函数调用：函数名加()即可完成调用该函数



# 处理其他的逻辑信息
# 多次去打印小李的信息

print('--------多次输出相同的信息----------')
def out(name,height,weight,hobby,pro):
    '''
    这个函数用来打印个人信息
    :return:
    '''
    print("%s的身高是%f" % (name,height))
    print("%s的体重是%f" % (name,weight))
    print("%s的爱好是%s" % (name,hobby))
    print("%s的专业是%s" % (name,pro))
    pass
out('小李',1.73,60,'coding','EIE')

# 1.必选参数
def sum(a,b):           # a,b在这里是形式参数：只是意义上的一种参数，不占用内存地址
    sum = a + b
    print(sum)
    pass
sum(1,2)                # 1，2在这里是实参，占用内存地址

# 2.默认参数【缺省参数】  默认参数始终放在参数列表中的尾部
def sum1(a = 10,b = 20):
    print('默认参数使用 = %d'%(a + b))
    pass
sum1()                  # 调用时如果不写参数，则直接使用默认参数的值
sum1(1,2)               # 调用时写明参数，则按照写明的参数值进行计算返回
sum1(1)                 # 调用时若只写一个参数值，则只能默认赋值给函数中第一个参数

# 3.可变长参数【当参数的个数不确定时使用】 使用*进行声明     args为元组类型
def changeable(*args):
    '''
    计算累加和
    :param args:
    :return:
    '''
    result = 0
    for item in args:
        result = result + item
        pass
    print('累加和为%d'%result)
    pass

changeable(1,2)
changeable(1,2,3)

# 4.关键字可变参数
# ** 来定义参数
# 在函数体内，参数关键字是一个字典类型，key是一个字符串
def keyfunc(**kwargs):
    print(kwargs)
    pass
dict_A = {'pro':'艺术','school':'CUGB'}
keyfunc(**dict_A)               # 如果直接传入字典类型的参数给函数，则需要加**
print('-------')
keyfunc(name = 'daniel',age = 23)     # 也可以直接以键值对的形式传给函数

def complex_func(*args,**kwargs):     # 可变长参数必须放到关键字可变参数之前
    print(args)                       # def complex_func(**kwargs,*args):这种不符合语法规范

    print(kwargs)
    pass
complex_func(1,2,3,4,name = '李等闲')
complex_func(age = 36)
# ==========================================================
# 函数执行完以后会返回一个对象，如果在函数的内部有return，就可以返回实际的值，否则返回的是none
# 在一个函数体中，可以出现多个return值，但是肯定只能返回一个。会整合为一个元组直接返回出来
def sum(a,b):
	c = a + b
	return c
	pass
result = sum(10,20)
print(result)

def calculate(num):
    list = []
    re = 0
    i = 1
    while i <= num:
        re = i + re
        i = i + 1
        pass
    list.append(re)
    return list
    pass
print(calculate(10))            # 返回数据类型可根据自身需要设置，可以是列表 元组 字典等等
# ==========================================================
def fun1():
    print("-==-=-==-1start=-")
    print("-==-=-==-balabala=-")
    print("-==-=-==-1end=-")
    pass
def fun2():
    print("-==-=-==-2start=-")
    fun1()                          # 函数fun2调用函数fun1
    print("-==-=-==-2end=-")
    pass
fun2()
# 函数的分类
# 1.有参数无返回值 2. 有参数有返回值  3.无参数无返回值   4.无参数有返回值


