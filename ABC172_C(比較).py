def ABC172_C():

    import time
    import random


    O_N=random.randint(1,200000)
    O_M=random.randint(1,200000)
    O_K=random.randint(1,10**9)
    LIST_A=[random.randint(1,O_K//100) for i in range (O_N)]
    LIST_B=[random.randint(1,O_K//100) for i in range (O_M)]

    '''
    ↑↑問題設定↑↑
    ----------------------------
    ↓↓二分探索↓↓
    '''
    N=O_N
    M=O_M
    K=O_K
    list_a=LIST_A
    list_b=LIST_B

    start1=time.time()

    import bisect


    totaltime_a=[0]
    for a in list_a:
        temp_a=totaltime_a[-1]+a
        if temp_a>K:
            break
        else:
            totaltime_a.append(temp_a)

    totaltime_b=[0]
    for b in list_b:
        totaltime_b.append(totaltime_b[-1]+b)

    ans1=0

    # laptimelist1=[]

    for i in range (len(totaltime_a)):
        # laptime_start=time.time()   #for文タイム計測
        Kb=K-totaltime_a[i]
        j=bisect.bisect_right(totaltime_b,Kb)-1
        if i+j>ans1:
            ans1=i+j
            BOOK_A=i
            BOOK_B=j
        else:
            pass
        # laptime_finish=time.time()  #for文タイム計測
        # laptimelist1.append(laptime_finish-laptime_start)

    # print(ans1)

    process_time1 = time.time() - start1
    # print(laptimelist1)
    # print(process_time1)

    '''
    ↑↑二分探索↑↑
    ----------------------------
    ↓↓配列操作↓↓
    '''
    N=O_N
    M=O_M
    K=O_K
    alist=LIST_A
    blist=LIST_B

    start2=time.time()

    A_total=[0]

    for a in alist:
        _a=A_total[-1]+a
        if _a>K:
            break
        else:
            A_total.append(_a)

    B_total=[0]
    for b in blist:
        B_total.append(B_total[-1]+b)

    ans2=0
    # laptimelist2=[]

    for i in range (len(A_total)):
        # laptime_start=time.time()   #for文タイム計測
        Kb=K-A_total[i]
        temp_Btotal=B_total
        temp_Btotal.append(Kb)
        temp_Btotal.sort()
        j=temp_Btotal.index(Kb)-1
        if temp_Btotal.count(Kb)==2:
            j+=1
        if i+j>ans2:
            ans2=i+j
        # laptime_finish=time.time()  #for文タイム計測
        # laptimelist2.append(laptime_finish-laptime_start)

    # print(ans2)

    process_time2 = time.time() - start2

    # print(laptimelist2)
    # print(process_time2)


    return '0',O_N,O_M,O_K,ans1,process_time1,ans2,process_time2,'0'




print('_,{0},{1},{2},{3},{4},{5},{6},_'.format('N','M','K','ans1','time1','ans2','time2'))
for i in range(1000):
    a=ABC172_C()
    print(a)