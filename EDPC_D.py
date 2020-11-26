N,W=map(int,input().split())
w=[]
v=[]
for i in range (N):
    a,b=map(int,input().split())
    w.append(a)
    v.append(b)

# dp[i][j]は、i未満までのj以下の価値の最大値
# dp=[[0]*(W+1) for i in range (N+1)]
dp=[[0 for i in range (W+1)] for j in range(N+1)]
for i in range (N):
    for j in range (W+1):
        if j<w[i]: # jよりもアイテムの単体で大きい場合は選べない
            dp[i+1][j]=dp[i][j]
        else:
            # 選ぶときは、空けた分の容量の価値のMAXとi個目を追加したものと、今までの最大値を比較
            dp[i+1][j]=max(dp[i][j],dp[i][j-w[i]]+v[i])

print(dp[-1][-1])
# print(w,v)