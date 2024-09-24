n=input().strip()
word=n.split()
longword=max(word,key=len)
print(longword,len(longword))