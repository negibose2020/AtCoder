N=int(input())
A=[]
for _ in range(N):
    a=int(input())
    A.append(a)

for i in range(1,N):
    r=A[i]-A[i-1]
    if r<0:
        print('down '+str(abs(r)))
    elif r==0:
        print('stay')
    else:
        print('up '+str(r))