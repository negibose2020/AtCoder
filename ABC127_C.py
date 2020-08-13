# AtCoder Beginner Contest 127
# C - Prison
import numpy as np


N,M= map(int,input().split())

cards=[i for i in range (1,N+1)]
C=np.array(cards)

for i in range (M):
    r,l = map(int,input().split())
    C=np.where(C<r,0,C)
    C=np.where(C>l,0,C)

print(np.count_nonzero(C))