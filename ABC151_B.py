N,K,M=map(int,input().split())
a=list(map(int,input().split()))

if (sum(a)+K)/N<M:
    print(-1)
    exit()
else:
    ans=N*M-sum(a)
    if ans <0 :
        print(0)
    else:
        print(ans)