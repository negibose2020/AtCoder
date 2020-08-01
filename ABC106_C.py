# AtCoder Beginner Contest 106
# C - To Infinity

S=input()
K=int(input())

whileone=-1
ans=-1
for i in range (len(S)):
    if S[i]=="1":
        whileone=i+1
    else:
        ans=S[i]
        break

if whileone>0 and whileone>=K:
    print(1)
else:
    print(ans)