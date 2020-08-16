# AtCoder Beginner Contest 134
# B - Golden Apple

N,D= map(int,input().split())

d=2*D+1
n=N/d

if n>N//d:
    print(int(n)+1)
else:
    print(int(n))
