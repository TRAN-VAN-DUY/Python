from math import *
def tn(n):
    if n==0 or n==1: return False
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0): return False
    return True
def check(n):
    m=0
    for i in range(len(n)-4,len(n)):
        m=m*10+int(n[i])
    if(tn(m)==False): return False
    return True
for t in range(int(input())):
    n=input()
    if(check(n)): print("YES")
    else: print("NO")