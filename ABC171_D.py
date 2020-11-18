from collections import Counter

N=int(input())
A=list(map(int,input().split()))
c=Counter(A)
commons=c.most_common()

ans=0

dic={}
for common in commons:
    dic[common[0]]=common[1]
    ans+=common[0]*common[1]
# print(dic)
# print(ans)

Q=int(input())
for i in range(Q):
    b,c=map(int,input().split())
    if b not in dic:
        print(ans)
        continue
    else:
        pass
    if c not in dic:
        ans+=(c-b)*dic[b]
        print(ans)
        dic[c]=dic[b]
        dic[b]=0
        continue
    else:
        pass
    ans+=(c-b)*dic[b]
    dic[c]+=dic[b]
    dic[b]=0
    print(ans)
