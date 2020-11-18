def Judge_the_color(P):
    if P <= 399:
        return 'gray'
    elif P<=799:
        return 'brown'
    elif P<=1199:
        return 'green'
    elif P<=1599:
        return 'lightblue'
    elif P<=1999:
        return 'blue'
    elif P<=2399:
        return 'yellow'
    elif P<=2799:
        return 'orange'
    elif P<=3199:
        return 'red'
    else:
        return 'WC'

N=int(input())
aaa=list(map(int,input().split()))
l=[]

for a in aaa:
    l.append(Judge_the_color(a))

WCs=l.count('WC')

MIN=len(set(l))
MAX=len(set(l))

if MIN==1 and l[0]=='WC':
    MIN=1
elif WCs>=1:
    MIN=MIN-1
else:
    pass

if WCs>=1:
    MAX=MAX-1+WCs
else:
    pass

print(MIN,MAX)