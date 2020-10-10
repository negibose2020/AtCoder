# AtCoder Regular Contest 104
# A - Plus Minus

A,B=map(int,input().split())
for i in range (-100,101):
    for j in range (-100,101):
        if i+j==A and i-j==B:
            print(i,j)
            exit()