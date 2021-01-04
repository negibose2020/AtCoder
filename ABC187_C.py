# AtCoder Beginner Contest 187
# C - 1-SAT

N=int(input())
ls=[]
st=set()
for _ in range (N):
    S=input()

    if S[0]=="!":
        S=S[1:]
        ls.append(S)
    else:
        st.add(S)

for i in range (len(ls)):
    if ls[i] in st:
        print(ls[i])
        exit()
    else:
        continue

print("satisfiable")