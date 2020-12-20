# パナソニックプログラミングコンテスト
# AtCoder Beginner Contest 186
# B - Blocks on Grid

H,W=map(int,input().split())

minValue=150

AREA=[]
for i in range (H):
    w=list(map(int,input().split()))
    minOfThisW=min(w)
    minValue=min(minValue,minOfThisW)
    AREA.append(w)

ans=0
for i in range (H):
    for j in range (W):
        ans+=AREA[i][j]-minValue

print(ans)