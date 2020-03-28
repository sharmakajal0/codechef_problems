#!/usr/bin/env python

'''Module for the block game'''

##
# Question URL: https://www.codechef.com/problems/PALL01
##

def block_game(input_number):

  '''Function definition for reversing the number'''
  assigned_value = input_number
  reverse_number = 0

  while input_number > 0:
    reminder_value = input_number % 10
    reverse_number = (reverse_number * 10) + reminder_value
    input_number = input_number // 10

  if assigned_value == reverse_number:
    print("wins")

  else:
    print("losses")

for _ in range(int(input())):
  INPUT_NUMBER = int(input())
  block_game(INPUT_NUMBER)
