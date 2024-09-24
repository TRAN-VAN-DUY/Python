from math import *
def check(n):
    a=list(n)
    b=a[::-1]
    for i in range(len(a)-1):
        if abs(ord(a[i])-ord(a[i+1]))!=abs(ord(b[i])-ord(b[i+1])):
            return False
    return True
t=int(input())
while t>0:
    n=input()
    if check(n):
        print("YES")
    else:
        print("NO")
    t-=1