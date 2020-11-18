S=input()
if S=='keyence' or S[0:7]=='keyence' or S[-7:]=='keyence':
    print('YES')
    exit()
else:
    pass

if S[0]=='k':
    if S[-6:]=='eyence':
        print('YES')
        exit()
    else:
        pass
if S[:2]=='ke':
    if S[-5:]=='yence':
        print('YES')
        exit()
    else:
        pass
if S[:3]=='key':
    if S[-4:]=='ence':
        print('YES')
        exit()
    else:
        pass
if S[:4]=='keye':
    if S[-3:]=='nce':
        print('YES')
        exit()
    else:
        pass
if S[:5]=='keyen':
    if S[-2:]=='ce':
        print('YES')
        exit()
    else:
        pass
if S[:6]=='keyenc':
    if S[-1]=='e':
        print('YES')
        exit()
    else:
        pass
print('NO')