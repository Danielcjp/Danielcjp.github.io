# 1.求三组连续自然数的和：求出1到10，20到30，30到45的和

# a = int(input('请输入下限：'))
# b = int(input('请输入上限：'))
# print(sum(range(a,b + 1)))

# 2.100个和尚吃100个馒头，大和尚一人吃3个馒头，小和尚三人吃一个馒头，请问大小和尚各有多少个
# da = 1
# while da <= 100:
# 	if 3 * da + (100 - da) / 3 == 100:
# 		print('大和尚一共有%d，小和尚有%d个'%(da,100 - da))
# 		break
# 	da = da + 1

# 3.指定一个列表，列表里含有唯一一个只出现过一次的数字。写程序找出这个 独一无二 的数字
list = [1,2,3,2,3,4,5,6,4,56,5,6,7,7,56]
set1 = set(list)		#只取出重复项中的一个
print(set1)
for i in set1:
	list.remove(i)
	pass
set2 = set(list)
print(set1 - set2)