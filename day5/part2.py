with open("input") as file:
    program = list(map(int, file.read().split(',')))

ptr = 0
inputs = [5]
outputs = []


def add(immediate_a=False, immediate_b=False):
    global ptr
    a = program[ptr + 1]
    b = program[ptr + 2]
    a_val = a if immediate_a else program[a]
    b_val = b if immediate_b else program[b]
    res = program[ptr + 3]
    program[res] = a_val + b_val
    ptr += 4


def multiply(immediate_a=False, immediate_b=False):
    global ptr
    a = program[ptr + 1]
    b = program[ptr + 2]
    a_val = a if immediate_a else program[a]
    b_val = b if immediate_b else program[b]
    res = program[ptr + 3]
    program[res] = a_val * b_val
    ptr += 4


def input(immediate_a=False, immediate_b=False):
    global ptr
    res = program[ptr + 1]
    program[res] = inputs.pop(0)
    ptr += 2


def output(immediate_a=False, immediate_b=False):
    global ptr
    a = program[ptr + 1]
    a_val = a if immediate_a else program[a]
    outputs.append(a_val)
    ptr += 2


def jump_if_true(immediate_a=False, immediate_b=False):
    global ptr
    a = program[ptr + 1]
    b = program[ptr + 2]
    a_val = a if immediate_a else program[a]
    b_val = b if immediate_b else program[b]
    if a_val > 0:
        ptr = b_val
    else:
        ptr += 3


def jump_if_false(immediate_a=False, immediate_b=False):
    global ptr
    a = program[ptr + 1]
    b = program[ptr + 2]
    a_val = a if immediate_a else program[a]
    b_val = b if immediate_b else program[b]
    if a_val == 0:
        ptr = b_val
    else:
        ptr += 3


def less_than(immediate_a=False, immediate_b=False):
    global ptr
    a = program[ptr + 1]
    b = program[ptr + 2]
    a_val = a if immediate_a else program[a]
    b_val = b if immediate_b else program[b]
    res = program[ptr + 3]
    if a_val < b_val:
        program[res] = 1
    else:
        program[res] = 0
    ptr += 4


def equals(immediate_a=False, immediate_b=False):
    global ptr
    a = program[ptr + 1]
    b = program[ptr + 2]
    a_val = a if immediate_a else program[a]
    b_val = b if immediate_b else program[b]
    res = program[ptr + 3]
    if a_val == b_val:
        program[res] = 1
    else:
        program[res] = 0
    ptr += 4


operations = {
    1: add,
    2: multiply,
    3: input,
    4: output,
    5: jump_if_true,
    6: jump_if_false,
    7: less_than,
    8: equals,
}

while program[ptr] != 99:
    if program[ptr] > 4:
        tmp_str = str(program[ptr]).zfill(5)
        op = int(tmp_str[3:5])
        immediate_ap = tmp_str[2] == '1'
        immediate_bp = tmp_str[1] == '1'
        if tmp_str[0] == '1':
            raise RuntimeError("something strange {}".format(tmp_str))
        operations[op](immediate_ap, immediate_bp)
    else:
        operations[program[ptr]]()

print(outputs)
