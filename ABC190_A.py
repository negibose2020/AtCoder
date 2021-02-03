# AtCoder Beginner Contest 190
# A - Very Very Primitive Game

A,B,C=map(int,input().split())

if C==0:
    if A>B:
        print("Takahashi")
    else:
        print("Aoki")
else:
    if A+1>B:
        print("Takahashi")
    else:
        print("Aoki")