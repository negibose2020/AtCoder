# AtCoder Beginner Contest 132
# B - Ordinary Number

n=int(input())
pls=list(map(int,input().split()))

ans=0

for i in range (n-2):
    a=pls[i]
    b=pls[i+1]
    c=pls[i+2]
    if a<b<c or c<b<a:
        ans+=1

print(ans)