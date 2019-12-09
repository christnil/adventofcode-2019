with open("input") as file:
    lines = file.readlines()


orbits = {}
for line in lines:
    a, b = line.strip().split(')')[:2]
    if b in orbits:
        raise RuntimeError('Orbits two planets')
    orbits[b] = a


def get_distance_tree(start):
    dis = {}
    current = start
    d = 0
    while current in orbits:
        dis[current] = d
        d += 1
        current = orbits[current]
    dis[current] = d
    return dis


dis_me = get_distance_tree(orbits['YOU'])
dis_santa = get_distance_tree(orbits['SAN'])
common = set(dis_me.keys()).intersection(set(dis_santa.keys()))

print(min(map(lambda key: dis_santa[key] + dis_me[key], common)))
