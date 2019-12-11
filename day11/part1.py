from robot import Robot
from intprogram import IntProgram
from queue import Queue
from threading import Thread

with open("input") as file:
    program_orig = list(map(int, file.read().split(',')))

q1 = Queue()
q2 = Queue()
instance = IntProgram(program_orig, q1, q2)
robot = Robot(q2, q1)

instance.start()
robot.start()
instance.join()
robot.join()

robot.print_result()
