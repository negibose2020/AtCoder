A,B=map(int,input().split())
for i in range(20000):
    if (i*8)//100==A and (i*10)//100==B:
        print(i)
        exit()
    else:
        pass
print(-1)