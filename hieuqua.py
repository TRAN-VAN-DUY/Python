a0,b0,c0=map(int,input().split())
a1,b1,c1=map(int,input().split())
timestart=a0*3600+b0*60+c0
timeend=a1*3600+b1*60+c1
if timeend>=timestart:
    timerun=timeend-timestart
else:
    timerun=86400-timestart+timeend
print(timerun)