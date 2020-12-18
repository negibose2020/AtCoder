N,M=map(int,input().split())
X=list(map(int,input().split()))

if N>=M:
    print(0)
    exit()

X.sort()
# dist=[]
dist2=[]
for i in range (1,M):
    d=abs(X[i-1]-X[i])
    # dist.append([d,i])
    dist2.append(d)
# print(X)
# dist=sorted(dist,reverse=True)
dist2=sorted(dist2,reverse=True)[N-1:]
# print(dist)
print(sum(dist2))


# ans=0
# span=[0]*(M+1)

# for i in range (N-1):
#     s=dist[i][1]
#     span[s]=1
# # print(span)

# temp=0
# for j in range (M-1):
#     if span[j+1]==1:
#         ans+=temp
#         temp=0
#     else:
#         temp+=abs(X[j]-X[j+1])
# else:
#     ans+=temp

# print(ans)