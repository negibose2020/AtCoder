# AtCoder Heuristic Contest 001
# A - AtCoder Ad

def Calculate_points(x1,y1,x2,y2,r,n):
    w=x2-x1
    h=y2-y1
    s=w*h
    p=1-(1-min(s,r)/max(s,r))**2
    p/=n
    return p

n=int(input())
ads=[]
height=[0]*10000
height_list=[-1]
width=[0]*10000
width_list=[-1]
points_horizontal_stripes=0 #横縞
points_vertical_stripes=0 #縦縞

for i in range (n):
    x,y,r=map(int,input().split())
    ads.append([x,y,r,i])
    height[y]+=1
    height_list.append(y)
    width[x]+=1
    width_list.append(x)

height_list.sort()
width_list.sort()



for i in range (n):
    height_i=ads[i][1]
    desired_area=ads[i][2]
    if height[height_i]==1:
        height_oder=height_list.index(height_i)
        pre_height_oder=height_oder-1
        pre_height_num=height_list[pre_height_oder]
        points_horizontal_stripes+=Calculate_points(0,pre_height_num+1,10000,ads[i][1]+1,desired_area,n)
        

        # print(0,pre_height_num+1,10000,ads[i][1]+1)
        continue

    else:
        points_horizontal_stripes+=Calculate_points(ads[i][0],ads[i][1],ads[i][0]+1,ads[i][1]+1,desired_area,n)
        # print(ads[i][0],ads[i][1],ads[i][0]+1,ads[i][1]+1)
        continue

for i in range (n):
    width_i=ads[i][0]
    desired_area=ads[i][2]
    if width[width_i]==1:
        width_oder=width_list.index(width_i)
        pre_width_oder=width_oder-1
        pre_width_num=width_list[pre_width_oder]
        points_vertical_stripes+=Calculate_points(pre_width_num+1,0,ads[i][0]+1,10000,desired_area,n)
        # print(pre_width_num+1,0,ads[i][0]+1,10000)

        continue

    else:
        points_vertical_stripes+=Calculate_points(ads[i][0],ads[i][1],ads[i][0]+1,ads[i][1]+1,desired_area,n)
        # print(ads[i][0],ads[i][1],ads[i][0]+1,ads[i][1]+1)

        continue

# print(points_horizontal_stripes*10**9)
# print(points_vertical_stripes*10**9)

points_horizontal_stripes*=10**9
points_vertical_stripes*=10**9

# if points_horizontal_stripes <= points_vertical_stripes : #確認用
if points_horizontal_stripes > points_vertical_stripes :
    for i in range (n):
        height_i=ads[i][1]
        # desired_area=ads[i][2]
        if height[height_i]==1:
            height_oder=height_list.index(height_i)
            pre_height_oder=height_oder-1
            pre_height_num=height_list[pre_height_oder]
            # points_horizontal_stripes+=Calculate_points(0,pre_height_num+1,10000,ads[i][1]+1,desired_area,n)
            print(0,pre_height_num+1,10000,ads[i][1]+1)
            continue

        else:
            # points_horizontal_stripes+=Calculate_points(ads[i][0],ads[i][1],ads[i][0]+1,ads[i][1]+1,desired_area,n)
            print(ads[i][0],ads[i][1],ads[i][0]+1,ads[i][1]+1)
            continue
else:
    for i in range (n):
        width_i=ads[i][0]
        # desired_area=ads[i][2]
        if width[width_i]==1:
            width_oder=width_list.index(width_i)
            pre_width_oder=width_oder-1
            pre_width_num=width_list[pre_width_oder]
            # points_vertical_stripes+=Calculate_points(pre_width_num+1,0,ads[i][0]+1,10000,desired_area,n)
            print(pre_width_num+1,0,ads[i][0]+1,10000)
            continue

        else:
            # points_vertical_stripes+=Calculate_points(ads[i][0],ads[i][1],ads[i][0]+1,ads[i][1]+1,desired_area,n)
            print(ads[i][0],ads[i][1],ads[i][0]+1,ads[i][1]+1)
            continue