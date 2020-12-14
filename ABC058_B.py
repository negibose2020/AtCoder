# AtCoder Beginner Contest 058
# B - ∵∴∵

O=input()
E=input()

P=""
for i in range(len(O)+len(E)):
    if i%2==0:
        P+=O[i//2]
    else:
        P+=E[i//2]
print(P)