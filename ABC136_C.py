N=int(input())
Hi=list(map(int,input().split()))

for i in range(N-1):
    if Hi[i] < Hi[i+1]:
        Hi[i+1]-=1
    
    if Hi[i] == Hi[i+1]:
        pass

    if Hi[i] > Hi[i+1] :
        print('No')
        exit()

print('Yes')