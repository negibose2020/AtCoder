# AtCoder Beginner Contest 084
# B - Postal Code

A,B=map(int,input().split())
S=input()

for i in range(A+B+1):
    if i==A:
        if S[i]=="-":
            continue
        else:
            print("No")
            exit()
    else:
        if S[i]=="-":
            print("No")
            exit()

print("Yes")