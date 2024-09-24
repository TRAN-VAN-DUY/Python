from math import *
def smm(n):
    a=list(map(int,n))
    for i in range(0,len(a)):
        if(a[i]!=4) and (a[i]!=7):
            return False
    return True

if __name__ == '__main__':
    t=int(input())
    while t>0:
        n=input()
        if(smm(n)):
            print("YES")
        else:
            print("NO")
        t-=1