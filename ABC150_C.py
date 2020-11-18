import itertools

N=int(input())
p=list(map(str,input().split()))
q=list(map(str,input().split()))
P=''.join(p)
Q=''.join(q)

ns=list(itertools.permutations(range(1,N+1)))
Ns=[]
for i in range(len(ns)):
    temparr=[]
    for j in range(N):
        a=ns[i][j]
        temparr.append(str(a))
    b=''.join(temparr)
    Ns.append(b)

PO=Ns.index(P)
QO=Ns.index(Q)
print(abs(PO-QO))
