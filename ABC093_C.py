# ABC093 C - Same Integers

def is_eaven(n):
    if n%2==0:
        return 1
    else:
        return 0

L=list(map(int,input().split()))

ans=0

tempL=[]

if L[0]==L[1]==L[2]:
    print(ans)
    exit()

for l in L:
    tempL.append(is_eaven(l))
if all (tempL) or not any(tempL):   #全て偶数or全て奇数の場合はpass
    pass
elif tempL.count(0)==2:
    for i in range (2):
        if tempL[i]==0:
            L[i]+=1
    ans+=1
elif tempL.count(1)==2:
    for i in range (2):
        if tempL[i]==1:
            L[i]+=1
    ans+=1
else:
    pass

if L[0]==L[1]==L[2]:
    print(ans)
    exit()

L.sort()

ans+=(L[2]-L[0])//2

if L[0]==L[1]==L[2]:
    print(ans)
    exit()

ans+=(L[2]-L[1])//2
print(ans)