S=input()

for s in S[::2]:
    if s=='L':
        print ('No')
        exit()

for s in S[1::2]:
    if s=='R':
        print('No')
        exit()

print('Yes')