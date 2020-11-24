# AtCoder Beginner Contest 184
# C - Super Ryuma

# 動けるマスの判定関数
def canSuperRyumaMoveCell(a,b,c,d):
    if a+b==c+d:
        return True
    if a-b==c-d:
        return True
    if abs(a-c)+abs(b-d)<=3:
        return True
    else:
        return False

r1,c1=map(int,input().split())
r2,c2=map(int,input().split())

# 0手で任意のマスに到達
if (r1,c1)==(r2,c2):
    print(0)
    exit()

# 1手で任意のマスに到達
if canSuperRyumaMoveCell(r1,c1,r2,c2):
    print(1)
    exit()


# 2手で任意のマスに到達_1
if (r1+c1)%2==(r2+c2)%2:
    print(2)
    exit()

# 2手で任意のマスに到達_2
firstMove=[[-3,0],[0,-3],[3,0],[0,3],[-2,-2],[-2,-1],[-2,0],[-2,1],[-2,2],[-1,-2],[-1,-1],[-1,0],[-1,1],[-1,2],[0,-2],[0,-1],[0,0],[0,1],[0,2],[1,-2],[1,-1],[1,0],[1,1],[1,2],[2,-2],[2,-1],[2,0],[2,1],[2,2]]
# print(len(firstMove))
for i in range (29):
    r=r1+firstMove[i][0]
    c=c1+firstMove[i][1]
    if canSuperRyumaMoveCell(r,c,r2,c2):
        print(2)
        exit()

# 2手で任意のマスに到達出来なかった場合
print(3)