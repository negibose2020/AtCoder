from line_profiler import LineProfiler
import os
from contextlib import redirect_stdout



import math
import random

def determination_of_multiples_of_eleven(num):
    numToStr=str(num)
    judge=0
    for i in range (len(numToStr)):
        if i%2==0:
            judge+=int(numToStr[i])
        else:
            judge-=int(numToStr[i])
    if judge%11==0:
        return True
    else:
        return False

def f(n):
    return n
def g(n):
    return f(n)
def h(n):
    return g(n)

def main():
    ans0=0
    for _ in range (10**6):
        ans0+=_
    ans1=0
    for i in range (10**6):
        ans1+=f(i)
    ans2=0
    for j in range (10**6):
        ans2+=g(j)
    ans3=0
    for k in range (10**6):
        ans3+=h(k)


    # for i in range (3):
    #     a=str(random.randint(10**50,10**51))
    #     b=(int(a)%11==0)

    # for i in range (3):
    #     a=str(random.randint(10**50,10**51))
    #     b=determination_of_multiples_of_eleven(a)


if __name__=='__name__':
    main()

# print()を画面出力する。
# prof = LineProfiler()
# prof.add_function(main)
# prof.runcall(main)
# prof.print_stats()

# print()を画面出力しない。
prof = LineProfiler()
prof.add_function(main)
with redirect_stdout(open(os.devnull,'w')):
    prof.runcall(main)
prof.print_stats()