# AtCoder Beginner Contest 188
# B - Orthogonality

import numpy as np

N=int(input())

A=list(map(int,input().split()))
B=list(map(int,input().split()))

a=np.array(A)
b=np.array(B)

if np.dot(a,b)==0:
    print("Yes")
else:
    print("No")