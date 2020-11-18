def toFindButton(arr,number):
    if arr.count(number)==0:
        return False
    else:
        return arr.index(number)

N=int(input())
lamps=[]
for a in range(N):
    _=int(input())
    lamps.append(_)
lamps.insert(0,"aaa")

PressedButtons=[False]*int(N+1)

a=1
count=0

if lamps.count(2)==0:
    print("-1")
    exit()

while PressedButtons[a]==False :
    PressedButtons[a]=True
    count+=1
    a=lamps[a]
    if a==2:
        print(count)
        exit()
print('-1')
