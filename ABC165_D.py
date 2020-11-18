
A,B,N=map(int,input().split())
# A,B,N=11, 10, 5

ans=0

if N>=B:
    ans=(A*(B-1))//B - A*((B-1)//B)
else:
    ans=(A*N)//B - A*(N//B)

print(ans)


############
# 補足資料 #
############

'''

import random

def ABC165_D(A,B,N):
    # A,B,N=map(int,input().split())
    ans=0

    for i in range(N+1):
        temp=(A*i)//B - A*(i//B)
        print(i,(A*i)//B,A*(i//B),temp)


# for i in range (100):
#     A=random.randint(0,100)
#     B=random.randint(0,100)
#     N=random.randint(0,100)
#     print(A,B,N)

#     a=ABC165_D(A,B,N)

#     print(a)

A,B,N=11,10,5
print('i,A*x//b,A*(x//B),ans')
a=ABC165_D(A,B,N)
print(a)

'''