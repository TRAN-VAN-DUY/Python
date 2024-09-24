from math import *
def tong(n):
    m=0
    for i in range(1,len(n),2):
        m+=int(n[i])
    return m
def tich(n):
    m=1
    for i in range(0,len(n),2):
        if n[i]!='0':
            m*=int(n[i])
    return m
for t in range(int(input())):
    n=input()
    print(tich(n),tong(n))