#!/usr/bin/env python

'''Module for distinct code'''

def distinct_code(test_string):
  length = len(test_string)
  country_names = []
  count = 0
  for i in range(0, length - 1):
    country_codes = test_string[i:i+2]
    if country_names.count(country_codes) == 0:
      country_names.append(country_codes)
      count = count + 1
  return count

for _ in range(int(input())):
  TEST_STRING = input()
  print(distinct_code(TEST_STRING))
