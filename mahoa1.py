from math import *
t=int(input())
while t>0:
    n=input()
    dem=1
    for i in range(0,len(n)-1):
        if(n[i]==n[i+1]):
            dem+=1
        else:
            print(dem,n[i],sep='',end='')
            dem=1
    if dem>1:
        print(dem,n[len(n)-1],sep='',end='\n')
    else:
        print(dem,n[len(n)-1],sep='',end='\n')
    t-=1