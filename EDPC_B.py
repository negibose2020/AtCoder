N,K=map(int,input().split())
h=list(map(int,input().split()))

dp=[1000000000]*(N)
dp[0]=0
for i in range (1,N):
    for j in range (1,K+1):
        if i-j<0:
            continue
        else:
            dp[i]=min(dp[i],dp[i-j]+abs(h[i]-h[i-j]))
            # print(dp)

# print(dp)
print(dp[-1])