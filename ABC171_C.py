# N=int(input())
N=27
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

name=[]

for i in range (20):
    N=N-1
    name.insert(0,a[N%26])
    N=N//26
    if N==0:
        break

print(''.join(name))