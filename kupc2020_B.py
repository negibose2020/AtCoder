# 京都大学プログラミングコンテスト 2020
# B - Numbers on Papers

※解けない！！

import bisect

mod=10**9+7

N,K=map(int,input().split())
vls=[]
for _ in range (N):
    v=list(map(int,input().split()))
    vls.append(v)
# print(vls)

ans=0

for i in range (K):
    print(i)
    a=vls[0][i]
    # print(a)
    templs=[]
    for j in range (1,N):
        print(a,vls[j],K-(bisect.bisect_left(vls[j],a)))
        templs.append(K-(bisect.bisect_left(vls[j],a)))
        # ans*=bisect.bisect_left(vls[j],a)
        # ans%=mod
        if  K-(bisect.bisect_left(vls[j],a))==0:
            a=1000000000+1
        else:
            a=vls[j][bisect.bisect_left(vls[j],a)]
    tempnum=1
    print(templs)
    for k in range(len(templs)):
        tempnum*=templs[k]
        tempnum%=mod
        print(tempnum)
    ans+=tempnum
    print(ans)

ans%=mod

print(ans)