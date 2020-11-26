N,W=map(int,input().split())
w=[]
v=[]
for i in range (N):
    a,b=map(int,input().split())
    w.append(a)
    v.append(b)

inf=10**9+7

dp=[[inf for i in range (110000)] for j in range (N+1)]

dp[0][0]=0
for i in range (N):
    for j in range (110000):
        if j<v[i]:
            dp[i+1][j]=dp[i][j]
        else:
            dp[i+1][j]=min(dp[i][j],dp[i][j-v[i]]+w[i])
# print(dp[-1][:150])

ans=0

for k in range (110000):
    tempans=dp[-1][k]
    if tempans!=inf:
        if tempans>W:
            continue    
        ans=k
print(ans)