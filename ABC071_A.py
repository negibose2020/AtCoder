x,a,b=map(int,input().split())
DisXA=abs(a-x)
DisXB=abs(b-x)
if DisXA<DisXB:
    print('A')
else:
    print('B')