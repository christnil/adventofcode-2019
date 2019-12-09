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
      return
    else:
      raise Exception('unknown op code: {}'.format(op))


def main():
  input = getInput()
  input[1] = 12
  input[2] = 2
  runprogram(input)
  print(input[0])

main()