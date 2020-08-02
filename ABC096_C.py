# AtCoder Beginner Contest 096
# C - Grid Repainting 2

def f (i,j):
    if any ([area[i-1][j]=='#',
            area[i+1][j]=='#',
            area[i][j-1]=='#',
            area[i][j+1]=='#']):
        return True


H,W=map(int,input().split())

area=['.'*(W+2)]

for i in range (H):
    A='.'+ input() +'.'
    area.append(A)

area.append('.'*(W+2))

ans='Yes'

for i in range (1,H+1):
    for j in range (1,W+1):
        if area[i][j]=='#':
            if f(i,j)==True:
                pass
            else:
                ans='No'
                break
        else:
            pass

print(ans)