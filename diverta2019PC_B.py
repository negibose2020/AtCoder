R,G,B,N=map(int,input().split())

ans=0

for i in range (3001):
    for j in range (3001):
        b=N-(R*i+G*j)
        if b<0:
            break
        if b%B==0:
            ans+=1
        
print(ans)