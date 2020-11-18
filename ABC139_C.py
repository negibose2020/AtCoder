N=int(input())
Hi=list(map(int,input().split()))

# ans=[0]*N

# for i in range (N):
#     a=0
#     # if Hi[i]<Hi[i-1]:
#     #     continue
#     for j in range(N-i-1):
#         if Hi[i+j]>=Hi[i+j+1]:
#             a+=1
#         else:
#             break
#     ans[i]=a

# print(max(ans))

ans=0
temp=0

for i in range(1,N):
    if Hi[i]<=Hi[i-1]:
        temp+=1
    else:
        if temp>ans:
            ans=temp
        else:
            pass
        temp=0
else:
    if temp>ans:
        ans=temp

print(ans)