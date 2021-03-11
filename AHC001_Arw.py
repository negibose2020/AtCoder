# AtCoder Heuristic Contest 001
# A - AtCoder Ad

def calculateScore(v,r,n):
    '''
    # v : 四角形の頂点4つ [x1,y1,x2,y2]
    # r : 希望する面積
    # n : 企業数
    企業広告の四角形の頂点4つから得られる得点を計算し、
    True or False と、Trueの場合は以下を返す。
    True : 得点
    False : False
    '''
    x1, y1, x2, y2 = map(int, v)
    w = x2 - x1
    h = y2 - y1
    s = w * h
    if s <= 0 : return False
    p = 1 - (1 - min(s, r) / max(s, r)) ** 2
    p /= n
    return p

def canIGetScore(INFO_i, v) :
    '''
    # INFO_i : 入力で与えられる情報 [i,x,y,r]
    # v : 四角形の頂点4つ [x1,y1,x2,y2]
    企業広告の四角形で、得点が得られるかを確認する。
    戻り値は、True or False
    '''
    i, x, y, r = map(int, INFO_i)
    x1, y1, x2, y2 = map(int, v)
    if x < x1 : return False
    if x > x2 : return False
    if y < y1 : return False
    if y > y2 : return False
    return True

def getData(boundaryLimits, INFO) :
    '''
    # boundaryLimits : 広告スペースを区切った際の始点と終点 [start_x,start_y,end_x,end_y]
    # INFO : 入力で与えられる情報の束 [i,x,y,r]がN個集まった情報
    # INFO_i : 入力で与えられる情報 [i,x,y,r]

    (区切られた)広告スペースと、入力から、以下の情報を返す。
    0 : 高さに関する情報。これは以下の3つの情報を持つ。
        0 : heightList
            0 : height
            1 : i
        1 : heightCnt
        2 : sameHeight_i
    1 : 幅に関する情報。これは以下の3つの情報を持つ。
        0 : widthList
            0 : width
            1 : i
        1 : widthCnt
        2 : sameWidth_i
    名前が良くない。。。
    '''
    start_x, start_y, end_x, end_y = map(int, boundaryLimits)

    height = [-1]*10000
    heightList = [[start_y - 1,-1]]
    width = [-1]*10000
    widthList = [[start_x - 1,-1]]
    heightCnt = 0
    widthCnt = 0
    sameHeight_i = set()
    sameWidth_i = set()

    for INFO_i in range (len(INFO)):
        i, x, y, r = map(int, INFO[INFO_i])

        if x < start_x or x > end_x : continue
        if y < start_y or y > end_y : continue
        
        if height[y] == -1 :
            height[y] = i
        else :
            sameHeight_i.add(i)
            sameHeight_i.add(height[y])
        # heightList.append(y)
        heightList.append([y,i])
        
        if width[x] == -1 :
            width[x] = i
        else :
            sameWidth_i.add(i)
            sameWidth_i.add(width[x])
        # widthList.append(x)
        widthList.append([x,i])
        
        heightCnt += 1
        widthCnt += 1

    sortedHeightList=sorted(heightList, key = lambda x:x[0])
    sortedWidthList=sorted(widthList, key= lambda y:y[0])
    # heightList.sort()
    # widthList.sort()

    return [[sortedHeightList, heightCnt, sameHeight_i], [sortedWidthList, widthCnt, sameWidth_i]]
    # return [[heightList, heightCnt, sameHeight_i], [widthList, widthCnt, sameWidth_i]]

def calculateArea(v) :
    '''
    # v : 四角形の頂点4つ [x1,y1,x2,y2]
    四角形の面積を求める。
    戻り値は面積の値(int)。
    '''
    x1, y1, x2, y2 = map(int, v)
    w = x2 - x1
    h = y2 - y1
    s = w * h
    return s

