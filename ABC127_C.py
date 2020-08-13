# AtCoder Beginner Contest 127
# C - Prison

import numpy as np

N,M= map(int,input().split())

# cards=[0]*N+1

G=[0]*(N+1)

for i in range (M):
    l,r=map(int,input().split())
    for j in range(l,r+1):
        G[j]+=1

print(G.count(M))