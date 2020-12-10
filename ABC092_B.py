# AtCoder Beginner Contest 092
# B - Chocolate

N=int(input())
D,X=map(int,input().split())
A=[]
C=[]
for i in range (N):
    a=int(input())
    day=0
    hoge=day*a+1
    c=0
    while hoge<=D:
        c+=1
        day+=1
        hoge=day*a+1
    else:
        A.append(a)
        C.append(c)
print(sum(C)+X)