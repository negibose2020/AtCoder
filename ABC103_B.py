# AtCoder Beginner Contest 103
# B - String Rotation

S=input()
T=input()

for _ in range (len(S)+2):
    S=S[1:]+S[0]
    # print(S)
    if S==T:
        print("Yes")
        exit()

print("No")