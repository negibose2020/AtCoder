N=int(input())
S=set()

for n in range(N):
    _=int(input())
    if _ in S:
        S.remove(_)
    else:
        S.add(_)

print(len(S))