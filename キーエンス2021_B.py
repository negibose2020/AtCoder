import collections

n,k=map(int,input().split())
a=list(map(int,input().split()))

C=collections.Counter(a)
# print(C)
ans=0

for i in range (len(C)):
    # print(C[i])
    if C[i]==0:
        break

    if C[i]>=k:
        ans+=k
    
    if 0<C[i]<k:
        k=C[i]
        ans+=k
    # print(i,ans,k)
print(ans)