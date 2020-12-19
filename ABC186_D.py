# パナソニックプログラミングコンテスト（AtCoder Beginner Contest 186）
# D - Sum of difference

N=int(input())
A=list(map(int,input().split()))
A.sort()
ans=0
ac_A=[0]
for i in range (N):
    ac_A.append(ac_A[-1]+A[i])

for i in range (1,N):
    ans+=A[i]*i-ac_A[i]

print(ans)