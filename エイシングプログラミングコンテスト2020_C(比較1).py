def f(x,y,z):
    n=x**2 + y**2 + z**2 + x*y + y*z + z*x
    return n
import time

s=time.time()

N=10000

anslist=[0]*60100

for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            n= f(x,y,z)
            anslist[n-1]+=1


for i in range(N):
    print(anslist[i])
f=time.time()

print(f-s)
