N=int(input())

for i in range(1,10):
    a=N//i
    if a*i==N and a<=9:
        print('Yes')
        exit()
    else:
        pass

print('No')