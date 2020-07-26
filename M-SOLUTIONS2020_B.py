R,G,B=map(int,input().split())
K=int(input())


for i in range (K+1):
    if R < G < B:
        print ('Yes')
        exit()
    else:
        pass
    
    if G < B:
        pass
    else:
        B*=2
        continue

    if R < G:
        pass
    else:
        G*=2
        continue

print('No')
