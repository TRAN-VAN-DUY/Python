def to(a,b,s:str):
    return int(s.replace(str(a),str(b)))
t=int(input())
for i in range(t):
    a,b=[int(x) for x in input().split()]
    x1=input()
    if(len(x1.split())>1): x1,x2=x1.split()
    else: x2=input()
    if a>b: a,b=b,a
    lon=to(a,b,x1)+to(a,b,x2)
    nho=to(b,a,x1)+to(b,a,x2)
    print(nho,lon)