N,K=map(int,input().split())

D=[]
while N>=K :
    D.append(N%K)
    N=N//K
print(len(D)+1)
