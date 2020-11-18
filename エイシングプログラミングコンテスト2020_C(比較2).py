from line_profiler import LineProfiler
import os
from contextlib import redirect_stdout

def f(x,y,z):
    n=x**2 + y**2 + z**2 + x*y + y*z + z*x
    return n

def main():
    N=10**4
    anslist=[0]*60100

    for x in range(1,100):
        for y in range(1,100):
            for z in range(1,100):
                n= f(x,y,z)
                anslist[n-1]+=1

    for i in range(N):
        print(anslist[i])

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