# AtCoder Grand Contest 015
# A - A+...+B Problem

n,a,b=map(int,input().split())

if a>b:
    print(0)
    exit()

print((b-a)*(n-2)+1)