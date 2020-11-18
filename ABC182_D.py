# AtCoder Beginner Contest 182
# D - Wandering

N=int(input())
Als=list(map(int,input().split()))

nowPosition=0
maxMoveToRight=0
lastMoveDist=0
maxR=0


for i in range (N):
    nowMoveDist=lastMoveDist+Als[i]
    if nowMoveDist>maxMoveToRight:
        maxMoveToRight=nowMoveDist
    if nowPosition+maxMoveToRight>maxR:
        maxR=nowPosition+maxMoveToRight
    nowPosition+=nowMoveDist
    lastMoveDist=nowMoveDist

print(maxR)