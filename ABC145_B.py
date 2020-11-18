N=int(input())
S=input()

s=S[0:N//2]
if s*2==S:
    print('Yes')
else:
    print('No')