# AtCoder Beginner Contest 086
# C - Traveling

N=int(input())

T=0
X,Y=0,0

for i in range (N):
    t, x, y =map(int,input().split())
    time =t-T
    distance=abs((x+y)-(X+Y))
    if time >= distance and time%2==distance%2:
        T=t
        X,Y=x,y
    else :
        print("No")
        exit()

print("Yes")