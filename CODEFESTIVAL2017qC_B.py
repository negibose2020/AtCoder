# CODE FESTIVAL 2017 qual C
# B - Similar Arrays

from itertools import product

N=int(input())
A=list(map(int,input().split()))

ls=[]
ans=0

for i in range (N):
    templs=[]
    for j in range(-1,2):
        templs.append(A[i]+j)
    ls.append(templs)

d=list(product(range(3),repeat=N))

for i in range(len(d)):
    tempnum=1
    for j in range (N):
        tempnum*=ls[j][d[i][j]]
    if tempnum%2==0:
        ans+=1

# print(ls)
# print(d)
print(ans)