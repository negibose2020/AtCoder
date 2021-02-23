# AtCoder Beginner Contest 189
# C - Mandarin Orange

N=int(input())
A=list(map(int,input().split()))

ans=max(A)

for i in range (N):
    h=A[i]
    for j in range (i,N):
        h=min(h,A[j])
        ans=max(ans,(j-i+1)*h)

print(ans)