X=int(input())
Y=0
R=0.01

C=100

while C<X:
    Y+= 1
    C= C*(1+R)//1
    
print(Y)