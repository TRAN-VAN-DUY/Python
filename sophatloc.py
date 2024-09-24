from math import *
def spl(n):
    a=list(n)
    if a[len(a)-2]!='8' or a[len(a)-1]!='6':
        return False
    return True

t=int(input())
while t>0:
    n=input()
    if spl(n):
        print("YES")
    else:
        print("NO")
    t-=1