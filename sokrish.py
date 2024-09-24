from math import *
def gt(x):
    tich=1
    for i in range(2,x+1):
        tich*=i
    return tich
def check(n):
    tong=0
    m=n
    while(n!=0):
        tong+=gt(n%10)
        n//=10
    if tong==m: return True
    return False
for i in range(int(input())):
    n=int(input())
    if check(n)==True:
        print("Yes")
    else:
        print("No")