# AtCoder Regular Contest 068
# C - X: Yet Another Die Game

x=int(input())

d,m=divmod(x,11)
if m==0:
    ans=2*d
else:
    if m>6:
        ans=2*d+2
    else:
        ans=2*d+1

print(ans)