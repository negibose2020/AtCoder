# AtCoder Regular Contest 108
# A - Sum and Product

s,p=map(int,input().split())

end=int((p**0.5))+1

for i in range (1,end):
    if p%i==0:
        a=p//i
        b=p//a
        if a+b==s:
            print("Yes")
            exit()


print("No")