# AtCoder Beginner Contest 175
# A - Rainy Season

S=input()

ans=0

for i in range (len(S)):
    if S[i]=="R":
        tempans=1
        for j in range (i+1,len(S)):
            if S[i]==S[j]:
                tempans+=1
            else:
                if tempans>ans:
                    ans=tempans
                break
        else:
            if tempans>ans:
                ans=tempans
print(ans)