# AtCoder Beginner Contest 190
# A - Very Very Primitive Game

A,B,C=map(int,input().split())

A+=C

for i in range (100):
    if i==0 and B==0 and A>0:
        print("Takahashi")
        exit()
    A-=1
    if A<=0:
        print("Aoki")
        exit()
    B-=1
    if B<=0:
        print("Takahashi")
        exit()