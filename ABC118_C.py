# def f(sortedlist):
#     if len(sortedlist)==1:
#         return sortedlist[0]
#     else:
#         newls=[sortedlist[0]]
#         for i in range(1,len(sortedlist)):
#             a=sortedlist[i]%sortedlist[0]
#             if a==0:
#                 continue
#             else:
#                 newls.append(a)
#         newls.sort()
#         return f(newls)

# N=int(input())
# A=list(map(int,input().split()))

# A.sort()

# print(f(A))

import math

N=int(input())
A=list(map(int,input().split()))
ans=A[0]
for i in range (N):
    ans=math.gcd(ans,A[i])
print(ans)