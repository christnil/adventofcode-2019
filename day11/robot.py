from queue import Queue
from threading import Thread


class Robot:
    def __init__(self, in_queue: Queue, out_queue: Queue):
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.painted = {(0, 0): True}
        self.position = (0, 0)
        self.dir = (-1, 0)
        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_y = 0
        self.task = Thread(target=self.run)
        self.task.setDaemon(True)

    def turn_left(self):
        if self.dir == (-1, 0):
            self.dir = (0, -1)
        elif self.dir == (0, -1):
            self.dir = (1, 0)
        elif self.dir == (1, 0):
            self.dir = (0, 1)
        elif self.dir == (0, 1):
            self.dir = (-1, 0)

    def turn_right(self):
        if self.dir == (-1, 0):
            self.dir = (0, 1)
        elif self.dir == (0, 1):
            self.dir = (1, 0)
        elif self.dir == (1, 0):
            self.dir = (0, -1)
        elif self.dir == (0, -1):
            self.dir = (-1, 0)

    def print_result(self):
        print('num painted')
        print(len(self.painted))
        print('')
        print(self.min_x, self.max_x, self.min_y, self.max_y)
        for x in range(self.min_x, self.max_x+1):
            for y in range(self.min_y, self.max_y+1):
                if (x, y) in self.painted and self.painted[(x, y)]:
                    print('@', end='')
                else:
                    print(' ', end='')
            print('')

    def update_limits(self):
        if self.position[0] < self.min_x:
            self.min_x = self.position[0]
        if self.position[0] > self.max_x:
            self.max_x = self.position[0]
        if self.position[1] < self.min_y:
            self.min_y = self.position[1]
        if self.position[1] > self.max_y:
            self.max_y = self.position[1]

    
    def move_forward(self):
        self.position = (self.position[0] + self.dir[0], self.position[1] + self.dir[1])
    
    def run(self):
        while True:
            code = self.in_queue.get()
            if code == 99:
                break
            elif code == 98:
                if self.position in self.painted and self.painted[self.position]:
                    self.out_queue.put(1)
                else:
                    self.out_queue.put(0)
            else:
                if code == 0:
                    self.painted[self.position] = False
                elif code == 1:
                    self.painted[self.position] = True
                self.update_limits()
                code = self.in_queue.get()
                if code == 0:
                    self.turn_left()
                elif code == 1:
                    self.turn_right()
                self.move_forward()

    def start(self):
        self.task.start()

    def join(self):
        self.task.join()