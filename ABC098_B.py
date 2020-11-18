N=int(input())
S=input()

ans=0

for i in range(1,N):
    X=S[:i]
    Y=S[i:]
    setX=set(X)
    setY=set(Y)
    intersectionXY=setX & setY
    _temp=len(intersectionXY)
    if _temp>ans:
        ans=_temp
    else:
        pass
print(ans)


# set 積集合