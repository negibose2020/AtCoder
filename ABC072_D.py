N=int(input())
p=list(map(int,input().split()))

ans=0

pre=False

for i in range (N):
    # print("start:{}:{}".format(i+1,pre))
    if p[i]==i+1:
        if pre==True:
            pre=False
            continue
        else:
            ans+=1
            pre=True
            # print(i+1,pre)
            continue
    pre=False
print(ans)

