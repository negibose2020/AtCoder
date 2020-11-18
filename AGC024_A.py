# AtCoder Grand Contest 024
# A - Fairness

a,b,c,k=map(int,input().split())

if k%2==0:
    print(a-b)
else:
    print(b-a)

# alist=[a]
# blist=[b]
# clist=[c]

# for i in range (k):
#     alist.append(blist[-1]+clist[-1])
#     blist.append(alist[-2]+clist[-1])
#     clist.append(blist[-2]+alist[-2])

# print(alist)
# print(blist)
# print(clist)