N=int(input())
hlist=list(map(int,input().split()))
dp=[10*5]*N
dp[0]=0
dp[1]=abs(hlist[1]-hlist[0])

if N>2:
    for i in range (2,N):
        c1=abs(hlist[i]-hlist[i-2])+dp[i-2]
        c2=abs(hlist[i]-hlist[i-1])+dp[i-1]
        dp[i]=min(c1,c2)

print(dp[-1])


#初DP問題AC
