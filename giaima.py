from math import *
t=int(input())
while t>0:
    n=input()
    for i in range(0,len(n),2):
        for j in range(0,int(n[i+1])):
            print(n[i],end='')
    print(end='\n')
    t-=1
    