# 第五回 アルゴリズム実技検定
# F - 一触即発

def is_bomb(p,conditions):
    for i in range (len(conditions)):
        res=0
        c1=conditions[i][0]
        c2=conditions[i][1]
        c3=conditions[i][2]
        if p[c1]==1:res+=1
        if p[c2]==1:res+=1
        if p[c3]==1:res+=1
        if res==3:
            return True
        else:
            continue
    return False


N,M=map(int,input().split())
conditions=[]
for _ in range (M):
    a,b,c=list(map(int,input().split()))
    a-=1
    b-=1
    c-=1
    conditions.append([a,b,c])

ans=0

for i in range(2**N):
    P=[]
    for j in range(N):
        if i>>j & 1 ==1:
            P.append(1)
        else:
            P.append(0)

    if is_bomb(P,conditions):
        continue
    else:
        temp=0
        PP=P[:]
        for k in range (N):
            if PP[k]==1:
                continue
            else:
                PP[k]=1
            if is_bomb(PP,conditions):
                temp+=1
                PP=P[:]
            else:
                PP=P[:]
                continue
        ans=max(ans,temp)

print(ans)