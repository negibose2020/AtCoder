# AtCoder Beginner Contest 134
# C - Exception Handling

N=int(input())
ls = []
lsmax=0
lsmaxnum=1
lsmax2=0
for i in range (N):
    a=int(input())
    ls.append(a)
    if a==lsmax:
        if lsmaxnum==1:
            pass
        else:
            lsmaxnum+=1
    if a>lsmax:
        lsmax=a
if lsmaxnum==1:
    ls2=sorted(ls)
    lsmax2=ls2[-2]

# print(lsmax,lsmax2,lsmaxnum)

for j in range (N):
    if ls[j]==lsmax:
        if lsmaxnum>1:
            print(lsmax)
        else:
            print(lsmax2)
    else:
        print(lsmax)