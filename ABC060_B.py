A,B,C=map(int,input().split())
for i in range (1,100000):
    if A*i%B==C:
        print('YES')
        exit()
    else:
        pass
print('NO')
