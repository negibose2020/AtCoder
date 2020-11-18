N=int(input())
Qlist=[]
ans=0
for i in range (N):
    s=int(input())
    ans+=s
    Qlist.append(s)
if ans%10==0:
    Qlist.sort()
    for j in range(N):
        temp=ans-Qlist[j]
        if temp%10==0:
            continue
        else:
            ans=temp
            break
    else:
        ans=0
else:
    pass
print(ans)