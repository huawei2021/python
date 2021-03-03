# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 20:23:25 2021

@author: USER
"""
import random
count=0
ans=random.randint(1,100)
guess=0
min=1
max=100
while ans!=guess:
    guess=int(input('請輸入%d-%d之間的整數:' % (min,max)))
    if guess>max or guess<min:
        print('輸入錯誤')
        continue
    if ans>guess:
        min=guess+1        
    if ans<guess:
        max=guess-1       
    count+=1    
print('賓果，共猜了%d次'%count)

