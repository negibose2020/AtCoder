# N=int(input())
# Ws=[]
# for n in range(N):
#     W=input()
#     Ws.append(W)
# print (N,Ws)

# N=9
# Ws=['basic', 'c', 'cpp', 'php', 'python', 'nadesico', 'ocaml', 'lua', 'assembly']
# Ws=['hoge', 'english', 'hoge', 'enigma']
# N=4

N=int(input())
Ws=[]
for n in range(N):
    W=input()
    Ws.append(W)

for w in range(len(Ws)):
    if Ws.count(Ws[w])>=2:
        print("No")
        exit()
        
for x in range (1,len(Ws)):
    if Ws[x][0] != Ws[x-1][-1]:
        print("No")
        exit()

print("Yes")