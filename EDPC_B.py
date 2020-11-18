N,K=map(int,input().split())
hi=list(map(int,input().split()))

dp=[10000000]*(N)
dp[0]=0
for i in range (1,N):
    dp[i]=min(dp[i],abs(hi[i]-hi[i-1])+dp[i-1])
    # print(dp)
    if 1 < i :
        for j in range(1,K+1):
            if j>i:
                pass
            else:
                dp[i]=min(dp[i],abs(hi[i]-hi[i-j])+dp[i-j])
            # print(dp)

# print(dp)
print(dp[-1])