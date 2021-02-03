# AtCoder Beginner Contest 190
# B - Magic 3

N,S,D=map(int,input().split())

for _ in range (N):
    X,Y=map(int,input().split())
    if X>=S:
        continue
    if Y>D:
        print("Yes")
        exit()
    else:
        continue

print("No")