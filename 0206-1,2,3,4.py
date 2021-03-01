# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 21:00:56 2021

@author: USER
"""


for i in range(1,5):
    for a in range(1,i+1):
        print(a,end='')
    print()
print('程式執行完畢')

for i in range(0,10)[::-1]: 
    for a in range(1,i+1,):
       
        print(a,end='')
    print()
print('程式執行完畢')
b=0
i=int(input('請輸入任意數字:'))
for a in range(1,i+1) :
    b+=a
print('1~',i,'總合為:',b,sep='')
print('程式執行完畢')

for i in range(5):
    print("　"*(4-i),end="")
    print('＊　'*(i+1))
for i in range(4)[::-1]:
    print("　"*(4-i),end="")
    print('＊　'*(i+1))
print('程式執行完畢')