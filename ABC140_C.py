# AtCoder Beginner Contest 140
# C - Maximal Value
'''
Aiは、Bの配列の隣り合う数字の最小値になる。
なお、
A[0]は、B[0]と一緒になる。
A[1]は、B[0]とB[1]の最小値となる。
A[2]は、B[1]とB[2]の最小値となる。
    ...(略)...
A[-1]は、B[-1]と一緒になる。
Bの配列の初めと終わりにinfを追加すれば、すべてのAに対して
A[0]は、B[0](追加したinf)とB[1]との最小値(結果的にB[1](もとのB[0]))
A[1]は、B[1]とB[2]との最小値
A[-1]は、B[-2]とB[-1](追加したinf)との最小値(結果的にB[-2](もとのB[-1]))
Aの配列候補を答えに足していく
'''

N=int(input())
Bfirst=[10**5+3]
B=list(map(int,input().split()))
Blast=[10**5+3]
BL=Bfirst+B+Blast

ans=0

for i in range (N):
    ans+= min(BL[i],BL[i+1])

print(ans)