# パナソニックプログラミングコンテスト（AtCoder Beginner Contest 186）
# C - Unlucky 7

N=int(input())
ans=0
for i in range (N+1):
    if ("7" in str(i)) or ("7" in str(oct(i))):
        ans+=1

print(N-ans)