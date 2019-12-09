import numpy as np;
import math


def get_input():
    with open("input") as file:
        return list(map(int, file.readlines()))


cache = {}


def calculate_fuel_fuel(fuel):
    if fuel in cache:
        return cache[fuel]
    additional_fuel = math.floor(fuel / 3) - 2
    if additional_fuel <= 0:
        cache[fuel] = 0
        return 0
    cache[fuel] = additional_fuel + calculate_fuel_fuel(additional_fuel)
    return cache[fuel]


def calculateFuel(modules):
    array = np.array(modules)
    fuel = np.floor(array / 3) - 2
    total_fuel = list(map(lambda x: x + calculate_fuel_fuel(x), fuel.tolist()))
    sum = np.sum(total_fuel)
    return sum


def main():
    inputs = get_input()
    fuel = calculateFuel(inputs)
    print(fuel)


main()
