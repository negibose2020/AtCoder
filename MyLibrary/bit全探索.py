N=3

for i in range(2**N):
    P=[]    
    for j in range(N):
        if i>>j & 1 ==1:
            P.append(1)
        else:
            P.append(0)
    print(P)

# >>
'''
[0, 0, 0]
[1, 0, 0]
[0, 1, 0]
[1, 1, 0]
[0, 0, 1]
[1, 0, 1]
[0, 1, 1]
[1, 1, 1]
'''