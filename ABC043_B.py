s=list(input())

ans=[]

for i in range (len(s)):
    if s[i]=="0" or s[i]=="1":
        ans.append(s[i])
    else:
        if len(ans)==0:
            pass
        else:
            ans.pop()

print("".join(ans))
