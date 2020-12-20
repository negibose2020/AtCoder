from functools import reduce
import math

def lcm_base(x,y):
    return (x*y) // math.gcd(x,y)

def lcm(*numbers):
    return reduce(lcm_base, numbers ,1)

def lcm_list(listOfNumbers):
    return reduce(lcm_base ,listOfNumbers ,1)

N=int(input())
l=[]
for i in range (N):
    l.append(int(input()))
ans=lcm_list(l)
print(ans)