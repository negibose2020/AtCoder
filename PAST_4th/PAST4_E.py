def f(oS,tS):
    if oS==tS:
        return False
    if tS==oS[::-1]:
        return False
    else:
        return True

import itertools

N=int(input())
S=input()

for v in itertools.permutations(S):
    tS="".join(v)
    if f(S,tS):
        print(tS)
        exit()
    
print("None")