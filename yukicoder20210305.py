# # N=int(input())
# # if N<=0:print(0)
# # else:
# #     print(N//100)

# n=int(input())
# ls=list(map(int,input().split()))
# ls.sort()

# ans=0

# i=0
# while len(ls)>0:
#     a=2**i
#     # print(i,ls)
#     while a>0:
#         # print(ls,i,a)
#         if len(ls)==0:
#             break
#         ans+=ls.pop()*i
#         a-=1
#     else:
#         i+=1

# print(ans)

