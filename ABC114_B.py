# AtCoder Beginner Contest 114
# B - 754

S=input()

ans=100000000

for i in range (len(S)-2):
    s=int(S[i:i+3])
    _ans=abs(753-s)
    if ans>_ans:
        ans=_ans
print(ans)