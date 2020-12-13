# AtCoder Beginner Contest 118
# B - Foods Loved by Everyone

N,M=map(int,input().split())

ls=[0]*(M+1)
for i in range(N):
    k=list(map(int,input().split()))
    for j in range (1,k[0]+1):
        ls[k[j]]+=1
    # print(ls)
ans=0
for i in range (len(ls)):
    if ls[i]==N:
        ans+=1
# print(ls)
print(ans)