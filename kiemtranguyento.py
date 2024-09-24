from math import *
t=int(input())
def nto(n):
    if(n==0 or n==1): return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True    
while(t>0):
    t-=1
    n=input()
    m=0
    for i in range(len(n)-4,len(n),1):
        m=m*10+int(n[i])
    if(nto(m)): print("YES")
    else: print("NO")