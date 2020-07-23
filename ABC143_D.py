# D - Triangles
from itertools import combinations

N=int(input())
Li=list(map(int,input().split()))

ans=0

l=list(combinations(Li,3))
for i in range(len(l)):
    a,b,c=l[i]
    if a<b+c and b<c+a and c<a+b:
        ans+=1

print(ans)
