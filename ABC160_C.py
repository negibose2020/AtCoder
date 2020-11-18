K,N=map(int,input().split())
A=list(map(int,input().split()))
A.append(A[0]+K)

D=[]
for i in range(len(A)-1):
    d=A[i+1]-A[i]
    D.append(d)

print(K-max(D))