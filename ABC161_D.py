# AtCoder Beginner Contest 161
# D - Lunlun Number

from collections import deque

K=int(input())

# seen=set()
lunlun=deque()
ans=0
for i in range (1,10):
    lunlun.append(i)

while len(lunlun)>0:
    # print(lunlun)
    ans+=1
    num=lunlun.popleft()
    if ans==K:
        print(num)
        exit()

    if num%10==0:
        lunlun.append(num*10)
        lunlun.append(num*10+1)
    elif num%10==9:
        lunlun.append(num*10+8)
        lunlun.append(num*10+9)
    else:
        a=num%10
        lunlun.append(num*10+a-1)
        lunlun.append(num*10+a)
        lunlun.append(num*10+a+1)


# BFS