from math import *
def tn(n):
    m=str(n)
    if(len(m)<2): return False
    k=m[::-1]
    if(k!=m): return False
    return True
for t in range(int(input())):
    n=input()
    m=0
    for i in range(len(n)):
        m+=int(n[i])
    if(tn(m)): print("YES")
    else: print("NO")