s=list(input())
t=list(input())
s.sort()
t.sort()
tt=sorted(t,reverse=True)

if s<tt:
    print("Yes")
else:
    print("No")