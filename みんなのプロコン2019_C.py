K,A,B=map(int,input().split())
if 1+K<=A or B-A<=2:
    print(K+1)
    exit()
else:
    ans=A
    cnt=(K+1-A)//2
    ans+=cnt*(B-A)
    if (K+1-A)%2==1:
        ans+=1
    print(ans)
