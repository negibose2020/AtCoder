# AtCoder Beginner Contest 053
# B - A to Z String

s=input()

a=s.index("A")
S=s[::-1]
z=S.index("Z")

print(len(S)-a-z)