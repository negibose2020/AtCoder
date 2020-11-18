from line_profiler import LineProfiler
import os
from contextlib import redirect_stdout


def main():
    a=10
    p=10**9+7

    for i in range(10**5):
        a*=a
        a%=p
    print(a)

    a=10
    for j in range(10**5):
        a*=a
    a%=p
    print(a)

if __name__=='__name__':
    main()

# print()を画面出力する。
prof = LineProfiler()
prof.add_function(main)
prof.runcall(main)
prof.print_stats()

# print()を画面出力しない。
# prof = LineProfiler()
# prof.add_function(main)
# with redirect_stdout(open(os.devnull,'w')):
#     prof.runcall(main)
# prof.print_stats()