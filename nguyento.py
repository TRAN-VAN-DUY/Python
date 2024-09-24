from math import *
def nt(n):
    if(n<=1):
        return False
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0):
            return False
    return True

def ntcn(i,n):
    if(gcd(i,n)==1):
        return True
    return False

if __name__ == '__main__':
    t=int(input())
    while t>0:
        n=int(input())
        k=0
        for i in range(1,n):
            if(ntcn(i,n)):
                k+=1
        if(nt(k)):
            print("YES")
        else:
            print("NO")
        t-=1