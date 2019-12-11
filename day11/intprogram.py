from queue import Queue
from threading import Thread


class IntProgram:
    def __init__(self, code, in_queue: Queue, out_queue: Queue):
        self.program = code[:]
        self.ptr = 0
        self.last_output = 0
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.relative_base = 0
        self.memory = {}
        self.num_out = 0
        self.operations = {
            1: self.add,
            2: self.multiply,
            3: self.input,
            4: self.output,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals,
            9: self.update_relative_base,
        }
        self.task = Thread(target=self.run)
        self.task.setDaemon(True)

    def read(self, ptr, mode='0'):
        program_value = self.program[ptr]
        if mode == '1':
            return program_value
        address = self.relative_base + program_value if mode == '2' else program_value
        if address < 0:
            raise RuntimeError('Read negative address')
        if address < len(self.program):
            return self.program[address]
        if address in self.memory:
            return self.memory[address]
        return 0

    def write(self, ptr, value, mode='0'):
        program_value = self.program[ptr]
        if mode == '1':
            raise RuntimeError('Cant write to direct mode')
        address = self.relative_base + program_value if mode == '2' else program_value
        if address < 0:
            raise RuntimeError('Read negative address')
        if address < len(self.program):
            self.program[address] = value
        else:
            self.memory[address] = value

    def add(self, op1='0', op2='0', r='0'):
        a = self.read(self.ptr + 1, op1)
        b = self.read(self.ptr + 2, op2)
        self.write(self.ptr + 3, a + b, r)
        self.ptr += 4

    def multiply(self, op1='0', op2='0', r='0'):
        a = self.read(self.ptr + 1, op1)
        b = self.read(self.ptr + 2, op2)
        self.write(self.ptr + 3, a * b, r)
        self.ptr += 4

    def input(self, op1='0', op2='0', r='0'):
        self.out_queue.put(98)
        val = self.in_queue.get()
        self.write(self.ptr + 1, val, op1)
        self.ptr += 2

    def get_output(self):
        return self.last_output

    def output(self, op1='0', op2='0', r='0'):
        a = self.read(self.ptr + 1, op1)
        self.last_output = a
        self.out_queue.put(a)
        self.num_out = self.num_out + 1
        self.ptr += 2

    def get_num_output(self):
        return self.num_out

    def jump_if_true(self, op1='0', op2='0', r='0'):
        a = self.read(self.ptr + 1, op1)
        b = self.read(self.ptr + 2, op2)
        if a > 0:
            self.ptr = b
        else:
            self.ptr += 3

    def jump_if_false(self, op1='0', op2='0', r='0'):
        a = self.read(self.ptr + 1, op1)
        b = self.read(self.ptr + 2, op2)
        if a == 0:
            self.ptr = b
        else:
            self.ptr += 3

    def less_than(self, op1='0', op2='0', r='0'):
        a = self.read(self.ptr + 1, op1)
        b = self.read(self.ptr + 2, op2)
        self.write(self.ptr + 3, 1 if a < b else 0, r)
        self.ptr += 4

    def equals(self, op1='0', op2='0', r='0'):
        a = self.read(self.ptr + 1, op1)
        b = self.read(self.ptr + 2, op2)
        self.write(self.ptr + 3, 1 if a == b else 0, r)
        self.ptr += 4

    def update_relative_base(self, op1='0', op2='0', r='0'):
        a = self.read(self.ptr + 1, op1)
        self.relative_base = self.relative_base + a
        self.ptr += 2

    def run(self):
        while self.program[self.ptr] != 99:
            if self.program[self.ptr] > 4:
                tmp_str = str(self.program[self.ptr]).zfill(5)
                op = int(tmp_str[3:5])
                m1 = tmp_str[2]
                m2 = tmp_str[1]
                m3 = tmp_str[0]
                if m3 == '1':
                    raise RuntimeError("something strange {}".format(tmp_str))
                self.operations[op](m1, m2, m3)
            else:
                self.operations[self.program[self.ptr]]()
        self.out_queue.put(99)

    def start(self):
        self.task.start()

    def join(self):
        self.task.join()