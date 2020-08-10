# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 16:25:15 2020

@author: wenpengspc
"""

import random
ans=random.randint(1,20)
t=0
while t<5:
    g=input("輸入數字")
    g=int(g)
    if g>ans:
        if t==4:
            print("你猜五次了,掰")
        else:
            print("猜小點")
        t=t+1
    elif g<ans:
        if t==4:
            print("你猜五次了,掰")
        else:
            print("猜大點")
            t=t+1
    else:
        print("猜對了")
        t=t+1
        print("你你總共猜了"+str(t)+"次猜對的")      
        break
   

        