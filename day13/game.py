from queue import Queue
from threading import Thread


class Game:
    def __init__(self, in_queue: Queue, out_queue: Queue, manual = False):
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.board = {}
        self.max_x = 0
        self.min_x = 0
        self.max_y = 0
        self.min_y = 0
        self.ball_x = 0
        self.paddle_x = 0
        self.task = Thread(target=self.run)
        self.task.setDaemon(True)
        self.manaul = manual

    def print_result(self):
        print('num blocks')
        print(len(list(filter(lambda x: x == 2, self.board.values()))))
        print('')


    def set_value(self, point, val):
        self.board[point] = val
        if point[0] < self.min_x:
            self.min_x = point[0]
        if point[0] > self.max_x:
            self.max_x = point[0]
        if point[1] < self.min_y:
            self.min_y = point[1]
        if point[1] > self.max_y:
            self.max_y = point[1]
        if val == 4:
            self.ball_x = point[0]
        if val == 3:
            self.paddle_x = point[0]

        
    def print_board(self):
        print('')
        print('game')
        print('')
        for y in range(self.min_y, self.max_y+1):
            for x in range(self.min_x, self.max_x+1):
                if (x, y) in self.board:
                    if self.board[(x, y)] == 0:
                        print(' ', end='')
                    if self.board[(x, y)] == 1:
                        print('#', end='')
                    if self.board[(x, y)] == 2:
                        print('.', end='')
                    if self.board[(x, y)] == 3:
                        print('_', end='')
                    if self.board[(x, y)] == 4:
                        print('*', end='')
                else:
                    print(' ', end='')
            print('')
        print('')


    def get_input(self):
        if self.manaul:
            self.print_board()
            while True:
                instruction = input('move joystick')
                if instruction == '-1' or instruction == '0' or instruction == '1':
                    self.out_queue.put(int(instruction))
                    break
                print('value must be between -1 and 1')
        else:
            if self.ball_x > self.paddle_x:
                self.out_queue.put(1)
            elif self.ball_x < self.paddle_x:
                self.out_queue.put(-1)
            else:
                self.out_queue.put(0)
        
    

    def run(self):
        while True:
            i1 = self.in_queue.get()
            if i1 == 'done':
                break
            if i1 == 'input':
                self.get_input()
                continue
            i2 = self.in_queue.get()
            i3 = self.in_queue.get()
            if i1 == -1 and i2 == 0:
                print('score:', i3)
            else:
                self.set_value((i1, i2), i3)
        

    def start(self):
        self.task.start()

    def join(self):
        self.task.join()