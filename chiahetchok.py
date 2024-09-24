from math import *
a,k,n=map(int,input().split())
v=[]
cuoi=n//k
for i in range(0,cuoi*k+1,k):
    if i>a:
        v.append(i-a)
if(len(v)==0):
    print("-1")
else:
    for i in range(len(v)):
        print(v[i],end=' ')