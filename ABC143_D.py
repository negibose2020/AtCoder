# D - Triangles
import bisect

N=int(input())
Li=list(map(int,input().split()))
Li.sort()

ans=0

for i in range(N):
    for j in range (i+1,N):
        a=Li[i]+Li[j]
        t=bisect.bisect_left(Li,a)
        ans+=t-(j+1)

print(ans)
