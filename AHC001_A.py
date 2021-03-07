# AtCoder Heuristic Contest 001
# A - AtCoder Ad

n=int(input())
ads=[]
h=[0]*10000

for i in range (n):
    x,y,r=map(int,input().split())
    ads.append([x,y,r,i])
    h[y]+=1



for i in range (n):
    height_i=ads[i][1]
    if h[height_i]==1:
        print(0,ads[i][1],10000,ads[i][1]+1)
    else:
        print(ads[i][0],ads[i][1],ads[i][0]+1,ads[i][1]+1)