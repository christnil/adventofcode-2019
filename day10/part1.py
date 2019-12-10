import math
from operator import itemgetter

with open('input') as file:
    matrix_in = list(map(lambda line: [x for x in line], file.readlines()))


astroids = []
for y in range(len(matrix_in)):
    for x in range(len(matrix_in[y])):
        if matrix_in[y][x] == '#':
            astroids.append((x, y))


vfor = lambda a, b: (b[0] - a[0], a[1] - b[1])
vlen = lambda v: math.sqrt(v[0] ** 2 + v[1] ** 2)
def normalize(v):
    length = vlen(v)
    return round(v[0] / length, 10), round(v[1] / length, 10)


def num_in_view_for_astroids(astroid, other_astroids):
    #print(other_astroids)
    vectors = list(map(lambda x: vfor(astroid, x), other_astroids))
    nvectors = list(map(lambda x: normalize(x), vectors))
    #print(vectors)
    #print(nvectors)
    #print(set(nvectors))
    return len(set(nvectors))



num_in_view = list(map(lambda x: (x, num_in_view_for_astroids(x, list(filter(lambda y: y != x, astroids)))), astroids))

max_point, in_sight = max(num_in_view, key=itemgetter(1))

print(max_point, in_sight)

# part2

mapped = list(map(lambda x: (x, normalize(vfor(max_point, x)), vlen(vfor(max_point, x))), filter(lambda x: x != max_point, astroids)))
by_vector = {}
unique_vectors = []
for x in mapped:
    if x[1] not in by_vector:
        by_vector[x[1]] = []
        unique_vectors.append(x[1])
    by_vector[x[1]].append(x)

for v in unique_vectors:
    by_vector[v].sort(key=itemgetter(2))

unique_vectors = list(map(lambda x: (x, math.atan2(x[0], x[1])), unique_vectors))
unique_vectors.sort(key=itemgetter(1))
for i in range(len(unique_vectors)):
    if unique_vectors[i][0] == (0.0, 1.0):
        index = i
        break

num_destroyed = 0
last_destroyed = 0;
while num_destroyed < 200:
    v = unique_vectors[i]
    i = (i + 1) % len(unique_vectors)
    if len(by_vector[v[0]]) > 0:
        last_destroyed = by_vector[v[0]].pop(0)
        num_destroyed = num_destroyed + 1
        print(num_destroyed)
        print(last_destroyed)

print()
print(num_destroyed)
print(last_destroyed)
print(last_destroyed[0][0] * 100 + last_destroyed[0][1])
