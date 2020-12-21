import math

N,M=map(int,input().split())

mod=10**9+7

if abs(N-M)>1:
    print(0)
    exit()
n=math.factorial(N)%mod
m=math.factorial(M)%mod
if N==M:
    print((n*m)*2%mod)
    exit()
print((n*m)%mod)