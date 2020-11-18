N=int(input())
Ai=list(map(int,input().split()))

# ans=[]
ans=[0]*N

# for i in range(1,N+1):
    # a=Ai.index(i)+1
    # ans.append(str(a))
for i in range (N):
    ans[Ai[i]-1]=str(i+1)

print(' '.join(ans))

# index()は線形探索
# 逆順列
