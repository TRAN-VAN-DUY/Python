from math import *
def check(n):
    m=0
    for i in range(1,len(n),2):
        if(n[i]=='0'):
            m+=1
    if(m!=len(n)//2): return False
    return True
def tong(n):
    m=0
    for i in range(0,len(n),2):
        m+=int(n[i])
    return m
def tich(n):
    m=1
    if(check(n)): m=0
    else:
        for i in range(1,len(n),2):
            if(n[i]!='0'):
                m*=int(n[i])
    return m
for t in range(int(input())):
    n=input()
    print(tong(n),tich(n))