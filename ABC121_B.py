N,M,C=map (int,input().split())
B=[]
b=list(input().split())
for _ in b:
    B.append(int(_))

Anser=0

for i in range(N):
    A=[]
    a=list(input().split())
    for _a in a:
        A.append(int(_a))
    temparr=[]
    for i in range(M):
        temparr.append(A[i]*B[i])
    if sum(temparr)+C>0:
        Anser+=1
print(Anser)