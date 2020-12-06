# AtCoder Beginner Contest 122
# B - ATCoder

S=input()

ans=0

temp=0
for i in range (len(S)):
    if S[i]=="A" or S[i]=="C" or S[i]=="G" or S[i]=="T":
        temp+=1
    else:
        if temp>ans:
            ans=temp
        temp=0
else:
    if temp>ans:
        ans=temp

print(ans)