def ReduceSize(INFO_i, v, n):
    '''
    サイズを小さくする基本的な機能を有している。
    横縞と縦縞で、この関数をもとに、それぞれ別の関数として作成している。
    # INFO_i : 入力で与えられる情報 [i,x,y,r]
    # v : 四角形の頂点4つ [x1,y1,x2,y2]
    # n : 企業数
    x, y よりも左上にあるX1, y1 を x, y に近づけて得点を得られるvを返す。
    v : [x1,y1,x2,y2]
    '''
    i, x, y, r = map(int, INFO_i)
    x1, y1, x2, y2 = map(int, v)

    w = x2 - x1
    h = y2 - y1

    area = calculateArea(v)

    diff = area - r
    fixVal = min(h, w)
    lengthToCut = diff // fixVal
    if fixVal == h and lengthToCut != 0 :
        temp_x1 = x1 + lengthToCut
        if x < temp_x1 :
            x1 = x
        else :
            x1 = temp_x1
    if fixVal == w and lengthToCut != 0 :
        temp_y1 = y1 + lengthToCut
        if y < temp_y1 :
            y1 = y
        else :
            y1 = temp_y1
    v = [x1, y1, x2, y2]

    return v


def ReduceSize_horizon(INFO_i, v, n):
    '''
    # INFO_i : 入力で与えられる情報 [i,x,y,r]
    # v : 四角形の頂点4つ [x1,y1,x2,y2]
    # n : 企業数
    x, y よりも左上にあるX1, y1 を x, y に近づけて得点を得られるvを返す。
    v : [x1,y1,x2,y2]
    '''
    i, x, y, r = map(int, INFO_i)
    x1, y1, x2, y2 = map(int, v)

    w = x2 - x1
    h = y2 - y1

    area = calculateArea(v)

    diff = area - r
    fixVal = w # 横縞と縦縞に関数を分離　fixValを幅に固定
    lengthToCut = diff // fixVal
    # if fixVal == h and lengthToCut != 0 :
    #     temp_x1 = x1 + lengthToCut
    #     if x < temp_x1 :
    #         x1 = x
    #     else :
    #         x1 = temp_x1
    if fixVal == w and lengthToCut != 0 :
        temp_y1 = y1 + lengthToCut
        if y < temp_y1 :
            y1 = y
        else :
            y1 = temp_y1
    v = [x1, y1, x2, y2]

    return v

def ReduceSize_vertic(INFO_i, v, n):
    '''
    # INFO_i : 入力で与えられる情報 [i,x,y,r]
    # v : 四角形の頂点4つ [x1,y1,x2,y2]
    # n : 企業数
    x, y よりも左上にあるX1, y1 を x, y に近づけて得点を得られるvを返す。
    v : [x1,y1,x2,y2]
    '''
    i, x, y, r = map(int, INFO_i)
    x1, y1, x2, y2 = map(int, v)

    w = x2 - x1
    h = y2 - y1

    area = calculateArea(v)

    diff = area - r
    fixVal = h # 横縞と縦縞に関数を分離　fixValを高さに固定
    lengthToCut = diff // fixVal
    if fixVal == h and lengthToCut != 0 :
        temp_x1 = x1 + lengthToCut
        if x < temp_x1 :
            x1 = x
        else :
            x1 = temp_x1
    # if fixVal == w and lengthToCut != 0 :
    #     temp_y1 = y1 + lengthToCut
    #     if y < temp_y1 :
    #         y1 = y
    #     else :
    #         y1 = temp_y1
    v = [x1, y1, x2, y2]

    return v


def CutExcessPart_horizon(INFO_i, v, boundaryLimits, n) :
    '''
    # INFO_i : 入力で与えられる情報 [i,x,y,r]
    # v : 四角形の頂点4つ [x1,y1,x2,y2]
    # boundaryLimits : 広告スペースを区切った際の始点と終点 [start_x,start_y,end_x,end_y]
    # n : 企業数
    横縞で区切るときにx2をxに近づけて得点が得られるvを返す。
    v : [x1,y1,x2,y2]
    '''
    i, x, y, r = map(int, INFO_i)
    x1, y1, x2, y2 = map(int, v)
    start_x, start_y, end_x, end_y = map(int, boundaryLimits)
    
    w = x2 - x1
    h = y2 - y1

    area = calculateArea(v)


    diff = area - r
    fixVal = h # 横縞と縦縞に関数を分離　fixValを高さに固定
    moveDist = diff // fixVal
    if fixVal == h and moveDist != 0 :
        temp_x2 = end_x - moveDist        
        if x+1 <= temp_x2 :
            x2 = temp_x2
        else :
            x2 = x + 1
        
    if fixVal == w and moveDist !=0 :
        temp_y2 = end_y - moveDist
        if y+1 <= temp_y2 :
            y2 = temp_y2
        else :
            y2 = y + 1
    
    v = [x1, y1, x2, y2]
        
    return v

