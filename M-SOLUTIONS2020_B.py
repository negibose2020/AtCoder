R,G,B=map(int,input().split())
K=int(input())

M=0

while R>=G or G>=B:
    if R>=G:
        G*=2
        M+=1
    
    if G>=B:
        B*=2
        M+=1

if M<=K:
    print('Yes')
else:
    print('No')
