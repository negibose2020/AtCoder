s=input()
t=input()

dplen=max(len(s),len(t))+1

dp=[[0 for i in range (len(t)+1) ] for j in range (len(s)+1)]

for i in range (1,len(s)+1):
    for j in range (1,len(t)+1):
        dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        if s[i-1]==t[j-1]:
            dp[i][j]=max(dp[i][j],dp[i-1][j-1]+1)

# print(dp)


reverseans=""
i=len(s)
j=len(t)

while(i>0 and j>0):
    if dp[i][j]==dp[i-1][j]:
        i-=1
    elif dp[i][j]==dp[i][j-1]:
        j-=1
    else:
        i-=1
        j-=1
        reverseans+=s[i]


print(reverseans[::-1])