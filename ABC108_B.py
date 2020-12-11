# AtCoder Beginner Contest 108
# B - Ruined Square

x1,y1,x2,y2=map(int,input().split())

if x1<=x2:
    if y1<=y2:
        x3=x2-(y2-y1)
        y3=y2+(x2-x1)
        x4=x1-(y2-y1)
        y4=y1+(x2-x1)
    else:
        x3=x2+(y1-y2)
        y3=y2+(x2-x1)
        x4=x1+(y1-y2)
        y4=y1+(x2-x1)

else:
    if y1<=y2:
        x3=x2-(y2-y1)
        y3=y2-(x1-x2)
        x4=x1-(y2-y1)
        y4=y1-(x1-x2)
    else:
        x3=x2+(y1-y2)
        y3=y2-(x1-x2)
        x4=x1+(y1-y2)
        y4=y1-(x1-x2)

print(x3,y3,x4,y4)