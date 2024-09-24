from math import *
n=input()
a=list(map(int,n))
k=0
for i in range(0,len(a)):
    if(a[i]==4) or (a[i]==7):
        k+=1
if(k==4) or (k==7):
    print("YES")
else:
    print("NO")