# AtCoder Beginner Contest 185
# D - Stamp

N,M=map(int,input().split())
A=[0]
a=list(map(int,input().split()))
a.append(N+1)
A.extend(a)
k=10**9+7
ans=0
A.sort()

# print(A)

for i in range (M+1):
    r=A[i+1]-A[i]-1
    if r==0:
        continue
    if k>r:
        k=r

for j in range (M+1):
    r=A[j+1]-A[j]-1
    if r==0:
        continue
    s=r%k
    if s==0:
        ans+=r//k
    else:
        ans+=r//k + 1
# print(k)
print(ans)
