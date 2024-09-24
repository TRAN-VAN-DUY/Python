from math import *
def nt(x):
    if(x<2): return False
    if x==2: return True
    if(x%2==0): return False
    for i in range(3,int(sqrt(x))+1,2):
        if(x%i==0): return False
    return True
def check(n):
    tong=0
    while(n!=0):
        tong+=n%10
        if nt(n%10)==False:
            return False
        n//=10
    if nt(tong)==False: return False
    return True
for i in range(int(input())):
    n=int(input())
    if(nt(n)==True and nt(int(''.join(reversed(str(n)))))==True and check(n)==True):
        print("Yes")
    else:
        print("No")