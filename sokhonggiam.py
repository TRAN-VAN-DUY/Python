from math import *
def check(n):
    a=list(map(int,n))
    for i in range(len(a)-1):
        if(a[i]>a[i+1]):
            return False
    return True

t=int(input())
while t>0:
    n=input()
    if(check(n)):
        print("YES")
    else:
        print("NO")
    t-=1