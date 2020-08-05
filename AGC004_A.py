# AtCoder Grand Contest 004
# A - Divide a Cuboid


l=list(map(int,input().split()))
l.sort()

if l[0]*l[1]*l[2]%2==0:
    print(0)
else:
    print(l[0]*l[1])