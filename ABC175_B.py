# AtCoder Beginner Contest 175
# B - Making Triangle

import bisect

N=int(input())
L=list(map(int,input().split()))

L.sort()

ans=0

for i in range (N):
    for j in range (i+1,N):
        if L[i]==L[j]:
            pass
        else:
            ab=L[i]+L[j]
            c=bisect.bisect_left(L,ab)
            bequalc=bisect.bisect_right(L,L[j])
            ans+=c-(bequalc)

print(ans)