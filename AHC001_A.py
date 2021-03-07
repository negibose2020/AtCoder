# AtCoder Heuristic Contest 001
# A - AtCoder Ad

n=int(input())
ads=[]
minx=1000
minxi=-1
miny=1000
minyi=-1
maxx=0
maxxi=-1
maxy=0
maxyi=-1
for i in range (n):
    x,y,r=map(int,input().split())
    ads.append([x,y,r,i])
    if x<minx:
        minx=x
        minxi=i
    if y<miny:
        miny=y
        minyi=i
    if x>maxx:
        maxx=x
        maxxi=i
    if y>maxy:
        maxy=y
        maxyi=i


area=[]

# sortedads=sorted(ads,key=)


for i in range (n):
    if i==minxi:
        print(0,ads[i][1],ads[i][0]+1,ads[i][1]+1)
    elif i==minyi:
        print(ads[i][0],0,ads[i][0]+1,ads[i][1]+1)
    elif i==maxxi:
        print(ads[i][0],ads[i][1],10000,ads[i][1]+1)
    elif i==maxyi:
        print(ads[i][0],ads[i][1],ads[i][0]+1,10000)
    else:
        print(ads[i][0],ads[i][1],ads[i][0]+1,ads[i][1]+1)

# print(ads)