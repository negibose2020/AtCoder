S=input()
L=("a","b","c","d","e","f","g","h","i","j","k","l","m","n",
    "o","p","q","r","s","t","u","v","w","x","y","z")
for l in L:
    if S.count(l)>0:
        pass
    else:
        print(l)
        exit()
else:
    print("None")