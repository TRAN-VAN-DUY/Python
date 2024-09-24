n=int(input())
v=[]
for i in range(n-1):
    t=int(input())
    v.append(t)
v.sort()
for i in range(n-1):
    if v[i]!=i+1:
        sbt=i+1
        break
    else:
        sbt=n
print(sbt)