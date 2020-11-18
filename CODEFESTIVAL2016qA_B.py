N=int(input())
ai=list(map(int,input().split()))
ai.insert(0,0)

ans=0

for i in range(1,N+1):
    if ai[ai[i]]==i:
        ans+=1
    else:
        pass
print(ans//2)
