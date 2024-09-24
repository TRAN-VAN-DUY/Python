from math import *
for t in range(int(input())):
    n=input()
    m=0
    for i in range(len(n)):
        m+=int(n[i])
    if(m%3==0): print("YES")
    else: print("NO")