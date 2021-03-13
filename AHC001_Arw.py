# AtCoder Heuristic Contest 001
# A - AtCoder Ad

from itertools import combinations
from collections import deque

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

def compensation_horizon(compensationData_horizon,INFO,horizontalStripesDic,horizontalStripesScore,heightDic, heightList):
    score=horizontalStripesScore
    dic=horizontalStripesDic
    nextCompensationData_horizon=[]
    
    for check_i in range (len(compensationData_horizon)):
        checkIndex=compensationData_horizon[check_i][0]
        if checkIndex==-1:
            continue
        possibleRange=compensationData_horizon[check_i][1]
        r=INFO[checkIndex][3]
        v=dic[checkIndex]
        area=calculateArea(v)
        #追加項目#######
        y=INFO[checkIndex][2]
        heightOder=heightList.index(y)
        preHeightOder = heightOder -1
        baseOfBorderingOnTop = heightList[preHeightOder]

        ###############
        x1,y1,x2,y2=map(int,v)

        if area > r :
            # pass
            # x1,y1,x2,y2=map(int,v)
            
            h=y2-y1
            temp_y1=y2-1
            temp_y2=y2-1+h
            if temp_y2>possibleRange:
                temp_y2=possibleRange
                temp_y1=possibleRange-h
                if temp_y1>y:
                    temp_y1=y1
                    temp_y2=y2
            else:
                pass
            v=[x1,temp_y1,x2,temp_y2]
            preIndex_INFO_i=heightDic[baseOfBorderingOnTop]
            nextCompensationData_horizon.append([preIndex_INFO_i,v[1]])

            
            dic[checkIndex]=v
            # continue
        else:
            score -= calculateScore(v,r,len(INFO))
            # x1,y1,x2,y2=map(int,v)
            diff= r-area
            w = x2-x1
            moveDist=diff//w
            temp_y2=y2+moveDist
            if temp_y2 >= possibleRange:
                y2=possibleRange
                # v = [x1,y1,x2,y2]
            else:
                y2=temp_y2
            temp_v=[x1,y1,x2,y2]

            if canIGetScore(INFO[checkIndex],temp_v):
                v = temp_v
            else:
                pass
            dic[checkIndex] = v
            score += calculateScore(v,r,len(INFO))

    if len(nextCompensationData_horizon)>0:

        for check_j in range (len(nextCompensationData_horizon)):
            checkIndex=nextCompensationData_horizon[check_j][0]
            if checkIndex==-1:
                continue
            possibleRange=nextCompensationData_horizon[check_j][1]
            r=INFO[checkIndex][3]
            v=dic[checkIndex]
            area=calculateArea(v)
            #追加項目#######
            y=INFO[checkIndex][2]
            heightOder=heightList.index(y)
            preHeightOder = heightOder -1
            baseOfBorderingOnTop = heightList[preHeightOder]
            ###############
            if area > r :
                continue
            else:
                score -= calculateScore(v,r,len(INFO))
                x1,y1,x2,y2=map(int,v)
                diff= r-area
                w = x2-x1
                moveDist=diff//w
                temp_y2=y2+moveDist
                if temp_y2 >= possibleRange:
                    y2=possibleRange
                    # v = [x1,y1,x2,y2]
                else:
                    y2=temp_y2
                temp_v=[x1,y1,x2,y2]

                if canIGetScore(INFO[checkIndex],temp_v):
                    v = temp_v
                else:
                    pass
                dic[checkIndex] = v
                score += calculateScore(v,r,len(INFO))

    return [score,dic]



