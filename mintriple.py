for t in range(int(input())):
    n,m=int(input()),-1e9
    a=[int(x) for x in input().split()]
    for j in range(n):
        l,r=j+1,n-1
        while l<r:
            s=a[j]+a[l]+a[r]
            m=min(s,m)
            