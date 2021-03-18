N,L=map(int,input().split())
x=set(map(int,input().split()))
t1,t2,t3=map(int,input().split())

'''
dp[i]=距離iにいる時の時間の最小値
dp[i] = dp[i-1]+t1
        dp[i-2]+t2+t1
        dp[i-4]+(3*t2)+t1
i==Lの時、そのまま走るか、手前でジャンプするかを決める。
'''
# inf=10**3
inf=10**9+7

dp=[inf]*(L+5)
dp[0]=0
for i in range (1,len(dp)):
    if i<2:
        dp[i]=min(dp[i],dp[i-1]+t1)
        if i in x:
            dp[i]+=t3 

    if i<4:
        dp[i]=min(dp[i],dp[i-1]+t1)
        dp[i]=min(dp[i],(dp[i-2]+t1+t2))
        if i in x:
            dp[i]+=t3

    else:
        dp[i]=min(dp[i],dp[i-1]+t1,dp[i-2]+t1+t2,dp[i-4]+t1+3*t2)
        if i in x:
            dp[i]+=t3
    if i==L:
        dp[i]=min(dp[i],dp[i-1]+t1)
        dp[i]=min(dp[i],dp[i-1]+t1//2+t2//2)
        dp[i]=min(dp[i],dp[i-2]+t1//2+t2+t2//2)
        if L>=3:
            dp[i]=min(dp[i],dp[i-3]+t1//2+t2*2+t2//2)
            if L>=4:
                dp[i]=min(dp[i],dp[i-4]+t1+3*t2)

# print(dp)
print(dp[L])