K=int(input())
A,B=map(int,input().split())

for i in range(1000):
    if A<=i*K and i*K<=B:
        print('OK')
        exit()
print('NG')
exit()
