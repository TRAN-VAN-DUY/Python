def isValid(s):
    a=s.count('A')
    b=s.count('B')
    c=s.count('C')
    return len(s)>=3 and a*b*c>0 and a<=b and b<=c
def back(i,s,n,list):
    if(i>n): return 
    if isValid(s): list+=[s]
    if i<n:
        back(i+1,s+'A',n,list)
        back(i+1,s+'B',n,list)
        back(i+1,s+'C',n,list)

list = []
back(0,'',int(input()),list)
list.sort(key=lambda e: (len(e),e))
print(*list,sep='\n')