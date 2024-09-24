for i in range(int(input())):
    s=input()
    ok=1
    ans=""
    for i in range(len(s)-1):
        x=str(s[i])
        z=int(s[i+1])
        i+=1
        for j in range(z):
            ans+=x
    print(ans)
        
