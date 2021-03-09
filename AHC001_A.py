# AtCoder Heuristic Contest 001
# A - AtCoder Ad

def Calculate_points(x1,y1,x2,y2,r,n):
    w=x2-x1
    h=y2-y1
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




def div_area(start_x,start_y,end_x,end_y,ads):
    n=len(ads)
    height=[0]*10000
    height_list=[start_y-1]
    width=[0]*10000
    width_list=[start_x-1]
    points_horizontal_stripes=0
    points_vertical_stripes=0
    # height_cnt=0
    # width_cnt=0
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
        # height_cnt+=1
        # width_cnt+=1

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
            area=(x2-x1)*(y2-y1)

            if area > r:

                if Calculate_points(x1,y1+25,x2,y2,r,n):
                    y1+=25
                elif Calculate_points(x1,y1+20,x2,y2,r,n):
                    y1+=20
                elif Calculate_points(x1,y1+15,x2,y2,r,n):
                    y1+=15
                elif Calculate_points(x1,y1+10,x2,y2,r,n):
                    y1+=10
                elif Calculate_points(x1,y1+5,x2,y2,r,n):
                    y1+=5
                elif Calculate_points(x1,y1+3,x2,y2,r,n):
                    y1+=3
                else:
                    pass
                # y1+=3
                # rdc=area/r
                # ajst=int(((y2-y1)/rdc)//1)
                # if y1+ajst>=y2:
                #     y1=y2+1
                # else:
                #     y1+=ajst
            points_horizontal_stripes+=Calculate_points(x1,y1,x2,y2,r,n)
            # print(start_x,pre_height_num+1,end_x,y+1)
            continue
            '''
            最後だったらareaを拡大しようとしたけど逆にスコア下がったのでお蔵入り
            if height_oder==height_cnt:
                points_horizontal_stripes+=Calculate_points(start_x,pre_height_num+1,end_x,end_y,r,n)
            else:
                points_horizontal_stripes+=Calculate_points(start_x,pre_height_num+1,end_x,y+1,r,n)
                # print(start_x,pre_height_num+1,end_x,y+1)
            '''

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
            x1=pre_width_num+1
            y1=start_y
            x2=x+1
            y2=end_y
            area=(x2-x1)*(y2-y1)

            if area > r:
                if Calculate_points(x1+25,y1,x2,y2,r,n):
                    x1+=25
                elif Calculate_points(x1+20,y1,x2,y2,r,n):
                    x1+=20
                elif Calculate_points(x1+15,y1,x2,y2,r,n):
                    x1+=15
                elif Calculate_points(x1+10,y1,x2,y2,r,n):
                    x1+=10
                elif Calculate_points(x1+5,y1,x2,y2,r,n):
                    x1+=5
                elif Calculate_points(x1+3,y1,x2,y2,r,n):
                    x1+=3
                else:
                    pass
            



            points_vertical_stripes+=Calculate_points(x1,y1, x2,y2,r,n)
            # print(pre_width_num+1,start_y, x+1,end_y)
            continue
            '''
            最後だったらareaを拡大しようとしたけど逆にスコア下がったのでお蔵入り
            if width_oder==width_cnt:
                points_vertical_stripes+=Calculate_points(pre_width_num+1,start_y, end_x,end_y,r,n)
            else:
                points_vertical_stripes+=Calculate_points(pre_width_num+1,start_y, x+1,end_y,r,n)
                # print(pre_width_num+1,start_y, x+1,end_y)
            '''
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
                    if Calculate_points(x1,y1+25,x2,y2,r,n):
                        y1+=25
                    elif Calculate_points(x1,y1+20,x2,y2,r,n):
                        y1+=20
                    elif Calculate_points(x1,y1+15,x2,y2,r,n):
                        y1+=15
                    elif Calculate_points(x1,y1+10,x2,y2,r,n):
                        y1+=10
                    elif Calculate_points(x1,y1+5,x2,y2,r,n):
                        y1+=5
                    elif Calculate_points(x1,y1+3,x2,y2,r,n):
                        y1+=3
                    else:
                        pass

                    # rdc=area/r
                    # ajst=int(((y2-y1)/rdc)//1)
                    # if y1+ajst>=y2:
                    #     y1=y2+1
                    # else:
                    #     y1+=ajst

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
                    if Calculate_points(x1+25,y1,x2,y2,r,n):
                        x1+=25
                    elif Calculate_points(x1+20,y1,x2,y2,r,n):
                        x1+=20
                    elif Calculate_points(x1+15,y1,x2,y2,r,n):
                        x1+=15
                    elif Calculate_points(x1+10,y1,x2,y2,r,n):
                        x1+=10
                    elif Calculate_points(x1+5,y1,x2,y2,r,n):
                        x1+=5
                    elif Calculate_points(x1+3,y1,x2,y2,r,n):
                        x1+=3
                    else:
                        pass
            
                dic[j]=[pre_width_num+1,start_y, x+1,end_y]
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


aa=div_area(0,0,10000//2,10000//2,ads)
bb=div_area(10000//2,0,10000,10000//2,ads)
cc=div_area(0,10000//2,10000,10000,ads)
c1=aa[1]+bb[1]+cc[1]
aa=aa[0]
aa.update(bb[0])
aa.update(cc[0])
#  =>Score: 606660526

dd=div_area(0,0,10000//2,10000//2,ads)
ee=div_area(10000//2,0,10000,10000//2,ads)
ff=div_area(0,10000//2,10000//2,10000,ads)
gg=div_area(10000//2,10000//2,10000,10000,ads)
c2=dd[1]+ee[1]+ff[1]+gg[1]
dd=dd[0]
dd.update(ee[0])
dd.update(ff[0])
dd.update(gg[0])
#  =>Score: 569533297

hh=div_area(0,0,3000,5000,ads)
ii=div_area(3001,0,10000,5000,ads)
jj=div_area(0,5001,10000,10000,ads)
c3=hh[1]+ii[1]+jj[1]
hh=hh[0]
hh.update(ii[0])
hh.update(jj[0])
#  =>Score: 582000792


kk=div_area(0,0,10000,10000,ads)
c4=kk[1]
kk=kk[0]
#  =>Score: 590233842

ll=div_area(0,0,10000,3000,ads)
mm=div_area(0,3000,10000,6000,ads)
nn=div_area(0,6000,10000,10000,ads)
c5=ll[1]+mm[1]+nn[1]
ll=ll[0]
ll.update(mm[0])
ll.update(nn[0])


oo=div_area(0,0,3000,10000,ads)
pp=div_area(3000,0,10000,5000,ads)
qq=div_area(3000,5000,10000,10000,ads)
c6=oo[1]+pp[1]+qq[1]
oo=oo[0]
oo.update(pp[0])
oo.update(qq[0])

if c1==max(c1,c2,c3,c4,c5,c6):
    for i in range (n):
        print(*aa[i])
elif c2==max(c1,c2,c3,c4,c5,c6):
    for i in range (n):
        print(*dd[i])
elif c3==max(c1,c2,c3,c4,c5,c6):
    for i in range (n):
        print(*hh[i])
elif c4==max(c1,c2,c3,c4,c5,c6):
    for i in range (n):
        print(*kk[i])
elif c5==max(c1,c2,c3,c4,c5,c6):
    for i in range (n):
        print(*ll[i])
else:
    for i in range(n):
        print(*oo[i])