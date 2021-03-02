N,M,Q=map(int,input().split())
G=[[False for i in range (N)] for j in range (N)]
# print(G)

for _ in range (M):
    u,v=map(int,input().split())
    u-=1
    v-=1
    G[u][v]=True
    G[v][u]=True

colors=list(map(int,input().split()))
# print(G)
for _ in range (Q):
    li=list(map(int,input().split()))
    if li[0]==1:
        x=li[1]-1
        print(colors[x])
        for i in range (N):
            if G[x][i]==False:
                continue
            else:
                colors[i]=colors[x]
    else:
        x=li[1]-1
        print(colors[x])
        colors[x]=li[2]
    # print(G)
    # print(colors)