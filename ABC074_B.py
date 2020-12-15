# AtCoder Beginner Contest 074
# B - Collecting Balls (Easy Version)

N=int(input())
K=int(input())
x=list(map(int,input().split()))

ans=0

for i in range(N):
    if x[i]>abs(x[i]-K):
        ans+=abs(x[i]-K)
        ans+=abs(x[i]-K)
    else:
        ans+=x[i]
        ans+=x[i]

print(ans)