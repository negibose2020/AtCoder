# AtCoder Beginner Contest 185
# C - Duodecim Ferra

from math import factorial

L=int(input())
s=L-1
a=factorial(s)//factorial(s-11)
b=factorial(11)

print(a//b)