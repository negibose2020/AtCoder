# AtCoder Beginner Contest 103
# C - Modulo Summation

from functools import reduce
import math

def lcm_base(x,y):
    return (x*y) // math.gcd(x,y)

def lcm(*numbers):
    return reduce(lcm_base, numbers ,1)

def lcm_list(listOfNumbers):
    return reduce(lcm_base ,listOfNumbers ,1)

N=int(input())
a=list(map(int,input().split()))

m=lcm_list(a)-1

ans = 0

for num in a:
    ans+=m%num

print(ans)