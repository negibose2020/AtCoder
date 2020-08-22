# AtCoder Beginner Contest 176
# C - Step

N=int(input())
Als=list(map(int,input().split()))

ans=0

for i in range (1,N):
    if Als[i]>=Als[i-1]:
        pass
    else :
        step=abs(Als[i]-Als[i-1])
        ans+=step
        Als[i]+=step
print(ans)