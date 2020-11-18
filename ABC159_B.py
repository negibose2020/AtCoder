S=input()
N=len(S)
S_1=S[0:(N-1)//2]
S_2=S[(N+3)//2:-1]

if S!=S[::-1]:
    print('No')
    exit()
else:
    pass
if S_1!=S_1[::-1]:
    print('No')
    exit()
else:
    pass
if S_2!=S_2[::-1]:
    print('No')
    exit()
else:
    print('Yes')