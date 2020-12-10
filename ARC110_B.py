# 鹿島建設プログラミングコンテスト2020（AtCoder Regular Contest 110）
# B - Many 110

def check1(N,T):
    if N==1 and T=="0":
        return 10**10
    if N==1 and T=="1":
        return 2*10**10
    return False

def check2(N,T):
    if N==2 and T=="00":
        return 0
    if N==2 and T=="01":
        return 10**10-1
    if N==2 and T=="10":
        return 10**10
    if N==2 and T=="11":
        return 10**10
    return False

def check3(N,T):
    if N==3 and T=="110":
        return 10**10
    if N==3 and T=="101":
        return 10**10-1
    if N==3 and T=="011":
        return 10**10-1
    return False

def check4(N,T):
    if T[:3]=="110":
        t="110"
        for i in range (3,N):
            if T[i]==t[i%3]:
                continue
            else:
                return 0
        if N%3==0:
            return 10**10-(N//3)+1
        else:
            return 10**10-(N//3)
    elif T[:3]=="101":
        t="101"
        # for i in range (3,N):
        #     if T[i%3]==t[i%3]:
        #         continue
        #     else:
        #         return 0
        # else:
        #     return int(10*10-(N//3)-1)

    elif T[:3]=="011":
        t="011"
        for i in range (3,N):
            if T[i]==t[i%3]:
                continue
            else:
                return 0
        if N%3==2:
            return 10**10-(N//3)-1
        else:
            return 10**10-(N//3)
    else:
        return 0
    for i in range (3,N):
        if T[i]==t[i%3]:
            continue
        else:
            return 0
    # if T[-1]=="1" and T[-2]=="0" and T[-3]=="1":
    #     return 10**10-(N//3)-1
    
    return 10**10-(N//3)


N=int(input())
T=input()

ans=0

a=check1(N,T)
if a:
    ans=a
b=check2(N,T)
if b:
    ans=b
c=check3(N,T)
if c:
    ans=c
d=check4(N,T)
if d:
    ans=d

print(ans)
