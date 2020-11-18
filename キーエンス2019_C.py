N=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if sum(a)<sum(b):
    print(-1)
    exit()

p=0

ori_d=[]
for i in range (N):
    _d=a[i]-b[i]
    ori_d.append([i,_d])

d=sorted(ori_d,key=lambda x: x[1])
d2=[0]*N
for j in range (N):
    if d[j][1]>=0:
        break
    else:
        p+=abs(d[j][1])
        d2[j]+=1

for k in range (N-1,0,-1):
    if p==0:
        break
    elif d[k][1]<p:
        p-=d[k][1]
        d[k][1]=0
        d2[k]+=1
    else:
        d[k][1]-=p
        p=0
        d2[k]+=1

print(sum(d2))