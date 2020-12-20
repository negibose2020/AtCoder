N=int(input())
p=list(map(int,input().split()))

ans=0

if p[0]==1 and p[1]==2:
    pre=True
else:
    pre=False

for i in range (N):
    if p[i]==i+1:
        if pre==True:
            pre=False
            pass
        else:
            ans+=1
            # print(i+1)
            pre=True
    pre=False
print(ans)

