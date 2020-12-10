# AtCoder Beginner Contest 094
# B - Toll Gates

import bisect

N,M,X=map(int,input().split())
A=list(map(int,input().split()))

b=bisect.bisect(A,X)
l=A[:b]
r=A[b:]
print(min(len(l),len(r)))