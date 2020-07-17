a=input()
b=input()
c=input()
A=a.replace('a','0').replace('b','1').replace('c','2')
list0=[]
for a in A:
    list0.append(int(a))
B=b.replace('a','0').replace('b','1').replace('c','2')
list1=[]
for b in B:
    list1.append(int(b))
C=c.replace('a','0').replace('b','1').replace('c','2')
list2=[]
for c in C:
    list2.append(int(c))
L=[list0,list1,list2]
# print(L)
# print(list0,list1,list2)

turn=0
nextturn=0

while L[turn]!=[]:
    nextturn=L[turn][0]
    L[turn]=L[turn][1:]
    turn=nextturn

ansarr=['A','B','C']
print(ansarr[turn])