x = 25
y = 6


with open('input') as file:
    encoded = [int(char) for char in file.readline().strip()]
    print(encoded)
    print(len(encoded))


layers = list(map(lambda i: encoded[i*x*y:(i+1)*x*y], range(0, int(len(encoded) / (x * y)))))
print(layers)


def get_num_of(layer, digit):
    return len(list(filter(lambda d: d == digit, layer)))


max_count = -1
max_layer = []
max_result = 0
for layer in layers:
    num_zero = get_num_of(layer, 0)
    if num_zero < max_count or max_count == -1:
        max_count = num_zero
        max_layer = layer
        max_result = get_num_of(layer, 1) * get_num_of(layer, 2)

print(max_count)
print(max_layer)
print(max_result)
