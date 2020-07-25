# ABC0555 - B - Training Camp

N=int(input())

ans=1

for i in range(1,N+1):
    ans*=i
    ans%=(10**9+7)

print(ans)
