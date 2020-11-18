N=int(input())
a=list(map(int,input().split()))
arr=[]
for A in a:
    if A%2==0:
        arr.append(A)
    else:
        pass

for n in arr:
    if n%3==0 or n%5==0:
        pass
    else:
        print('DENIED')
        exit()
print('APPROVED')