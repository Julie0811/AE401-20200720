# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 17:32:10 2020

@author: wenpengspc
"""

scores=[]
total=0
avg=0

n=input("班上有幾位大佬?")
n=int(n)

for i in range(n):
    name=input("輸入名子")
    scores.append(name)
    
    s=input("輸入成績=")
    s=int(s)
    scores.append(s)
for item in range(1,n*2,2):
    total=total+scores[item]
print("平均是",total/n)

highest=0
for i in range(1,n*2,2):
    if scores[i]>highest:
        highest=scores[i]
        highestname=scores[i-1]
print(highestname,"最高分是",highest)
lowest=100
for i in range(1,n*2,2):
    if scores[i]<lowest:
        lowest=scores[i]
        lowestname=scores[i-1]
print(lowestname,"最低分是",lowest)
