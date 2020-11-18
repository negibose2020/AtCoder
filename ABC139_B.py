A,B=map(int,input().split())
for i in range(21):
    if 1+i*A-i>=B:
        print(i)
        exit()