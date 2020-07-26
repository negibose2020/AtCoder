R,G,B=map(int,input().split())
K=int(input())


for _ in range (K) :
    if R < G :
        pass
    else:
        G*=2
        continue

    if G < B :
        pass
    else:
        B*=2
        continue
    
if R < G < B :
    print('Yes')
else :
    print('No')
