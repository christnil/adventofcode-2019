import numpy as np;


def getInput():
    with open("input") as file:
        return list(map(int, file.read().split(',')))


def runprogram(instructions):
    for x in range(0, len(instructions) - 3, 4):
        op = instructions[x]
        a = instructions[x + 1]
        b = instructions[x + 2]
        r = instructions[x + 3]
        if op == 1:
            instructions[r] = instructions[a] + instructions[b]
        elif op == 2:
            instructions[r] = instructions[a] * instructions[b]
        elif op == 99:
            return instructions[0]
        else:
            raise Exception('unknown op code: {}'.format(op))


def main():
    input = getInput()
    for noun in range(0, 100):
        for verb in range(0, 100):
            instance = input[:]
            instance[1] = noun
            instance[2] = verb
            result = runprogram(instance)
            if result == 19690720:
                print('noun: {}'.format(noun))
                print('verb: {}'.format(verb))
                print((100 * noun) + verb)
                return


main()
