from math import *
def nto(n):
    if(n==0 or n==1): return False
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0): return False
    return True

for t in range(int(input())):
    n=input()
    if(nto(len(n))==False):
        print("NO")
    else:
        k=0
        for i in range(len(n)):
            if(nto(int(n[i]))):
                k+=1
            if(k>len(n)//2):
                print("YES")
                break
        if(k<=len(n)//2): print("NO")    