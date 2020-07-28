# AtCoder Beginner Contest 046
# B - AtCoDeerくんとボール色塗り

N,K=map(int,input().split())

ans=K

for _ in range(1,N):
    ans*=K-1

print(ans)
