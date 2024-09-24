m=int(input())
v=int(input())
t=int(input())
d=input().strip()
ds=v*t
if d=='C':
    kp=ds%m
elif d=='A':
    kp=(m-ds%m)%m
print(kp)