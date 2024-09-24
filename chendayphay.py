from math import *
n=input()
a=list(n)
for i in range(len(a)-3,0,-3):
    a.insert(i,',')
for i in range(len(a)):
    print(a[i],end='')