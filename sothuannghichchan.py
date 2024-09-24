from math import*
def tn(n):
    n=str(n)
    if  len(n)%2!=0:
        return False
    
    for i in range(len(n)):
        if int(n[i])%2!=0:
            return False
    
    for i in range(len(n)):
        if n[i]!=n[len(n)-1-i]:
            return False
    
    return True
a=[]
def lietke():
    for i in range(int(1e6)+1):   
        if tn(i):
            a.append(i)   
    
lietke()
for t in range(int(input())):
    n=int(input())
    for i in range(len(a)):
        if a[i]>=n:
            break
        print(a[i],end=" ")
    print()
