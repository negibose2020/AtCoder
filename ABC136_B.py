N=int(input())
if N<10:
    print(N)
    exit()
if N<100:
    print(9)
    exit()
if N<1000:
    print(9+N-100+1)
    exit()
if N<10000:
    print(909)
    exit()
if N<100000:
    print(909+N-10000+1)
    exit()
if N==100000:
    print(90909)
    exit()