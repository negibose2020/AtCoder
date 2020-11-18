N=int(input())
list=[1,2,4,8,16,32,64]
if list.count(N)==1:
    print(N)
    exit()

list.append(N)
anslist=sorted(list)

print(anslist[anslist.index(N)-1])