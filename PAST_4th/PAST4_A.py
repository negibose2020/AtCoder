# A - 中央値
a,b,c=map(int,input().split())
l=[a,b,c]
l.sort()
if l[1]==a:
    print("A")
elif l[1]==b:
    print("B")
else:
    print("C")