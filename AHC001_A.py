# AtCoder Heuristic Contest 001
# A - AtCoder Ad

def Calculate_points(x1,y1,x2,y2,r,n):
    w=x2-x1+1 #+1を追加
    h=y2-y1+1 #+1を追加
    s=w*h
    if s<=0: return False
    p=1-(1-min(s,r)/max(s,r))**2
    p/=n
    return p

def CanIGetPoint(x,y,x1,y1,x2,y2):
    if x<x1:return False
    if x>x2:return False
    if y<y1:return False
    if y>y2:return False
    return True

def ReduceSize(x,y,x1,y1,x2,y2,r,n):
    # サイズをカットしても得点が得られるようなx1,y1,x2,y2を返す
    mxp=Calculate_points(x1,y1,x2,y2,r,n)
    w=x2+1-x1
    h=y2+1-y1
    area=w*h
    x1,y1,x2,y2=map(int,[x1,y1,x2,y2])
    rdc=area//r

    for _ in range (5):
        if area+1<=rdc*r:
            break
        ph=mxp
        pw=mxp
        adjst_h=y2-h//rdc
        adjst_w=x2-w//rdc
        if CanIGetPoint(x,y,x1,adjst_h,x2,y2):
            ph=Calculate_points(x1,adjst_h,x2,y2,r,n)
        if CanIGetPoint(x,y,adjst_w,y1,x2,y2):
            pw=Calculate_points(adjst_w,y1,x2,y2,r,n)
        if ph>pw:
            if ph>mxp:
                mxp=ph
                mxcod=[x1,adjst_h,x2,y2]
                x1,y1,x2,y2=map(int,mxcod)
        if pw>ph:
            if pw>mxp:
                mxp=pw
                mxcod=[adjst_w,y1,x2,y2]
                x1,y1,x2,y2=map(int,mxcod)
        w=x2+1-x1
        h=y2+1-y1
        area=w*h
        rdc=area//r

    return [x1,y1,x2,y2]


