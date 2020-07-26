N,K=map(int,input().split())
A=list(map(int,input().split()))

dictS={}
dictS[0]=1

for n in range (1,N):
    if n<K:
        dictS[n]=A[n]*dictS[n-1]
    else:
        dictS[n]=A[n]*dictS[n-1]/A[n-K]

    if n>=K:
        if dictS[n]>dictS[n-1]:
            print('Yes')
        else:
            print('No')