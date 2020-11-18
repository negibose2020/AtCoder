# AtCoder Beginner Contest 183
# C - Travel

import itertools

N,K=map(int,input().split())

Tls=[]
for i in range (N):
    t=list(map(int,input().split()))
    Tls.append(t)

ans=0

v=list(itertools.permutations(range(N-1)))
for i in range (len(v)):
    D=v[i]
    path=[1]
    time=0
    for j in range(len(D)):
        path.append(D[j]+2)
    path.append(1)
    # print(path) // 都市を巡回するルートを確認
    for k in range(len(path)-1):
        time+=Tls[path[k]-1][path[k+1]-1]
    if time==K:
        ans+=1
print(ans)