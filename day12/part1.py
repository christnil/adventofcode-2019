pos = [
    (-5, 6, -11),
    (-8, -4, -2),
    (1, 16, 4),
    (11, 11, -4)
]

vel = [
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0)
]

def e(v):
    return abs(v[0]) + abs(v[1]) + abs(v[2])


def calc_vel(vel_cur, v1, v2):
    vel_new = (
        vel_cur[0] + (1 if v2[0] > v1[0] else -1 if v2[0] < v1[0] else 0),
        vel_cur[1] + (1 if v2[1] > v1[1] else -1 if v2[1] < v1[1] else 0),
        vel_cur[2] + (1 if v2[2] > v1[2] else -1 if v2[2] < v1[2] else 0),
    )
    return vel_new

def apply_vel(p, v):
    return (p[0] + v[0], p[1] + v[1], p[2] + v[2])

def debug_print(step):
    print('step', step)
    for i in range(4):
        print(pos[i], vel[i])
    print()


debug_print(0)
for i in range(1000):
    for v1 in range(4):
        for v2 in range(4):
            vel[v1] = calc_vel(vel[v1], pos[v1], pos[v2])
    for v1 in range(4):
        pos[v1] = apply_vel(pos[v1], vel[v1])
    debug_print(i + 1)
    

sump = 0
for v1 in range(4):
    sump = sump + e(pos[v1]) * e(vel[v1])
print(sump)
