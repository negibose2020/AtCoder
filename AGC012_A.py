N=int(input())
ai=list(map(int,input().split()))
l1=sorted(ai,reverse=True)

l2=l1[1::2]
ans=l2[:N]
print(sum(ans))
