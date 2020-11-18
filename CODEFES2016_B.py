N,A,B=map(int,input().split())
S=input()

nowA=0
nowB=0

for s in S:
    if s=='c':
        print('No')
    elif s=='a':
        if nowA+nowB<A+B:
            print('Yes')
            nowA+=1
        else:
            print('No')
    else:
        if nowA+nowB<A+B and nowB<B:
            print('Yes')
            nowB+=1
        else:
            print('No')
