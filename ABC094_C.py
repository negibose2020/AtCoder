N=int(input())
x=list(map(int,input().split()))

X=sorted(x)
M1=X[(N//2)-1]
M2=X[N//2]

# print(X)
# print(M1,M2)

for i in range (N):
    if x[i]<=M1:
        print(M2)
    else:
        print(M1)
