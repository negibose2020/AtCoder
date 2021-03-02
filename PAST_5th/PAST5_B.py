# 第五回 アルゴリズム実技検定
# B - 上書き

N=int(input())
S=input()

T=[]
for i in range (N):
    while S[i] in T:
        del(T[T.index(S[i])])
    T.append(S[i])

print("".join(T))