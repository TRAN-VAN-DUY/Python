from math import *
def tn(n):
    if n==0 or n==1: return False
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0): return False
    return True
def check(n):
    for i in range(len(n)):
        if(tn(i)):
            if(tn(int(n[i]))==False):
                return False
        else:
            if(tn(int(n[i]))):
                return False
    return True

for t in range(int(input())):
    n=input()
    if(check(n)): print("YES")
    else: print("NO")