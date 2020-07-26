N,K=map(int,input().split())
A=list(map(int,input().split()))

dictS={}
dictS[0]=1

p=170141183460469231731687303715884105727

for n in range (1,N):
    if n<K:
        # S.append(A[n]*S[-1])
        dictS[n]=(A[n]*dictS[n-1])%p

    else:
        # S.append(A[n]*S[-1]/A[n-K])
        dictS[n]=(A[n]*dictS[n-1]/A[n-K])%p

for i in range (K,N):
    if dictS[i]>dictS[i-1]:
        print('Yes')
    else:
        print('No')
