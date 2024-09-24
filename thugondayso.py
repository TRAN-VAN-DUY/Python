n,a,st=input(),list(map(int,input().split())),[]
for i in a:
    if len(st)>0 and (st[len(st)-1]+i)%2==0:
        st.pop()
    else:
        st.append(i)
print(len(st))