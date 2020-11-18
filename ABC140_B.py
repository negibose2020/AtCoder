N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

ans=0

for i in range (N):
    ans+=B[A[i]-1]

for j in range(1,N):
    if A[j]==A[j-1]+1:
        ans+=C[A[j]-2]

print(ans)