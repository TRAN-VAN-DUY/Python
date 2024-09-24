from math import *
def chiahet(n):
    a=list(map(int,n))
    tong=0
    for i in range(len(a)):
        tong+=a[i]
    if tong%10==0:
        return True
    return False

def check(n):
    a=list(map(int,n))
    for i in range(len(a)-1):
        if abs(a[i]-a[i+1])!=2:
            return False
    return True

t=int(input())
while t>0:
    n=input()
    if check(n) and chiahet(n):
        print("YES")
    else:
        print("NO")
    t-=1