def CutExcessPart_vertic(INFO_i, v, boundaryLimits, n) :
    '''
    # INFO_i : 入力で与えられる情報 [i,x,y,r]
    # v : 四角形の頂点4つ [x1,y1,x2,y2]
    # boundaryLimits : 広告スペースを区切った際の始点と終点 [start_x,start_y,end_x,end_y]
    # n : 企業数
    縦縞で区切るときにy2をyに近づけて得点が得られるvを返す。
    v : [x1,y1,x2,y2]
    '''
    i, x, y, r = map(int, INFO_i)
    x1, y1, x2, y2 = map(int, v)
    start_x, start_y, end_x, end_y = map(int, boundaryLimits)
    
    w = x2 - x1
    h = y2 - y1

    area = calculateArea(v)

    diff = area - r
    fixVal = w # 横縞と縦縞に関数を分離　fixValを幅に固定
    moveDist = diff // fixVal

    if fixVal == h and moveDist != 0 :
        temp_x2 = end_x - moveDist
        if x+1 <= temp_x2 :
            x2 = temp_x2
        else :
            x2 = x + 1
    
    if fixVal == w and moveDist !=0 :
        temp_y2 = end_y - moveDist
        if y+1 <= temp_y2 :
            y2 = temp_y2
        else :
            y2 = y + 1
    
    v = [x1, y1, x2, y2]

    return v

def compensation_horizon(compensationData_horizon,INFO,horizontalStripesDic,horizontalStripesScore):
    score=horizontalStripesScore
    dic=horizontalStripesDic
    for check_i in range (len(compensationData_horizon)):
        checkIndex=compensationData_horizon[check_i][0]
        if checkIndex==-1:
            continue
        possibleRange=compensationData_horizon[check_i][1]
        r=INFO[checkIndex][3]
        v=dic[checkIndex]
        area=calculateArea(v)

        if area > r :
            continue
        else:
            score -= calculateScore(v,r,len(INFO))
            x1,y1,x2,y2=map(int,v)
            diff= r-area
            w = x2-x1
            moveDist=diff//w
            temp_y2=y2+moveDist
            if temp_y2 > possibleRange:
                y2=possibleRange
                # v = [x1,y1,x2,y2]
            else:
                y2=temp_y2
            v = [x1,y1,x2,y2]
            dic[checkIndex] = v
            score += calculateScore(v,r,len(INFO))

    return [score,dic]



def compensation_vertic (compensationData_vertical,INFO,verticalStripesDic,verticalStripesScore):
    score=verticalStripesScore
    dic=verticalStripesDic
    for check_i in range (len(compensationData_vertical)):
        checkIndex=compensationData_vertical[check_i][0]
        if checkIndex==-1:
            continue
        possibleRange=compensationData_vertical[check_i][1]
        r=INFO[checkIndex][3]
        v=dic[checkIndex]
        area=calculateArea(v)

        # print(0,dic[checkIndex],possibleRange)
        
        if area > r :
            continue
        else:
            score -= calculateScore(v,r,len(INFO))
            x1,y1,x2,y2=map(int,v)
            diff= r- area
            h = y2 -y1
            moveDist=diff//h
            temp_x2=x2+moveDist
            if temp_x2 > possibleRange:
                x2=possibleRange
            else:
                x2=temp_x2
            v = [x1,y1,x2,y2]
            dic[checkIndex] = v
            score += calculateScore(v,r,len(INFO))

        # print(1,dic[checkIndex])

    return [score,dic]



