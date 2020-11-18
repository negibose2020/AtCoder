H=1000000000000
H=int(input())
m=1
a=0

while H>1:
    a=m
    H=H//2
    _m=2*m
    m=_m

print(2*m-1)