def compensation_vertic (compensationData_vertical,INFO,verticalStripesDic,verticalStripesScore,widthDic,widthList):
    score=verticalStripesScore
    dic=verticalStripesDic
    nextCompensationData_vertic=[]

    for check_i in range (len(compensationData_vertical)):
        checkIndex=compensationData_vertical[check_i][0]
        if checkIndex==-1:
            continue
        possibleRange=compensationData_vertical[check_i][1]
        r=INFO[checkIndex][3]
        v=dic[checkIndex]
        area=calculateArea(v)
        x=INFO[checkIndex][1]
        widthOder=widthList.index(x)
        preWidthOder= widthOder -1
        baseOfBorderingOnLeft=widthList[preWidthOder]

        # print(0,dic[checkIndex],possibleRange)
        x1,y1,x2,y2=map(int,v)
        
        if area > r :
            w=x2-x1
            temp_x1=x2-1
            temp_x2=x2-1+w
            if temp_x2>possibleRange:
                temp_x2=possibleRange
                temp_x1=possibleRange-w
                # if temp_x1>x:
                #     temp_x1=x1
                #     temp_x2=x2
            else:
                pass
            v=[temp_x1,y1,temp_x2,y2]
            preIndex_INFO_i=widthDic[baseOfBorderingOnLeft]
            nextCompensationData_vertic.append([preIndex_INFO_i,v[0]])

            dic[checkIndex]=v

            # continue
        else:
            score -= calculateScore(v,r,len(INFO))
            diff= r- area
            h = y2 -y1
            moveDist=diff//h
            temp_x2=x2+moveDist
            if temp_x2 >= possibleRange:
                x2=possibleRange
            else:
                x2=temp_x2
            temp_v=[x1,y1,x2,y2]

            if canIGetScore(INFO[checkIndex],temp_v):
                v=temp_v
            else:
                pass

            dic[checkIndex] = v
            score += calculateScore(v,r,len(INFO))

        # print(1,dic[checkIndex])

    if len(nextCompensationData_vertic)>0:
        for check_j in range (len(nextCompensationData_vertic)):
            checkIndex=nextCompensationData_vertic[check_j][0]
            if checkIndex==-1:
                continue
            possibleRange=nextCompensationData_vertic[check_j][1]
            r=INFO[checkIndex][3]
            v=dic[checkIndex]
            area=calculateArea(v)
            x=INFO[checkIndex][1]
            widthOder=widthList.index(x)
            preWidthOder= widthOder -1
            baseOfBorderingOnLeft=widthList[preWidthOder]
            

            # print(0,dic[checkIndex],possibleRange)
            x1,y1,x2,y2=map(int,v)
            if area > r :
                continue
            else:
                score -= calculateScore(v,r,len(INFO))
                diff= r- area
                h = y2 -y1
                moveDist=diff//h
                temp_x2=x2+moveDist
                if temp_x2 >= possibleRange:
                    x2=possibleRange
                else:
                    x2=temp_x2
                temp_v=[x1,y1,x2,y2]

                if canIGetScore(INFO[checkIndex],temp_v):
                    v=temp_v
                else:
                    pass

                dic[checkIndex] = v
                score += calculateScore(v,r,len(INFO))

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

        #OK
        heightOder = heightList.index(y)
        preHeightOder = heightOder -1
        baseOfBorderingOnTop = heightList[preHeightOder]
        x1 = start_x
        y1 = baseOfBorderingOnTop + 1
        x2 = end_x
        y2 = y+1
        v = [x1, y1, x2, y2]
        area = calculateArea(v)

        if heightOder == heightCnt :
                        
            if area<=r:
                v=[x1,y1,x2,end_y]
                area=calculateArea(v)
            if r<area:
                w=x2-x1
                needheight=r//w

                if needheight==0:
                    needheight+=1
                if needheight>=(end_y-y):
                    temp_y1=end_y-needheight
                    if temp_y1<baseOfBorderingOnTop+1:
                        v=[x1,baseOfBorderingOnTop+1,end_x,end_y]
                    else:
                        v=[x1,temp_y1,x2,end_y]
                        preIndex_INFO_i=heightDic[baseOfBorderingOnTop]
                        compensationData_horizon.append([preIndex_INFO_i,v[1]])
                else:
                    v=[x1,y,x2,y+needheight]
                    preIndex_INFO_i=heightDic[baseOfBorderingOnTop]
                    compensationData_horizon.append([preIndex_INFO_i,v[1]])

                    area=calculateArea(v)
                    if area >r:
                        diff= area-r
                        moveD=diff//(y2-y1)
                        if moveD==(x2-x1):
                            moveD=1
                        temp_x1=x1+moveD
                        if temp_x1<x:
                            x1=x
                            x2=x2-moveD+x
                        else:
                            x1=temp_x1
                        v=[x1,y1,x2,y2]

        else:
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
        if canIGetScore(INFO[INFO_i],v):
            # if i==42 and heightCnt==heightOder and calculateArea(v)<r:print(7,v)

            horizontalStripesScore += calculateScore(v,r,n)
        else:
            x1 = start_x
            y1 = baseOfBorderingOnTop + 1
            x2 = end_x
            y2 = y+1
            v = [x1, y1, x2, y2]
        
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

        if widthOder == widthCnt :

            if area<=r:
                v=[x1,y1,end_x,y2]
                area=calculateArea(v)
            if r<area:
                h=y2-y1
                needwidth=r//h

                if needwidth==0:
                    needwidth+=1
                if needwidth>=(end_x-x):
                    temp_x1=end_x-needwidth
                    if temp_x1<baseOfBorderingOnLeft+1:
                        v=[baseOfBorderingOnLeft+1,y1,end_x,end_y]
                    else:
                        v=[temp_x1,y1,end_x,y2]
                        preIndex_INFO_i=widthDic[baseOfBorderingOnLeft]
                        compensationData_vertical.append([preIndex_INFO_i,v[0]])
                else:
                    v=[x,y1,x+needwidth,y2]
                    preIndex_INFO_i=widthDic[baseOfBorderingOnLeft]
                    compensationData_vertical.append([preIndex_INFO_i,v[0]])

                    area=calculateArea(v)
                    if area >r :
                        diff = area -r
                        moveD=diff//(y2-y1)
                        if moveD==(y2-y1):
                            moveD=1
                        temp_y1=y1+moveD
                        if temp_y1<y:
                            y1=y
                            y2=y2-moveD+y
                        else:
                            y1=temp_y1
                        v=[x1,y1,x2,y2]

        else:
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
            
        if canIGetScore(INFO[INFO_i],v):
            verticalStripesScore += calculateScore(v,r,n)
        else:
            x1 = baseOfBorderingOnLeft + 1
            y1 = start_y
            x2 = x+1
            y2 = end_y
            v = [x1, y1, x2, y2]
        verticalStripesDic[i]= v


    horizontalStripes_after=compensation_horizon(compensationData_horizon,INFO,horizontalStripesDic,horizontalStripesScore,heightDic, heightList)
    horizontalStripesScore=horizontalStripes_after[0]
    horizontalStripesDic=horizontalStripes_after[1]
    verticalStripes_after=compensation_vertic(compensationData_vertical,INFO,verticalStripesDic, verticalStripesScore,widthDic,widthList)
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
twoPoints=[]