def TryOutPatturns(x,y,x1,y1,x2,y2,r,n):
    # 複数パターンを試して、一番高い得点のx1,y1,x2,y2を返す
    mxp=Calculate_points(x1,y1,x2,y2,r,n)
    mxcod=[x1,y1,x2,y2]
    reducesizedcod=ReduceSize(x,y,x1,y1,x2,y2,r,n)
    reducesizedp=Calculate_points(reducesizedcod[0],reducesizedcod[1],reducesizedcod[2],reducesizedcod[3],r,n)
    if reducesizedp>mxp:
        mxp=reducesizedp
        mxcod=reducesizedcod

    for i in range (3):
        for j in range (3):
            trying_x1=x1+i
            trying_y1=y1+j
            if CanIGetPoint(x,y,trying_x1,trying_y1,x2,y2):
                p=Calculate_points(trying_x1,trying_y1,x2,y2,r,n)
                if p>mxp:
                    mxp=p
                    mxcod=[trying_x1,trying_y1,x2,y2]
    return mxcod


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
            x1=start_x
            y1=pre_height_num+1
            x2=end_x
            y2=y+1
            if height_oder==height_cnt:
                y2=end_y

            area=(x2-x1)*(y2-y1)

            if area > r:
                arr=TryOutPatturns(x,y,x1,y1,x2,y2,r,n)
                x1=arr[0]
                y1=arr[1]
                x2=arr[2]
                y2=arr[3]
            points_horizontal_stripes+=Calculate_points(x1,y1,x2,y2,r,n)
            # print(start_x,pre_height_num+1,end_x,y+1)
            continue
        else:
            points_horizontal_stripes+=Calculate_points(x,y,x+1,y+1,r,n)
            # print(x,y,x+1,y+1)
            continue


    for ads_i in range (len(ads)):
        x,y,r,j=ads[ads_i]
        if x<start_x or x>end_x:
            continue
        if y<start_y or y>end_y:
            continue
        
        width_i=x
        if width[width_i]==1:
            width_oder=width_list.index(width_i)
            pre_width_oder=width_oder-1
            pre_width_num=width_list[pre_width_oder]
            x1=pre_width_num+1
            y1=start_y
            x2=x+1
            y2=end_y
            if width_oder==width_cnt:
                x2=end_x
            area=(x2-x1)*(y2-y1)

            if area > r:
                arr=TryOutPatturns(x,y,x1,y1,x2,y2,r,n)
                x1=arr[0]
                y1=arr[1]
                x2=arr[2]
                y2=arr[3]
            
            points_vertical_stripes+=Calculate_points(x1,y1, x2,y2,r,n)
            # print(pre_width_num+1,start_y, x+1,end_y)
            continue

        else:
            points_vertical_stripes+=Calculate_points(x,y,x+1,y+1,r,n)
            # print(x,y,x+1,y+1)
            continue

    if points_horizontal_stripes>points_vertical_stripes :
    # if points_horizontal_stripes>points_vertical_stripes or points_horizontal_stripes<points_vertical_stripes:
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
                x1=start_x
                y1=pre_height_num+1
                x2=end_x
                y2=y+1
                area=(x2-x1)*(y2-y1)

                if area >r:
                    arr=TryOutPatturns(x,y,x1,y1,x2,y2,r,n)
                    x1=arr[0]
                    y1=arr[1]
                    x2=arr[2]
                    y2=arr[3]

                dic[j]=[x1,y1,x2,y2]
                # print(start_x,pre_height_num+1,end_x,y+1)
                continue
                '''
                if height_oder==height_cnt:
                    dic[j]=[start_x,pre_height_num+1,end_x,end_y]
                else:
                    dic[j]=[start_x,pre_height_num+1,end_x,y+1]
                '''
            else:
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
            if width[width_i]==1:
                width_oder=width_list.index(width_i)
                pre_width_oder=width_oder-1
                pre_width_num=width_list[pre_width_oder]
                x1=pre_width_num+1
                y1=start_y
                x2=x+1
                y2=end_y
                area=(x2-x1)*(y2-y1)

                if area > r:
                    arr=TryOutPatturns(x,y,x1,y1,x2,y2,r,n)
                    x1=arr[0]
                    y1=arr[1]
                    x2=arr[2]
                    y2=arr[3]

                dic[j]=[x1,y1,x2,y2]
                # print(pre_width_num+1,start_y, x+1,end_y)
                continue
                '''
                if width_oder==width_cnt:
                    dic[j]=[pre_width_num+1,start_y, end_x,end_y]    
                else:
                    dic[j]=[pre_width_num+1,start_y, x+1,end_y]
                '''
            else:
                dic[j]=[x,y,x+1,y+1]
                # print(x,y,x+1,y+1)
                continue
    point=max(points_horizontal_stripes,points_vertical_stripes)
    # print(point*10**9)

    return [dic,point*10**9]


n=int(input())

ads=[]

for i in range (n):
    x,y,r=map(int,input().split())
    ads.append([x,y,r,i])

point4ans=0
dic4ans=dict()

for fh_i in range(1,20):
    for fh_j in range (1,20):
        mx=fh_i*500
        my=fh_j*500
        a1=div_area(0,0,mx,my,ads)
        a2=div_area(mx+1,0,10000,my,ads)
        a3=div_area(0,my+1,mx,10000,ads)
        a4=div_area(mx+1,my+1,10000,10000,ads)
        p=a1[1]+a2[1]+a3[1]+a4[1]
        d=a1[0]
        d.update(a2[0])
        d.update(a3[0])
        d.update(a4[0])
        # print(d)
        if p>point4ans:
            point4ans=p
            dic4ans=dict()
            dic4ans.update(d)

for ans_i in range (n):
    print(*dic4ans[ans_i])
