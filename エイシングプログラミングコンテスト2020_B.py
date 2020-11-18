N=int(input())
ai=list(map(int,input().split()))

ai=ai[::2]

ans=0

for i in range(len(ai)):
    if ai[i] %2==1:
        ans+=1
print(ans)

N=int(input())
ai=list(map(int,input().split()))

ans=0

for a in ai[::2]:
    if a%2==1:
        ans+=1
print(ans)


N=int(input())
ai=list(map(int,input().split()))

ans=0

for i in range(N):
    if i%2==1:
        continue

    if ai[i] %2==1:
        ans+=1
print(ans)
