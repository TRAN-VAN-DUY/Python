t=int(input())
diem=[int(input()) for i in range(t)]
diem.sort()
silver=diem[-2]
print(f"Silver = {silver}")