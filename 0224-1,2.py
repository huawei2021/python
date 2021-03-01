# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 20:59:13 2021

@author: USER
"""

'''
1.輸入迴圈次數，判斷哪些數值是奇數，哪些是偶數
2.輸入迴圈次數，計算數值中為偶數的加總，印出加總值
'''
a=0
b=0
for i in range(11):
    if i%2==0 and i!=0:
        a+=i
        print('偶數',i)
    elif i%2!=0:
        b+=i
        print('奇數',i)
print('奇數總和為',b)
print('偶數總和為',a)