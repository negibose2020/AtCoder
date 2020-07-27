N,K=map(int,input().split())
A=list(map(int,input().split()))

for i in range (K,N):
    if A[i]>A[i-K]:
        print('Yes')
    else:
        print('No')

# WAだが、前にコミットしたものはコード自体に間違いがあることに気づいた。

N,K=map(int,input().split())
A=list(map(int,input().split()))

dictS={}
dictS[0]=1

P=10**9+7


for n in range (1,N+1):
    if n-1<K:
        dictS[n]=(A[n-1]*dictS[n-1])%P
    else:
        dictS[n]=(A[n-1]*dictS[n-1]/A[n-1-K])%P

    if n>K:
        if dictS[n]>dictS[n-1]:
            print('Yes')
        else:
            print('No')
