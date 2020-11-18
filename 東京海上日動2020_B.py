A,V=map(int,input().split())
B,W=map(int,input().split())
T=int(input())

if A<B:
    if A+T*V>=B+T*W:
        print('YES')
    else:
        print('NO')

elif B<A:
    if -1*T*V+A<=-1*T*W+B:
        print('YES')
    else:
        print('NO')
