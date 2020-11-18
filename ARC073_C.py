N,T=map(int,input().split())
a=list(input().split())
ts=[]
for _ in range (len(a)):
    ts.append(int(a[_]))

# ts=[0, 3]
# N,T=2, 4

YU=T

for i in range(1,N):
    if ts[i]-ts[i-1]<T:
        YU+=T-(T-(ts[i]-ts[i-1]))
    else:
        YU+=T
print (YU)