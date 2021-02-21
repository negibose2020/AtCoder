# SOMPO HD プログラミングコンテスト2021(AtCoder Beginner Contest 192)
# D - Base n

def henkan(list,base,M):
    l=len(list)
    ans=0
    for i in range(l):
        ans+=list[i]*(base**(l-1-i))
        if ans>M:
            return False
    if ans in ansset:
        return False
    else:
        ansset.add(ans)
    return True

X=input()
M=int(input())
Xlist=list(map(int,X))
d=max(Xlist)

ansset=set()

ans=0
i=d+1

while henkan(Xlist,i,M)==True:
    ans+=1
    i+=1
print(ans)