N=int(input())

abc=[]
for i in range (N):
    _=list(map(int,input().split()))
    abc.append(_)
# print(abc)

dp=[[0]*3 for i in range (N)]
dp[0][0]=abc[0][0]
dp[0][1]=abc[0][1]
dp[0][2]=abc[0][2]
for i in range(1,N):
    for j in range(3):
        if j==0:
            dp[i][j]=max(dp[i-1][1]+abc[i][j],dp[i-1][2]+abc[i][j])
            # print(dp)
        if j==1:
            dp[i][j]=max(dp[i-1][2]+abc[i][j],dp[i-1][0]+abc[i][j])
            # print(dp)
        if j==2:
            dp[i][j]=max(dp[i-1][0]+abc[i][j],dp[i-1][1]+abc[i][j])
            # print(dp)

print(max(dp[-1]))