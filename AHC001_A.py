# AtCoder Heuristic Contest 001
# A - AtCoder Ad

n=int(input())
ads=[]
height=[0]*10000
height_list=[-1]

for i in range (n):
    x,y,r=map(int,input().split())
    ads.append([x,y,r,i])
    height[y]+=1
    height_list.append(y)

height_list.sort()

for i in range (n):
    height_i=ads[i][1]
    if height[height_i]==1:
        height_oder=height_list.index(height_i)
        pre_height_oder=height_oder-1
        pre_height_num=height_list[pre_height_oder]

        print(0,pre_height_num+1,10000,ads[i][1]+1)
    else:
        print(ads[i][0],ads[i][1],ads[i][0]+1,ads[i][1]+1)