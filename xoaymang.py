for t in range(int(input())):
    n,d=map(int,input().split())
    a=[int(x) for x in input().split()]
    for i in range(d,n):
        print(a[i],end=' ')
    for i in range(0,d):
        print(a[i],end=' ')
    print(end='\n')