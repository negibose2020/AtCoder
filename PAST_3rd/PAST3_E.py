N,M,Q=map(int,input().split())
# G=[[False for i in range (N)] for j in range (N)]
G=[]
for _ in range (N):
    G.append([])
# print(G)

for _ in range (M):
    u,v=map(int,input().split())
    u-=1
    v-=1
    G[u].append(v)
    G[v].append(u)

colors=list(map(int,input().split()))
# print(G)
for _ in range (Q):
    li=list(map(int,input().split()))
    if li[0]==1:
        x=li[1]-1
        print(colors[x])
        for i in range (len(G[x])):
            t=G[x][i]
            colors[t]=colors[x]
    else:
        x=li[1]-1
        print(colors[x])
        colors[x]=li[2]
    # print(G)
    # print(colors)