def decideSizeAdsUnderBoundaryLimits(boundaryLimits, INFO) :
    # boundaryLimits : 広告スペースを区切った際の始点と終点 [start_x,start_y,end_x,end_y]
    # INFO : 入力で与えられる情報 [i,x,y,r]
    start_x, start_y, end_x, end_y = map(int, boundaryLimits)
    n = len(INFO)
    horizontalStripesScore = 0
    verticalStripesScore = 0
    horizontalStripesDic = dict()
    verticalStripesDic = dict()

    data = getData(boundaryLimits, INFO)
    heightListData = data[0][0]
    heightList=[]
    heightDic=dict()
    for heightList_i in range (len(heightListData)):
        heightList.append(heightListData[heightList_i][0])
        heightDic[heightListData[heightList_i][0]]=heightListData[heightList_i][1]

    heightCnt = data[0][1]
    sameHeight_i = data[0][2]
    widthListData = data[1][0]
    widthList=[]
    widthDic=dict()
    for widthList_i in range (len(widthListData)):
        widthList.append(widthListData[widthList_i][0])
        widthDic[widthListData[widthList_i][0]]=widthListData[widthList_i][1]
    widthCnt = data[1][1]
    sameWidth_i = data[1][2]

    compensationData_horizon=[]
    compensationData_vertical=[]

    # ここから横縞の計算 主に高さを使用して計算を進める
    for INFO_i in range (n) :
        i, x, y, r = map(int, INFO[INFO_i])
        if x < start_x or x > end_x : continue
        if y < start_y or y > end_y : continue

        if i in sameHeight_i :
            v = [x, y, x+1, y+1]
            horizontalStripesScore += calculateScore(v, r, n)
            horizontalStripesDic[i] = v
            continue

        
        heightOder = heightList.index(y)
        preHeightOder = heightOder -1
        baseOfBorderingOnTop = heightList[preHeightOder]
        x1 = start_x
        y1 = baseOfBorderingOnTop + 1
        x2 = end_x
        y2 = y+1
        v = [x1, y1, x2, y2]
        area = calculateArea(v)

        if r > area and heightOder == heightCnt :
            y2 = end_y
            v = [x1, y1, x2, y2]
        
        # 上側を削る処理
        if area > r :
            y1_before=v[1]
            v = ReduceSize_horizon(INFO[INFO_i], v, n)
            area = calculateArea(v)
            y1_after=v[1]
            if y1_after != y1_before:
                preIndex_INFO_i=heightDic[baseOfBorderingOnTop]
                compensationData_horizon.append([preIndex_INFO_i,y1_after])

        # 左側を削る処理
        if area > r :
            v = ReduceSize(INFO[INFO_i], v, n)
            area = calculateArea(v)

        # 右側を削る処理
        if area > r :
            v = CutExcessPart_horizon(INFO[INFO_i],v,boundaryLimits,n)
            area =calculateArea(v)
        
        horizontalStripesScore += calculateScore(v,r,n)
        horizontalStripesDic[i]= v
    

    # ここから縦縞の計算
    for INFO_i in range (n) :
        i, x, y, r = map(int, INFO[INFO_i])
        if x < start_x or x > end_x : continue
        if y < start_y or y > end_y : continue

        if i in sameWidth_i :
            v = [x, y, x+1, y+1]
            verticalStripesScore += calculateScore(v, r, n)
            verticalStripesDic[i] = v
            continue

        widthOder = widthList.index(x)
        preWidthOder = widthOder -1
        baseOfBorderingOnLeft = widthList[preWidthOder]
        x1 = baseOfBorderingOnLeft + 1
        y1 = start_y
        x2 = x+1
        y2 = end_y
        v = [x1, y1, x2, y2]
        area = calculateArea(v)

        if r > area and widthOder == widthCnt :
            x2 = end_x
            v = [x1, y1, x2, y2]

        # 左側を削る処理
        if area > r :
            x1_before=v[0]
            v = ReduceSize_vertic(INFO[INFO_i], v, n)
            area = calculateArea(v)
            x1_after=v[0]
            if x1_after != x1_before:
                preIndex_INFO_i=widthDic[baseOfBorderingOnLeft]
                compensationData_vertical.append([preIndex_INFO_i,x1_after])

        # 上側を削る処理
        if area > r :
            v = ReduceSize(INFO[INFO_i],v,n)
            area = calculateArea(v)

        # 下側を削る処理
        if area > r :
            v = CutExcessPart_vertic(INFO[INFO_i],v,boundaryLimits,n)
            area = calculateArea(v)

        verticalStripesScore += calculateScore(v,r,n)
        verticalStripesDic[i]= v

    horizontalStripes_after=compensation_horizon(compensationData_horizon,INFO,horizontalStripesDic,horizontalStripesScore)
    horizontalStripesScore=horizontalStripes_after[0]
    horizontalStripesDic=horizontalStripes_after[1]
    verticalStripes_after=compensation_vertic(compensationData_vertical,INFO,verticalStripesDic, verticalStripesScore)
    verticalStripesScore=verticalStripes_after[0]
    verticalStripesDic=verticalStripes_after[1]

    if horizontalStripesScore >= verticalStripesScore:
        score=horizontalStripesScore
        dic=horizontalStripesDic
    else:
        score=verticalStripesScore
        dic=verticalStripesDic

    return [dic,score*10**9]


