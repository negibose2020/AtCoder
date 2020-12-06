# AtCoder Beginner Contest 116
# B - Collatz Problem

s=int(input())

ls=[s]
ls2=[0]*30001000
ls2[s+1]=1
for i in range (1,1000010):
# for i in range (1,10):
    if ls[-1]%2==0:
        _=ls[-1]//2
        ls.append(_)
        if ls2[_+1]>0:
            print(i+1)
            exit()
        ls2[_+1]+=1
    else:
        _=3*ls[-1]+1
        ls.append(_)
        if ls2[_+1]>0:
            print(i+1)
            exit()
        ls2[_+1]+=1

# print(ls)