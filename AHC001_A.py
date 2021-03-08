# AtCoder Heuristic Contest 001
# A - AtCoder Ad

def Calculate_points(x1,y1,x2,y2,r,n):
    w=x2-x1
    h=y2-y1
    s=w*h
    p=1-(1-min(s,r)/max(s,r))**2
    p/=n
    return p


def div_area(start_x,start_y,end_x,end_y,ads):
    n=len(ads)
    height=[0]*10000
    height_list=[start_y-1]
    width=[0]*10000
    width_list=[start_x-1]
    points_horizontal_stripes=0
    points_vertical_stripes=0
    height_cnt=0
    width_cnt=0
    dic=dict()

    for ads_i in range (len(ads)):
        x,y,r,j=ads[ads_i]
        if x < start_x or x > end_x :
            continue
        if y < start_y or y > end_y :
            continue
        height[y]+=1
        height_list.append(y)
        width[x]+=1
        width_list.append(x)
        height_cnt+=1
        width_cnt+=1

        height_list.sort()
        width_list.sort()

    for ads_i in range (len(ads)):
        x,y,r,j=ads[ads_i]
        if x<start_x or x>end_x :
            continue
        if y<start_y or y>end_y:
            continue

        height_i=y
        if height[height_i]==1:
            height_oder=height_list.index(height_i)
            pre_height_oder=height_oder-1
            pre_height_num=height_list[pre_height_oder]
            if height_oder==height_cnt:
                points_horizontal_stripes+=Calculate_points(start_x,pre_height_num+1,end_x,end_y,r,n)
            else:
                points_horizontal_stripes+=Calculate_points(start_x,pre_height_num+1,end_x,y+1,r,n)
                # print(start_x,pre_height_num+1,end_x,y+1)
            continue

        else:
            points_horizontal_stripes+=Calculate_points(x,y,x+1,y+1,r,n)
            # print(x,y,x+1,y+1)
            continue


    for ads_i in range (len(ads)):
        x,y,r,j=ads[ads_i]
        if x<start_y or x>end_x:
            continue
        if y<start_y or y>end_y:
            continue
        
        width_i=x
        if width[width_i]==1:
            width_oder=width_list.index(width_i)
            pre_width_oder=width_oder-1
            pre_width_num=width_list[pre_width_oder]
            if width_oder==width_cnt:
                points_vertical_stripes+=Calculate_points(pre_width_num+1,start_y, end_x,end_y,r,n)
            else:
                points_vertical_stripes+=Calculate_points(pre_width_num+1,start_y, x+1,end_y,r,n)
            # print(pre_width_num+1,start_y, x+1,end_y)
            continue
        else:
            points_vertical_stripes+=Calculate_points(x,y,x+1,y+1,r,n)
            # print(x,y,x+1,y+1)
            continue


    if points_horizontal_stripes>points_vertical_stripes:
        for ads_i in range (len(ads)):
            x,y,r,j=ads[ads_i]
            if x<start_x or x>end_x :
                continue
            if y<start_y or y>end_y:
                continue

            height_i=y
            if height[height_i]==1:
                height_oder=height_list.index(height_i)
                pre_height_oder=height_oder-1
                pre_height_num=height_list[pre_height_oder]
                if height_oder==height_cnt:
                    dic[j]=[start_x,pre_height_num+1,end_x,end_y]
                # points_horizontal_stripes+=Calculate_points(start_x,pre_height_num+1,end_x,y+1,r,n)
                else:
                    dic[j]=[start_x,pre_height_num+1,end_x,y+1]
                # print(start_x,pre_height_num+1,end_x,y+1)
                continue
            else:
                # points_horizontal_stripes+=Calculate_points(x,y,x+1,y+1,r,n)
                dic[j]=[x,y,x+1,y+1]
                # print(x,y,x+1,y+1)
                continue
    else:
        for ads_i in range (len(ads)):
            x,y,r,j=ads[ads_i]
            if x<start_x or x>end_x:
                continue
            if y<start_y or y>end_y:
                continue
            
            width_i=x
            desired_area=r
            if width[width_i]==1:
                width_oder=width_list.index(width_i)
                pre_width_oder=width_oder-1
                pre_width_num=width_list[pre_width_oder]
                if width_oder==width_cnt:
                    dic[j]=[pre_width_num+1,start_y, end_x,end_y]    
                # points_vertical_stripes+=Calculate_points(pre_width_num+1,start_y, x+1,end_y,r,n)
                else:
                    dic[j]=[pre_width_num+1,start_y, x+1,end_y]
                # print(pre_width_num+1,start_y, x+1,end_y)
                continue

            else:
                # points_vertical_stripes+=Calculate_points(x,y,x+1,y+1,r,n)
                dic[j]=[x,y,x+1,y+1]
                # print(x,y,x+1,y+1)
                continue
    return dic







n=int(input())

ads=[]

for i in range (n):
    x,y,r=map(int,input().split())
    ads.append([x,y,r,i])

ans=[]

a=div_area(0,0,10000//2,10000//2,ads)
b=div_area(10000//2,0,10000,10000//2,ads)
c=div_area(0,10000//2,10000,10000,ads)
a.update(b)
a.update(c)
#  =>Score: 597947519

# a=div_area(0,0,10000//2,10000//2,ads)
# b=div_area(10000//2,0,10000,10000//2,ads)
# c=div_area(0,10000//2,10000//2,10000,ads)
# d=div_area(10000//2,10000//2,10000,10000,ads)
# a.update(b)
# a.update(c)
# a.update(d)
#  =>Score: 561258921

# a=div_area(0,0,3000,5000,ads)
# b=div_area(3001,0,10000,5000,ads)
# c=div_area(0,5001,10000,10000,ads)
# a.update(b)
# a.update(c)
#  =>Score: 575013904


# a=div_area(0,0,10000,10000,ads)
#  =>Score: 570530257

for i in range (n):
    print(*a[i])