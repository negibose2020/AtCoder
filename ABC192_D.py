# SOMPO HD プログラミングコンテスト2021(AtCoder Beginner Contest 192)
# D - Base n

def is_ok(num):
    a=henkan(Xlist,num,M)
    if a<=M:
        return True
    else:
        return False

def megru_bisect(ok,ng):
    while(abs(ok-ng)>1):
        mid=(ok+ng)//2
        if is_ok(mid):
            ok=mid
        else:
            ng=mid
    return ok


def henkan(list,base,M):
    l=len(list)
    ans=0
    for i in range(l):
        ans+=list[i]*(base**(l-1-i))
    return ans

X=input()
M=int(input())
Xlist=list(map(int,X))
d=max(Xlist)

if len(X)==1:
    if henkan(Xlist, d+1,M)<=M:
        print(1)
        exit()
    else:
        print(0)
        exit()


ans=megru_bisect(d,10**18+2)

print(ans-d)