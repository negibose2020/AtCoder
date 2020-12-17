import math
N,K=map(int,input().split())

ans=0

for i in range (1,N+1):
    for j in range (100):
        a=i*2**j
        if a>=K:
            ans+=1/N*(0.5**j)
            break

print(ans)