#!/usr/bin/env python

'''Module for snack up'''

##
# Question URL: https://www.codechef.com/problems/SNACKUP
##

def snack_up(test_integer):

  '''Function Definition of snack up'''
  count = 0
  print(test_integer)

  for _ in range(test_integer):
    count += 1
    print(test_integer)

    for i in range(test_integer):
      print(i + 1, end=' ')

      if count > test_integer: count = 1

      print(count, end=' ')
      count += 1

      if count > test_integer: count = 1

      print(count)

for _ in range(int(input())):
  NUMBER_JUDGE = int(input())
  snack_up(NUMBER_JUDGE)
