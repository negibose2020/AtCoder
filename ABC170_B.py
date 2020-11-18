X,Y=map(int,input().split())

if Y>4*X or Y<2*X:
    print('No')
    exit()
else:
    pass

if (Y-2*X)%2==0:
    print('Yes')
else:
    print('No')