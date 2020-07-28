# DISCO presents ディスカバリーチャンネル コードコンテスト2020 予選
# B - Iron Bar Cutting

import bisect

N=int(input())
A=list(map(int,input().split()))

l=sum(A)//2
m=sum(A)%2

aA=[0]
for i in range (N):
    aA.append(A[i]+aA[-1])

t=bisect.bisect_left(aA,l)


print(abs(aA[t]-l)+m)
