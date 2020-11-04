def determination_of_multiples_of_eight(num):
    numToStr=str(num)
    if len(numToStr)==1:
        numToStr=numToStr.zfill(3)
        # print(int(numToStr))

    if int(numToStr[-3:])%8==0:
        return True
    else:
        return False

from itertools import combinations,permutations
from collections import Counter
S=input()
if len(S)<3:
    if determination_of_multiples_of_eight(S) or determination_of_multiples_of_eight(S[::-1]):
        print("Yes")
        exit()


for i in range (8,999,8):
    C=Counter(S)

    if C[str(i).zfill(3)[0]]>0:
        C[str(i).zfill(3)[0]]-=1
        if C[str(i).zfill(3)[1]]>0:
            C[str(i).zfill(3)[1]]-=1
            if C[str(i).zfill(3)[2]]>0:
                C[str(i).zfill(3)[2]]-=1
                print("Yes")
                exit()

print("No")
