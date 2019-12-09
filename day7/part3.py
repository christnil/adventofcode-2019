import itertools
from queue import Queue
from threading import Thread

with open("input") as file:
    program_orig = list(map(int, file.read().split(',')))


class IntProgram:
    def __init__(self, code, in_queue: Queue, out_queue: Queue):
        self.program = code[:]
        self.ptr = 0
        self.last_output = 0
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.operations = {
            1: self.add,
            2: self.multiply,
            3: self.input,
            4: self.output,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals,
        }
        self.task = Thread(target=self.run)
        self.task.setDaemon(True)

    def add(self, immediate_a=False, immediate_b=False):
        a = self.program[self.ptr + 1]
        b = self.program[self.ptr + 2]
        a_val = a if immediate_a else self.program[a]
        b_val = b if immediate_b else self.program[b]
        res = self.program[self.ptr + 3]
        self.program[res] = a_val + b_val
        self.ptr += 4

    def multiply(self, immediate_a=False, immediate_b=False):
        a = self.program[self.ptr + 1]
        b = self.program[self.ptr + 2]
        a_val = a if immediate_a else self.program[a]
        b_val = b if immediate_b else self.program[b]
        res = self.program[self.ptr + 3]
        self.program[res] = a_val * b_val
        self.ptr += 4

    def input(self, immediate_a=False, immediate_b=False):
        val = self.in_queue.get()
        des = self.program[self.ptr + 1]
        self.program[des] = val
        self.ptr += 2

    def get_output(self):
        return self.last_output

    def output(self, immediate_a=False, immediate_b=False):
        a = self.program[self.ptr + 1]
        a_val = a if immediate_a else self.program[a]
        self.last_output = a_val
        self.out_queue.put(a_val)
        self.ptr += 2

    def jump_if_true(self, immediate_a=False, immediate_b=False):
        a = self.program[self.ptr + 1]
        b = self.program[self.ptr + 2]
        a_val = a if immediate_a else self.program[a]
        b_val = b if immediate_b else self.program[b]
        if a_val > 0:
            self.ptr = b_val
        else:
            self.ptr += 3

    def jump_if_false(self, immediate_a=False, immediate_b=False):
        a = self.program[self.ptr + 1]
        b = self.program[self.ptr + 2]
        a_val = a if immediate_a else self.program[a]
        b_val = b if immediate_b else self.program[b]
        if a_val == 0:
            self.ptr = b_val
        else:
            self.ptr += 3

    def less_than(self, immediate_a=False, immediate_b=False):
        a = self.program[self.ptr + 1]
        b = self.program[self.ptr + 2]
        a_val = a if immediate_a else self.program[a]
        b_val = b if immediate_b else self.program[b]
        res = self.program[self.ptr + 3]
        if a_val < b_val:
            self.program[res] = 1
        else:
            self.program[res] = 0
        self.ptr += 4

    def equals(self, immediate_a=False, immediate_b=False):
        a = self.program[self.ptr + 1]
        b = self.program[self.ptr + 2]
        a_val = a if immediate_a else self.program[a]
        b_val = b if immediate_b else self.program[b]
        res = self.program[self.ptr + 3]
        if a_val == b_val:
            self.program[res] = 1
        else:
            self.program[res] = 0
        self.ptr += 4

    def run(self):
        while self.program[self.ptr] != 99:
            if self.program[self.ptr] == 99:
                self.done = True
            elif self.program[self.ptr] > 4:
                tmp_str = str(self.program[self.ptr]).zfill(5)
                op = int(tmp_str[3:5])
                immediate_ap = tmp_str[2] == '1'
                immediate_bp = tmp_str[1] == '1'
                if tmp_str[0] == '1':
                    raise RuntimeError("something strange {}".format(tmp_str))
                self.operations[op](immediate_ap, immediate_bp)
            else:
                self.operations[self.program[self.ptr]]()

    def start(self):
        self.task.start()

    def join(self):
        self.task.join()


def startProgram(phase, in_queue, out_queue):
    instant = IntProgram(program_orig, in_queue, out_queue)
    in_queue.put(phase)
    instant.start()
    return instant


max_out = 0
best_perm = []
i = 1
for permutation in itertools.permutations(range(5, 10)):
    current_out = 0
    queues = list(map(lambda x: Queue(), range(len(permutation))))
    instances = list(map(lambda x: startProgram(permutation[x], queues[x - 1], queues[x]), range(len(permutation))))
    queues[-1].put(0)
    for instance in instances:
        instance.join()
    if instances[-1].get_output() > max_out:
        max_out = instances[-1].get_output()
        best_perm = permutation


print(best_perm)
print(max_out)
