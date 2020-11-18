# AtCoder Regular Contest 107
# 


a,b,c=map(int,input().split())

mod=998244353

A=(a*(a+1))//2
B=(b*(b+1))//2
C=(c*(c+1))//2

ans=A%mod
ans*=B%mod
ans*=C%mod


print(ans%mod)