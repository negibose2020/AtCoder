# AtCoder Beginner Contest 091
# B - Two Colors Card Game

import collections

N=int(input())
S=[]
for i in range (N):
    s=input()
    S.append(s)

M=int(input())
T=[]
for j in range(M):
    t=input()
    T.append(t)

C_S=collections.Counter(S)
C_T=collections.Counter(T)

score=0

for word in C_S:
    temp_score=C_S[word] - C_T[word]
    if temp_score>score :
        score=temp_score
    else:
        pass

print(score)