# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:15:32 2021

@author: USER
"""

'''
1.六個數以氣泡排序法排列
2.1~49取6個數不重複
'''

      


import random
a=list()
for i in range(1,50):
    a.append(i)
n=random.sample(a,6)

# while len(n)<6:
#     num=int(input('請輸入數字:'))
#     n.append(num)
print('串列內容:',n)
print('氣泡排序法:')
l=len(n)
for i in range(l)[::-1]:
    for j in range(i):
        if n[j]>n[j+1]:
            k=n[j]
            n[j]=n[j+1]
            n[j+1]=k
print(n)







