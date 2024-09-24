from math import *
t=int(input())
while t>0:
    n=input()
    a=int(n)
    m=int(n[::-1])
    if gcd(m,a)==1:
        print("YES")
    else:
        print("NO")
    t-=1