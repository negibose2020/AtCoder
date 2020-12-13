# AtCoder Beginner Contest 123
# B - Five Dishes

A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())

ls1=[]
ls2=[[0] for i in range(10)]
abcde=[A,B,C,D,E]
for _ in abcde:
    mod=_%10
    if mod==0:
        ls1.append(_)
    else:
        ls2[mod].append(_)

ls2=ls2[::-1]

ans=0
count=0
for _ in ls1:
    ans+=_
    count+=1
for i in range (10):
    for j in range (1,len(ls2[i])):
        if count<4:
            t=(ls2[i][j]//10)
            if t==0:
                ans+=10
                count+=1
            else:
                ans+=t*10+10
                count+=1
        else:
            ans+=ls2[i][j]
    # print(count,ans)
# print(ls1)
# print(ls2)
print(ans)