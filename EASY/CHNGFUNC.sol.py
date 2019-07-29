import math
def perfect_function(num_one, num_two):

  '''Function Definition for perfect function'''
    
  total = 0
  try:
    for i in range(1, num_one + 1):
      x = i * i
      for j in range(1, num_two + 1):
        f_n = x + j
        if math.sqrt(f_n) % 1 == 0:
          total += 1
        else: total += 0

    print(total)
  except EOFError:
    raise EOFError("End of file")
NUM_ONE, NUM_TWO = map(int, input().split())
perfect_function(NUM_ONE, NUM_TWO)
