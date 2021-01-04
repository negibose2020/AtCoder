# AtCoder Beginner Contest 187
# D - Choose Me

N=int(input())

T=0
A=0
ls=[]

for i in range (N):
    a,b=map(int,input().split())
    ls.append([a,b])
    A+=a
sortedls=sorted(ls, key=lambda x:2*x[0]+x[1],reverse=True)

ans=0

for i in range (N):
    A=A-sortedls[i][0]
    T=T+sortedls[i][0]+sortedls[i][1]
    if A>=T:
        continue
    else:
        print(i+1)
        exit()