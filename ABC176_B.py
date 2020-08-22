# AtCoder Beginner Contest 176
# B - Multiple of 9

N=input()
ls=list(map(int,N))

lssum=sum(ls)
if lssum%9==0:
    print('Yes')
else :
    print('No')