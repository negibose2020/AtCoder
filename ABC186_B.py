# パナソニックプログラミングコンテスト（AtCoder Beginner Contest 186）
# B - Blocks on Grid

H,W=map(int,input().split())

mini=999999999999999

E=[]
for i in range (H):
    w=list(map(int,input().split()))
    _mini=min(w)
    mini=min(mini,_mini)
    E.append(w)
# print(E)
# print(H,W)
ans=0
for i in range (H):
    for j in range (W):
        ans+=E[i][j]-mini

print(ans)