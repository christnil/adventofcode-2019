from game import Game
from intprogram import IntProgram
from queue import Queue
from threading import Thread

with open("input") as file:
    program_orig = list(map(int, file.read().split(',')))

q1 = Queue()
q2 = Queue()
instance = IntProgram(program_orig, q1, q2)
game = Game(q2, q1)

instance.start()
game.start()
instance.join()
game.join()

game.print_result()
