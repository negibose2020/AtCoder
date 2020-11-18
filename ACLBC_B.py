a,b,c,d=map(int,input().split())
if b<c:
    print('No')
    exit()
if c<=b and a<=c:
    print('Yes')
    exit()
if d<a:
    print('No')
    exit()
if a<=d and c<=a:
    print('Yes')
    exit()

print('No')