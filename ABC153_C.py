N,K=map(int,input().split())
h=list(map(int,input().split()))

H=sorted(h,reverse=True)
if K>=N:
    print(0)
    exit()

Ans=H[K:]
print(sum(Ans))