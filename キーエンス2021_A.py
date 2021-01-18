N=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

maxa=a[0]
maxb=b[0]
maxnum=a[0]*b[0]
for i in range (N):
    maxa=max(maxa,a[i])
    maxnum=max(maxnum,maxa*b[i])
    print(maxnum)