import collections

N=int(input())
a=list(map(int,input().split()))

C=list(collections.Counter(a).most_common())
ans=0
for i in range (len(C)):
    k=C[i][0]
    v=C[i][1]
    # print(C[i],k,v)
    if k==v:
        continue
    if k>v:
        ans+=v
        continue
    if k<v:
        ans+=v-k
        continue

# print(C)
print(ans)