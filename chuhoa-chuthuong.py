from math import *
def check(n):
    a=list(map(str,n))
    hoa=0
    thuong=0
    for i in range(0,len(a)):
        if 'a'<=a[i]<='z':
            thuong+=1
        else:
            hoa+=1
    if thuong>=hoa:
        return True
    else:
        return False
    
n=input()
if(check(n)):
    print(n.lower())
else:
    print(n.upper())