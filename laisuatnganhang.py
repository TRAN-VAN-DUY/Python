from math import *
t=int(input())
while t>0:
    n,x,m=map(float,input().split())
    k=1
    n+=n*x//100
    while n<m:
        k+=1
        n+=n*x//100
    print(k)
    t-=1