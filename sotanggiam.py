from math import *
for t in range(int(input())):
    def ans(n):
        if len(n)<3: return "NO"
        index=-1
        for i in range(len(n)):
            if n[i]>=n[i+1]:
                index=i
                break
        for i in range(index,len(n)-1):
            if n[i]<=n[i+1]: return "NO"
        return "YES"
    print(ans(input()))