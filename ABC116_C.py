def f(ls,mini):
    # print(ls)
    if max(ls)==mini:
        ans.append(mini)
        return 

    # 答えに最小の高さを足す。
    # 各要素の高さを最小値分引く。
    ans.append(mini)
    for i in range (len(ls)):
        ls[i]-=mini
    
    # 高さ>0の間は一緒に水やりできるため、連続区間を取っていき、2次元配列とする。
    li=[]
    sls=[]
    for j in range (len(ls)):
        if ls[j]>0:
            sls.append(ls[j])
        else:
            if len(sls)>0:
                li.append(sls)
            sls=[]
    else:
        if len(sls)>0:
            li.append(sls)

    # 上記の二次元配列を再起関数に入れる
    for k in range (len(li)):
        f(li[k],min(li[k]))


N=int(input())
h=list(map(int,input().split()))
ans=[]

f(h,min(h))

print(sum(ans))