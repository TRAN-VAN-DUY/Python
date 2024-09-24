from math import *
def check(n):
    a=list(map(int,n))
    if(a[0]!=a[len(a)-2]) or (a[1]!=a[len(a)-1]):
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