N=int(input())
INFO=[]
intersectionPoints=[]

for i in range (N):
    x,y,r=map(int,input().split())
    INFO.append([i,x,y,r])
    iP_p=[x+int(r**0.5),y+int(r**0.5)]
    if iP_p[0]>=10000 or iP_p[1]>=10000:
        pass
    else:
        intersectionPoints.append([r,iP_p])
    iP_n=[x-int(r**0.5),y-int(r**0.5)]
    if iP_n[0]<=0 or iP_n[1]<=0:
        pass
    else:
        intersectionPoints.append([r,iP_n])
    sorted_intersectionPoints=sorted(intersectionPoints,reverse=True ,key= lambda x:x[0])
    intersectionPoints=sorted_intersectionPoints[:]


canvas=[0,0,10000,10000]
nomal=decideSizeAdsUnderBoundaryLimits(canvas,INFO)
dic4ans=nomal[0]
score4ans=nomal[1]

for fh_i in range (1,20):
    for fh_j in range (1,20):
        mx=fh_i*500 # x軸の中継地点
        my=fh_j*500 # y軸の中継地点
        a1=decideSizeAdsUnderBoundaryLimits([0,0,mx,my],INFO) # 広告スペースを区切ったときの 左上
        a2=decideSizeAdsUnderBoundaryLimits([ mx+1,0,10000,my],INFO) # 広告スペースを区切ったときの 右上
        a3=decideSizeAdsUnderBoundaryLimits([ 0,my+1,mx,10000],INFO) # 広告スペースを区切ったときの 左下
        a4=decideSizeAdsUnderBoundaryLimits([ mx+1,my+1,10000,10000],INFO) # 広告スペースを区切ったときの 右下
        p=a1[1]+a2[1]+a3[1]+a4[1]
        d=a1[0]
        d.update(a2[0])
        d.update(a3[0])
        d.update(a4[0])
        # print(d)
        if p>score4ans:
            score4ans=p
            dic4ans=dict()
            dic4ans=d

for iP_i in range (len(intersectionPoints)):
    mx=intersectionPoints[iP_i][1][0]
    my=intersectionPoints[iP_i][1][1]
    a1=decideSizeAdsUnderBoundaryLimits([0,0,mx,my],INFO) # 広告スペースを区切ったときの 左上
    a2=decideSizeAdsUnderBoundaryLimits([ mx+1,0,10000,my],INFO) # 広告スペースを区切ったときの 右上
    a3=decideSizeAdsUnderBoundaryLimits([ 0,my+1,mx,10000],INFO) # 広告スペースを区切ったときの 左下
    a4=decideSizeAdsUnderBoundaryLimits([ mx+1,my+1,10000,10000],INFO) # 広告スペースを区切ったときの 右下
    p=a1[1]+a2[1]+a3[1]+a4[1]
    d=a1[0]
    d.update(a2[0])
    d.update(a3[0])
    d.update(a4[0])
    # print(d)
    if p>score4ans:
        score4ans=p
        dic4ans=dict()
        dic4ans=d

# for ans_i in range(N):
#     # print(*dic4ans[ans_i])
#     print(ans_i,dic4ans[ans_i])
#     print(INFO[ans_i])
#     print(r-calculateArea(dic4ans[ans_i]),r>calculateArea(dic4ans[ans_i]))
#     print("-------------------")

for ans_i in range(N):
    print(*dic4ans[ans_i])


'''
23=>198
'''