for i in range (N):
    x,y,r=map(int,input().split())
    INFO.append([i,x,y,r])
    iP_p=[x+int(r**0.5),y+int(r**0.5)]
    twoPoints.append([r,[x,y]])
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
# print(000,score4ans)

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
            # print(111,fh_i,fh_j,score4ans)

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
        # print(222,iP_i,score4ans)

for fivesec_i in range (1,20):
    for fivesec_j in range (1,20):
        point_i=[500*fivesec_i,500*fivesec_i]
        point_j=[10000-180*fivesec_j,10000-150*fivesec_j]
        left_up=[min(point_i[0],point_j[0]),min(point_i[1],point_j[1])]
        right_dow=[max(point_i[0],point_j[0]),max(point_i[1],point_j[1])]
        a0=decideSizeAdsUnderBoundaryLimits([left_up[0]+1,left_up[1]+1,right_dow[0],right_dow[1]],INFO)
        a1=decideSizeAdsUnderBoundaryLimits([0,0,right_dow[0],left_up[1]],INFO) # 広告スペースを区切ったときの 左上
        a2=decideSizeAdsUnderBoundaryLimits([ right_dow [0]+1,0,10000,right_dow[1]],INFO) # 広告スペースを区切ったときの 右上
        a3=decideSizeAdsUnderBoundaryLimits([ 0,left_up[1]+1 ,left_up[0],10000],INFO) # 広告スペースを区切ったときの 左下
        a4=decideSizeAdsUnderBoundaryLimits([ left_up[0]+1,right_dow[1]+1,10000,10000],INFO) # 広告スペースを区切ったときの 右下
        p=a0[1]+a1[1]+a2[1]+a3[1]+a4[1]
        d=a0[0]
        d.update(a1[0])
        d.update(a2[0])
        d.update(a3[0])
        d.update(a4[0])
        # print(d)
        if p>score4ans:
            score4ans=p
            dic4ans=dict()
            dic4ans=d
            # print(333,fivesec_i,fivesec_j,score4ans)

