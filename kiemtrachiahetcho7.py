from math import *
for i in range(int(input())):
    def ans(n):
        for j in range(1000):
            if int(n)%7==0:
                return n
            n=str(int(n)+int(''.join(reversed(n))))
        return -1
    print(ans(input()))