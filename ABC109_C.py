import math

N,X=map(int,input().split())
x=list(map(int,input().split()))
x.append(X)
x.sort()

if N==1:
    print(x[1]-x[0])
    exit()

ans=math.gcd(x[1]-x[0],x[2]-x[1])

for i in range (1,N+1):
    ans=math.gcd(ans,x[i]-x[i-1])

print(ans)