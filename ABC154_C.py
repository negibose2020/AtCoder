N=int(input())
A=list(map(int,input().split()))
a=set(A)
if len(a)==N:
    print('YES')
else:
    print('NO')