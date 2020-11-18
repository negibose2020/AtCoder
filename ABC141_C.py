N,K,Q=map(int,input().split())
L=[0]*(N)

for i in range(Q):
    a=int(input())
    L[a-1]+=1
    print(L)

for l in L:
    if K+l-Q >0:
        print('Yes')
    else:
        print('No')

