from collections import deque

N,X,Y=map(int,input().split())
visited=[[-1 for i in range (500)] for j in range (500)]

for _ in range (N):
    a,b=map(int,input().split())
    a+=250
    b+=250
    visited[a][b]=0


for i in range (500):
    visited[0][i]=0
    visited[i][0]=0
    visited[-1][i]=0
    visited[i][-1]=0

q=deque()
q.append([250,250])
visited[250][250]=0

while len(q)>0:
    v=q.popleft()
    now=visited[v[0]][v[1]]
    # print(v)
    if [v[0],v[1]]==[X+250,Y+250]:
        # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        print(visited[v[0]][v[1]])
        exit()
        # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    if visited[v[0]-1][v[1]]==-1 :
        q.append([v[0]-1,v[1]])
        visited[v[0]-1][v[1]]=now+1
    if visited[v[0]][v[1]-1]==-1 :
        q.append([v[0],v[1]-1])
        visited[v[0]][v[1]-1]=now+1
    if visited[v[0]+1][v[1]]==-1 :
        q.append([v[0]+1,v[1]])
        visited[v[0]+1][v[1]]=now+1
    if visited[v[0]][v[1]+1]==-1  :
        q.append([v[0],v[1]+1])
        visited[v[0]][v[1]+1]=now+1
    if visited[v[0]+1][v[1]+1]==-1  :
        q.append([v[0]+1,v[1]+1])
        visited[v[0]+1][v[1]+1]=now+1
    if visited[v[0]-1][v[1]+1]==-1  :
        q.append([v[0]-1,v[1]+1])
        visited[v[0]-1][v[1]+1]=now+1

print(-1)

## BFS
## 幅優先探索