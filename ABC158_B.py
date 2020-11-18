N,A,B=map(int,input().split())
full=N//(A+B)
rest=N%(A+B)
if rest <=A:
    print(full*A+rest)
    exit()
else:
    print(full*A+A)
    exit()