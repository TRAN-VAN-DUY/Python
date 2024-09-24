from math import *
for t in range(int(input())):
    def ans(n):
        for i in range(len(n)):
            if(n[i]!='0' and n[i]!='1' and n[i]!='2'): return "NO"
        return "YES"
    print(ans(input()))