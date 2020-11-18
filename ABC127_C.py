# AtCoder Beginner Contest 127
# C - Prison
import numpy as np


N,M= map(int,input().split())

cardnums=[i for i in range (1,N+1)]
canthrough=[0]*N
C=np.array([cardnums,canthrough])

print(C)

for i in range (M):
    r,l = map(int,input().split())
    C=np.delete(C,np.where(C<r)[0],axis=1)
    C=np.delete(C,np.where(C>l)[0],axis=1)
    

print(C)

#     C=np.where(C<r,0,C)
#     C=np.where(C>l,0,C)

# print(np.count_nonzero(C))