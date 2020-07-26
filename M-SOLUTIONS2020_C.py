N,K=map(int,input().split())
A=list(map(int,input().split()))

S=[1]

for n in range (N):
    if n<K:
        S.append(A[n]*S[-1])
    else:
        S.append(A[n]*S[-1]/A[n-K])

for i in range (K+1,N+1):
    if S[i]>S[i-1]:
        print('Yes')
    else:
        print('No')