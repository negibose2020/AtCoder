# AtCoder Beginner Contest 187
# C - 1-SAT

N=int(input())

st=set()

for _ in range (N):
    S=input()
    st.add(S)

for s in st:
    if s[0]=='!':
        if s[1:] in st:
            print(s[1:])
            exit()

print("satisfiable")