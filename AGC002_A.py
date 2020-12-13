# AtCoder Grand Contest 002
# A - Range Product

a,b=map(int,input().split())
if a==0 or b==0:
    print("Zero ")
    exit()
if a<0 and b>0:
    print("Zero")
    exit()
if a>0:
    print("Positive")
    exit()

if (abs(a)-abs(b)+1)%2==0:
    print("Positive")
else:
    print("Negative")