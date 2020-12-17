import collections

N,K=map(int,input().split())
A=list(map(int,input().split()))

ans=0

C=collections.Counter(A).most_common()
# print(C)
if len(C)<=K:
    print(0)
    exit()
for i in range (len(C)-K):
    a=C.pop()
    ans+=a[1]

    # print(a)
# print(C[0])
print(ans)