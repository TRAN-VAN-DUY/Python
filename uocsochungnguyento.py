from math import *
def nto(n):
    if(n<=1):
        return False
    else:
        for i in range(2,int(sqrt(n))+1):
            if(n%i==0):
                return False
    return True

def tong(n):
    tong=0
    while(n!=0):
        tong+=n%10
        n//=10
    return tong

t=int(input())
while t>0:
    a,b=map(int,input().split())
    if(nto(tong(gcd(a,b)))):
        print("YES")
    else:
        print("NO")
    t-=1