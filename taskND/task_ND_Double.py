"""
题号:1  题型:问答/综合题  本题分数:10
创建一个变量age表示一个人的年龄，赋予合理值。再使用if-elif-else结构，根据年龄输出他处于哪个年龄阶段
1. 如果年龄小于2岁，输出"baby"
2. 如果年龄为2（含）至13（含）岁，输出"kid"
3. 如果年龄为14（含）至20（含）岁，输出"teenager"
4. 如果年龄为21（含）至60（含）岁，输出"adult"
5. 如果年龄大于60岁，输出"senior citizen"
"""


def task1():
    age = 20
    if age < 2:
        print("baby")
    elif 2 <= age <= 13:
        print("kid")
    elif 14 <= age <= 20:
        print("teenager")
    elif 21 <= age <= 60:
        print("adult")
    else:
        print("senior citizen")


'''
题号:2  题型:问答/综合题  本题分数:10
选择5个熟悉的英语单词，完成以下操作 
1. 将每个单词分别作为关键字(key)，词对应的中文意思作为值(value)，建立字典(dict)。 
2. 向字典中加入"apple": "苹果" 
3. 将"apple"对应的项从字典中删除 
4. 遍历字典输出每个键值对
'''


def task2():
    fruitDic = {"Banana": "香蕉", "Blueberry": "蓝莓", "Cherry": "樱桃", "Grape": "葡萄", "Kiwifruit": "猕猴桃"}
    fruitDic.update({"apple": "苹果"})
    fruitDic.pop("apple")
    for k, v in fruitDic.items():
        print('%s:%s' % (k, v))


'''
题号:3  题型:问答/综合题  本题分数:10
任意选择五个城市的英文名，用python完成以下操作 
1. 将城市名存储在一个列表中，并打印出来 
2. 使用append向列表添加一个新的城市名，打印列表 
2. 将列表中所有城市名按字典序由小到大输出
'''


def task3():
    cityList = ["Beijing", "Shanghai", "Hong Kong", "Guangzhou", "Shenzhen"]
    print(cityList)
    cityList.append("Tianjin")
    print(cityList)
    cityList.sort()
    print(cityList)


'''
题号:4  题型:问答/综合题  本题分数:10
编写程序给定一个正整数n，在屏幕输出如下面样例所示的n行的图案，如n=5时，输出 ***** **** *** ** * n=3时，输出 *** ** *
'''


def task4(num):
    count = num  # count用来计算每行空格的个数
    while num:
        print((count - num) * "", end="")
        print(num * "*")
        num -= 1


'''
题号:5  题型:问答/综合题  本题分数:10
编写函数，实现以下功能： 
1. 函数参数为一个由整数组成的列表 
2.函数返回列表中最大整数在列表中的下标（如有多个最大整数，则返回下标最小的）
'''
elist = [1, 4, 6, 8, 3, 9, 10, 5, 10]
newList = elist.copy()
maxNum = 0
for i in range(0, len(newList)-1):
    for j in range(i+1, len(newList)):
        if newList[i] > newList[j]:
            newList[i], newList[j] = newList[j], newList[i]

maxNum = newList[-1]
Num = elist.index(maxNum)
print("最大数是%d，它的下标为%d" % (maxNum, Num))


'''
题号:6  题型:问答/综合题  本题分数:10
编写函数，实现以下功能： 
1. 函数参数为两个数a, b 
2. 函数返回a÷b的结果 
3. 使用异常处理，当出现除零错误时输出错误提示
'''


def task6_div(a, b):
    try:
        print(a / b)
        return a / b
    except ZeroDivisionError as e:
        print("ZeroDivisionError: division by zero")


'''
题号:7  题型:问答/综合题  本题分数:10
斐波那契数列满足f(0)=1, f(1)=1, f(n)=f(n-1)+f(n-2) (n≥2) 编写程序计算f(10)
'''
num = int(input("请输入需要计算的项数："))
n1 = 1
n2 = 1
count = 2
numList = []
if num < 0:
    print("请输入一个正整数")
elif num == 1 or num == 0:
    print("裴波那契数列：")
    print(n1)
else:
    print("裴波那契数列：")
    numList = [1, 1]
    # print(numList)
    while count <= num:
        nth = n1 + n2
        numList.append(nth)
        n1 = n2
        n2 = nth
        count += 1
    print(numList)

# 使用高阶函数实现
# def task7(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return task7(num - 2) + task7(num - 1)


'''

题号:8  题型:问答/综合题  本题分数:10
使用pyplot绘制y=cos(x) (0≤x≤2*PI)的函数曲线
'''
import numpy as np
import matplotlib.pyplot as plt

plt.xticks([0, np.pi / 2, np.pi, np.pi * 3 / 2, np.pi * 2],
           [r'$0$', r'$\pi/2$', r'$\pi$', r'$\pi*3/2$', r'$\pi*2$'])
x = np.linspace(0, np.pi * 2, 256, endpoint=True)
y = np.cos(x)
plt.plot(x, y, 'b', linewidth=2)
plt.show()

'''
题号:9  题型:问答/综合题  本题分数:10
编写程序在屏幕打印出"Hello Python!"
'''
print("Hello Python!")


'''
题号:10  题型:问答/综合题  本题分数:10
读取一个文本文件，统计文件中不同单词的个数。
'''
# coding=gb2312
import string

words = {}
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for line in open("test.txt"):
    for word in line.split():
        word = word.strip(strip)
        if len(word) >= 1:
            words[word] = words.get(word, 0)+1

for word in sorted(words):
    print("'{0}': {1} times".format(word, words[word]))


if __name__ == "__main__":
    task1()
    task2()
    task3()
    task4(10)
    task6_div(1, 10)

