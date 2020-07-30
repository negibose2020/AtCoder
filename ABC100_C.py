# AtCoder Beginner Contest 100
# C - *3 or /2
def f(N,c):
    if N%2==0:
        n=N//2
        c+=1
        return f(n,c)
    else:
        return c



N=int(input())
A=list(map(int,input().split()))

count=0

for a in A:
    count+= f(a,0)

print(count)
    