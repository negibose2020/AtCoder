# AtCoder Beginner Contest 175
# A - Rainy Season

S=input()
if S=="RRR":
    print(3)
    exit()
if S=="SRR" or S=="RRS":
    print(2)
    exit()
if S=="SSS":
    print(0)
    exit()
else:
    print(1)