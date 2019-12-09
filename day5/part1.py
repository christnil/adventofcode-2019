
with open("input") as file:
    program = list(map(int, file.read().split(',')))

ptr = 0
inputs = [1]
outputs = []


def add(immediate_a = False, immediate_b = False):
    global ptr
    a = program[ptr + 1]
    b = program[ptr + 2]
    a_val =  a if immediate_a else program[a]
    b_val = b if immediate_b else program[b]
    res = program[ptr + 3]
    program[res] = a_val + b_val
    ptr += 4


def multiply(immediate_a = False, immediate_b = False):
    global ptr
    a = program[ptr + 1]
    b = program[ptr + 2]
    a_val =  a if immediate_a else program[a]
    b_val = b if immediate_b else program[b]
    res = program[ptr + 3]
    program[res] = a_val * b_val
    ptr += 4


def input(immediate_a = False, immediate_b = False):
    global ptr
    res = program[ptr + 1]
    program[res] = inputs.pop(0)
    ptr += 2


def output(immediate_a = False, immediate_b = False):
    global ptr
    a = program[ptr + 1]
    a_val =  a if immediate_a else program[a]
    outputs.append(a_val)
    ptr += 2


operations = {
    1: add,
    2: multiply,
    3: input,
    4: output
}


while program[ptr] != 99:
    if program[ptr] > 4:
        tmp_str = str(program[ptr]).zfill(5)
        op = int(tmp_str[3:5])
        immediate_a = tmp_str[2] == '1'
        immediate_b = tmp_str[1] == '1'
        if tmp_str[0] == '1':
            raise RuntimeError("something strange {}".format(tmp_str))
        operations[op](immediate_a, immediate_b)
    else:
        operations[program[ptr]]()


print(outputs)
