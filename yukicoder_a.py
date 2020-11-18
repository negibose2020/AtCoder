def position(n, xs):
    for i, x in enumerate(xs):
        if x == n: return i
    return -1

# 循環小数 m/n = ([...],[...])
def repdec(m, n):
    xs = []
    ys = []
    while True:
        p = m / n
        q = m % n
        if q == 0:
            ys.append(p)
            return ys, [0]
        else:
            x = position(q, xs)
            if x >= 0:
                ys.append(p)
                return ys[:x+1], ys[x+1:]
            xs.append(q)
            ys.append(p)
            m = q * 10

print(repdec(335,113))