N,M=map(int,input().split())

box=[1]*(N+1)
red=[0]*(N+1)
red[1]=1

for i in range (M):
    x,y=map(int,input().split())
    if box[x]==1 and red[x]==1:
        box[x]-=1
        red[x]-=1
        box[y]+=1
        red[y]+=1
        if red[y]>1:red[y]=1
    if box[x]>1 and red[x]==1:
        box[x]-=1
        # red[x]+-=0
        box[y]+=1
        red[y]+=1
        if red[y]>1:red[y]=1
    if box[x]>=1 and red[x]==0:
        box[x]-=1
        box[y]+=1
print(sum(red))