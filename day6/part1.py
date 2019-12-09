with open("input") as file:
    lines = file.readlines()


orbits = {}
all = set()
for line in lines:
    a, b = line.strip().split(')')[:2]
    all.add(a)
    all.add(b)
    if b in orbits:
        raise RuntimeError('Orbits two planets')
    orbits[b] = a

cache = {}


def orbitCount(planet):
    if planet not in orbits:
        return 0
    elif planet not in cache:
        cache[planet] = orbitCount(orbits[planet]) + 1
    return cache[planet]


print(sum(map(orbitCount, all)))
