from math import *
def nto(n):
    if(n==0 or n==1): return False
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0): return False
    return True

for i in range(int(input())):
    n=int(input())
    cnt=0
    for j in range(n-6):
        if (nto(j) and nto(j+6)) and (nto(j+4) or nto(j+2)):
            cnt+=1
    print(cnt)