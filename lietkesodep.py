from math import *
def check(n):
    for i in range(len(n)):
        if(int(n[i])%2==1):
            return False
    for i in range(int(len(n))//2):
        if n[i]!=n[len(n)-1-i]:
            return False
    if len(n)%2==1:
        return False
    return True
for t in range(int(input())):
    n=input()
    for i in range(22,int(n),2):
        if(check(str(i))):
            print(i,end=" ")
    print()