# AtCoder Beginner Contest 194
# B - Job Assignment

n=int(input())

amin=[10**9+7,0] # Aを早く終わらせることができる人の情報[m,i]
bmin=[10**9+7,0] # Bを早く終わらせることができる人の情報[m,i]
a=[]
b=[]

for i in range (n):
    A,B=map(int,input().split())
    a.append(A)
    b.append(B)
    if amin[0]>A: # Aにかかる時間が短ければ更新
        amin=[A,i]
    if bmin[0]>B: # Bにかかる時間が短ければ更新
        bmin=[B,i]
a.sort()
b.sort()

if amin[1]==bmin[1]:
    print(min(amin[0]+bmin[0],max(a[0],b[1]),max(a[1],b[0])))
else:
    print(max(a[0],b[0]))