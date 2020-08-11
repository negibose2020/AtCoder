# AtCoder Beginner Contest 097
# B - Exponential

X=int(input())

ans = 1

for i in range (1,X):
    for j in range (2,X):
        a=i**j
        if a==a//1 and a > ans and a<=X :
            ans=a
        if a>X:
            break
    if a>X:
        continue
print(ans)