from math import *
for t in range(int(input())):
    n=input()
    m=1
    for i in range(len(n)):
        if(n[i]!='0'):
            m*=int(n[i])
    print(m)
    