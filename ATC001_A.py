# A - 深さ優先探索
from collections import deque

H,W=map(int,input().split())
area=[]
s=[0,0]
g=[1,1]
for i in range (H):
    c=input()
    if 's' in c: s=[i,c.index('s')]
    if 'g' in c: g=[i,c.index('g')]
    area.append(c)

seen=[]
for _ in range (H):
    seen.append([-1]*W)
todo=deque()
seen[s[0]][s[1]]=0
todo.append(s)

while len(todo)>0:
    v=todo.pop()
    if v==g:
        print('Yes')
        exit()
    # print(v)
    if v[0]-1>=0 and area[v[0]-1][v[1]]!="#" and seen[v[0]-1][v[1]]==-1:
        seen[v[0]-1][v[1]]=seen[v[0]][v[1]]+1
        todo.append([v[0]-1,v[1]])
    if v[0]+1<H and area[v[0]+1][v[1]]!="#" and seen[v[0]+1][v[1]]==-1:
        seen[v[0]+1][v[1]]=seen[v[0]][v[1]]+1
        todo.append([v[0]+1,v[1]])
    if v[1]-1>=0 and area[v[0]][v[1]-1]!="#" and seen[v[0]][v[1]-1]==-1:
        seen[v[0]][v[1]-1]=seen[v[0]][v[1]]+1
        todo.append([v[0],v[1]-1])
    if v[1]+1<W and area[v[0]][v[1]+1]!="#" and seen[v[0]][v[1]+1]==-1:
        seen[v[0]][v[1]+1]=seen[v[0]][v[1]]+1
        todo.append([v[0],v[1]+1])
    # print(todo)
    # print(seen)
    
# print(seen)
# print(area,s,g)
print("No")


# BFS
# 深さ優先探索