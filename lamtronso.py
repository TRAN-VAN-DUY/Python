t=int(input())
for i in range(1,t+1):
    n=input()
    a=list(map(int,n))
    if len(a)==1:
        print(a[0])
    else:
        for i in range(len(a)-1,0,-1):
            if a[i]>=5:
                a[i]=0
                a[i-1]=a[i-1]+1
            else:
                a[i]=0
        for i in range(len(a)):
            print(a[i],end='')
    print(end='\n')