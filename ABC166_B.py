N,K=map(int,input().split())
L=[0]*(N+1)

ans=0

for i in range(K):
    _d=int(input())
    _a=list(input().split())
    for _ in _a:
        L[int(_)]+=1

for j in range(1,N+1):
    if L[j]==0:
        ans+=1
print(ans)