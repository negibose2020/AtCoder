N=int(input())
A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())

a=(N+(A-1))//A
b=(N+(B-1))//B
c=(N+(C-1))//C
d=(N+(D-1))//D
e=(N+(E-1))//E

bottleneck=max(a,b,c,d,e)
# print(a,b,c,d,e)
print(4+bottleneck)