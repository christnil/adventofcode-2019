from numpy import lcm

x = [-5, -8, 1, 11]
y = [6, -4, 16, 11]
z = [-11, -2, 4, -4]

def fv(v, d):
    return [v[0] + d[0], v[1] + d[1], v[2] + d[2], v[3] + d[3]]

def fd(v, d):
    new_d = [d[0], d[1], d[2], d[3]]
    for i in range(4):
        for j in range(4):
            if v[i] < v[j]:
                new_d[i] = new_d[i] + 1
            elif v[i] > v[j]:
                new_d[i] = new_d[i] - 1
    return new_d

def find_loop(iv):
    v = [iv[0], iv[1], iv[2], iv[3]]
    d = [0, 0, 0, 0]

    d = fd(v, d)
    v = fv(v, d)
    i = 1
    while v != iv or d != [0, 0, 0, 0]:
        d = fd(v, d)
        v = fv(v, d)
        i = i + 1
    print(iv, v, d)
    return i


xl = find_loop(x)
yl = find_loop(y)
zl = find_loop(z)

print(xl, yl, zl)
print(lcm(xl, lcm(yl, zl)))
