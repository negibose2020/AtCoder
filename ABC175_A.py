# AtCoder Beginner Contest 175
# A - Rainy Season

S=input()

ans=0
count=0

if S[0]=="R":
    count=1

for i in range (1,len(S)):
    if S[i]=="R":
        if count>0:
            pass
        else:
            count=1
        if S[i-1]=="R":
            count+=1
        else:
            if count>ans:
                ans=count
                count=0
else:
    if count>ans:
        ans=count

print(ans)