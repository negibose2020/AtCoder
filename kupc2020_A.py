# 京都大学プログラミングコンテスト 2020
# A - Classroom Distance

N=int(input())
ans=0
preX,preY=map(int,input().split())

for i in range (N-1):
    x,y=map(int,input().split())
    ans+=abs(preX-x)+abs(preY-y)
    preX=x
    preY=y
print(ans)