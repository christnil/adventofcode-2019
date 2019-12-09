import numpy as np;

def getInput():
  with open("input") as file:
    return list(map(int, file.readlines()))

def calculateFuel(modules):
  array = np.array(modules)
  print(array)
  step1 = array / 3
  print(step1)
  step2 = np.floor(step1)
  print(step2)
  step3 = step2 - 2
  print(step3)
  step4 = np.sum(step3)
  print(step4)

def main():
  input = getInput()
  calculateFuel(input)

main()