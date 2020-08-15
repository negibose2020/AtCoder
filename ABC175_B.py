# AtCoder Beginner Contest 175
# B - Making Triangle

N=int(input())
L=list(map(int,input().split()))

ans=0

for i in range (N):
    for j in range (i+1,N):
        for k in range (j+1,N):
            a=min(L[i],L[j],L[k])
            c=max(L[i],L[j],L[k])
            b=(L[i]+L[j]+L[k]-a-c)
            if a+b>c and a<b<c:
                ans+=1

print(ans)