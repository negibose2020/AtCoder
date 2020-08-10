# AtCoder Regular Contest 099
# C - Minimization 
N,K =map(int,input().split())
A=list(map(int,input().split()))

ans=0

a=N-K
ans+=1

while a>0:
    a+=1
    ans+=1
    a=a-K
print(ans)