N=int(input())
vn=list(map(int,input().split()))
vn.sort()

value=vn[0]

for i in range(1,N):
    tempV=(value+vn[i])/2
    value=tempV

print(value)