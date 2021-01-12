# AtCoder Beginner Contest 188
# A - Three-Point Shot

X,Y=map(int,input().split())

if X<Y:
    if X+3>Y:
        print("Yes")
    else:
        print("No")
else:   # Y>X また、制約より Y==X はない。
    if Y+3>X:
        print("Yes")
    else:
        print("No")