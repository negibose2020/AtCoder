N=int(input())
Ai=list(map(int,input().split()))


Ai.sort()

ans=0

for i in range (1,N):
    if i%2==0:
        ans+=Ai[-1]
    else:
        ans+=Ai.pop()
print(ans)