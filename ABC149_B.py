A,B,K=map(int,input().split())
if K<=A:
    print(A-K,B)
    exit()
elif K>=A+B:
    print(0,0)
else:
    print(0,B+A-K)