import re
t=int(input())
for i in range(t):
    n=input()
    a=sorted([int(x) for x in re.split("[a-z]+",n) if x!=''])
    if len(a)>0:
        print(a[0])