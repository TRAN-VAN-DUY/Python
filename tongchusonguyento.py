from math import *
def tn(n):
    if n==0 or n==1: return False
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0): return False
    return True
for t in range(int(input())):
    n=input()
    m=0
    for i in range(len(n)):
        m+=int(n[i])
    if(tn(m)): print("YES")
    else: print("NO")