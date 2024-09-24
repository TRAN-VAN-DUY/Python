from math import *
def tn(n):
    if n==0 or n==1: return False
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0): return False
    return True
def sum(n):
    sum=0
    for i in range(len(n)):
        sum+=int(n[i])
    return sum
def check(n):
    if(tn(sum(n))==False): return False
    for i in range(len(n)):
        if(i%2==0):
            if(int(n[i])%2==1): return False
        else:
            if(int(n[i])%2==0): return False
    return True

for t in range(int(input())):
    n=input()
    if(check(n)): print("YES")
    else: print("NO")