N,M=map(int,input().split())
a=input().split()
A=[]
for _ in a:
    A.append(int(_))
if sum(A)>N:
    print(-1)
else:
    print(N-sum(A))
