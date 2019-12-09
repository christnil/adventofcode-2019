from functools import reduce
x = 25
y = 6


with open('input') as file:
    encoded = [int(char) for char in file.readline().strip()]
    print(encoded)
    print(len(encoded))


layers = list(map(lambda i: encoded[i*x*y:(i+1)*x*y], range(0, int(len(encoded) / (x * y)))))
print(layers)


image = list(map(lambda x: ' ' if x == 0 else '*', reduce(
    lambda cur, it: list(map(lambda i: cur[i] if cur[i] < 2 else it[i], range(0, len(cur)))),
    layers
)))

rows = list(map(lambda i: image[i*25:(i+1)*25], range(0, int(len(image) / 25))))
string_rows = list(map(lambda r: ''.join(p for p in r), rows))

for r in string_rows:
    print(r)