if N>2:
    sortedTwoPoints=sorted(twoPoints, reverse=True, key = lambda x : x[0])
    numOfSelectPoint=min(45,N)
    sortedTwoPoints = sortedTwoPoints[:numOfSelectPoint]
    tp=list(combinations(sortedTwoPoints,2))
    for tp_i in range (len(tp)):
        p_i=tp[tp_i][0][1]
        p_j=tp[tp_i][1][1]
        if abs(p_i[0]-p_j[0])<10 or abs(p_i[0]-p_j[1])<10 or abs(p_i[1]-p_j[1])<10 or abs(p_i[1]==p_j[0])<10 :
            continue
        else:
            left_up=[min(p_i[0],p_j[0]),min(p_i[1],p_j[1])]
            right_dow=[max(p_i[0],p_j[0]),max(p_i[1],p_j[1])]
            a0=decideSizeAdsUnderBoundaryLimits([left_up[0]+1,left_up[1]+1,right_dow[0],right_dow[1]],INFO)
            a1=decideSizeAdsUnderBoundaryLimits([0,0,right_dow[0],left_up[1]],INFO) # 広告スペースを区切ったときの 左上
            a2=decideSizeAdsUnderBoundaryLimits([ right_dow [0]+1,0,10000,right_dow[1]],INFO) # 広告スペースを区切ったときの 右上
            a3=decideSizeAdsUnderBoundaryLimits([ 0,left_up[1]+1 ,left_up[0],10000],INFO) # 広告スペースを区切ったときの 左下
            a4=decideSizeAdsUnderBoundaryLimits([ left_up[0]+1,right_dow[1]+1,10000,10000],INFO) # 広告スペースを区切ったときの 右下
            p=a0[1]+a1[1]+a2[1]+a3[1]+a4[1]
            d=a0[0]
            d.update(a1[0])
            d.update(a2[0])
            d.update(a3[0])
            d.update(a4[0])
            # print(d)
            if p>score4ans:
                score4ans=p
                dic4ans=dict()
                dic4ans=d
                # print(444,p_i,p_j,score4ans)
if N>2:
    sortedTwoPoints=sorted(twoPoints, key = lambda x : x[0])
    numOfSelectPoint=min(45,N)
    sortedTwoPoints = sortedTwoPoints[:numOfSelectPoint]
    tp=list(combinations(sortedTwoPoints,2))
    for tp_i in range (len(tp)):
        p_i=tp[tp_i][0][1]
        p_j=tp[tp_i][1][1]
        if abs(p_i[0]-p_j[0])<10 or abs(p_i[0]-p_j[1])<10 or abs(p_i[1]-p_j[1])<10 or abs(p_i[1]==p_j[0])<10 :
            continue
        else:
            left_up=[min(p_i[0],p_j[0]),min(p_i[1],p_j[1])]
            right_dow=[max(p_i[0],p_j[0]),max(p_i[1],p_j[1])]
            a0=decideSizeAdsUnderBoundaryLimits([left_up[0]+1,left_up[1]+1,right_dow[0],right_dow[1]],INFO)
            a1=decideSizeAdsUnderBoundaryLimits([0,0,right_dow[0],left_up[1]],INFO) # 広告スペースを区切ったときの 左上
            a2=decideSizeAdsUnderBoundaryLimits([ right_dow [0]+1,0,10000,right_dow[1]],INFO) # 広告スペースを区切ったときの 右上
            a3=decideSizeAdsUnderBoundaryLimits([ 0,left_up[1]+1 ,left_up[0],10000],INFO) # 広告スペースを区切ったときの 左下
            a4=decideSizeAdsUnderBoundaryLimits([ left_up[0]+1,right_dow[1]+1,10000,10000],INFO) # 広告スペースを区切ったときの 右下
            p=a0[1]+a1[1]+a2[1]+a3[1]+a4[1]
            d=a0[0]
            d.update(a1[0])
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

# print(score4ans)

for ans_i in range(N):
    print(*dic4ans[ans_i])
    # if ans_i==42:
    #     print(dic4ans[ans_i])


'''
23=>198
'''