A,B,C,D=map(int,input().split())

HP_T=A
HP_A=C

for i in range(1,1000):
    if i%2==1:
        HP_A -= B
    else:
        HP_T -= D

    if HP_A<=0:
        print('Yes')
        exit()
    elif HP_T<=0:
        print('No')
        exit()
    else:
        pass