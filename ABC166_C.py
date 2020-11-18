N,M=map(int,input().split())
hs=input().split()

H=[0]                           #各丘の高さ(index1は文中の1)
for h in hs:
    H.append(int(h))


P=[[0]*1 for i in range(N+1)]   #各丘からの道 二次元配列 (index1は文中の1)
count=0
for p in range(len(P)):
    P[p][0]=p                   #P[][0] 各配列の要素1は自身の丘の数字
# print(P)

for m in range(M):
    pathfrom,pathto= map (int,input().split())
    P[pathfrom].append(H[pathto])
    P[pathto].append(H[pathfrom])
for i in range(1,len(P)):
    if len(P[i])==1:
        count+=1
    else:
        P[i][0]=H[i]
        _rP=P[i][1:]
        if P[i][0]>max(_rP):
            count+=1
print(count)