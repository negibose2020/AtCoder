# AtCoder Beginner Contest 044
# B - 美しい文字列

import collections

w=input()

C=collections.Counter(w)
nums=list(C.values())
# print(nums)
for i in range (len(nums)):
    if int(nums[i])%2==0:
        continue
    else:
        print("No")
        exit()
print("Yes")