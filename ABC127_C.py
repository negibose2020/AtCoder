# AtCoder Beginner Contest 127
# C - Prison

import numpy as np

N,M= map(int,input().split())

# cards=[0]*N+1

G=[0]*(N+1)
Garr=np.array(G)

for i in range (M):
    l,r=map(int,input().split())
    g=[1 if ( l<=i and i<=r ) else 0 for i in range (N+1)]
    garr=np.array(g)
    Garr+=garr

ans=np.count_nonzero(Garr==M)

print (ans)
