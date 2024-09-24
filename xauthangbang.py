from math import *
def check(n):
    n1=n[::-1]
    for i in range(len(n)-1):
        if(abs(ord(n[i])-ord(n[i+1]))!=(abs(ord(n1[i])-ord(n1[i+1])))): return False
    return True
for t in range(int(input())):
    s=input()
    if(check(s)): print("YES")
    else: print("NO")