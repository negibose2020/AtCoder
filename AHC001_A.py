# AtCoder Heuristic Contest 001
# A - AtCoder Ad

n=int(input())
ads=[]
for _ in range (n):
    x,y,r=map(int,input().split())
    ads.append([x,y,r])

area=[]

for i in range (n):
    print(ads[i][0],ads[i][1],ads[i][0]+1,ads[i][1]+1)

# print(ads)