# AtCoder Beginner Contest 063
# B - Varied

S=input()

for i in range(len(S)-1):
    for j in range (i+1,len(S)):
        if S[i]==S[j]:
            print("no")
            exit()

print("yes")