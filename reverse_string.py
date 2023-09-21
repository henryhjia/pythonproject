#!/use/bin/python3
"""
@brief Reverse string
@reversestring

Two methods:
1. string slicing
2. manual

In Python, strings do not have a built-in reverse() method. Unlike lists, strings 
are immutable, which means their contents cannot be modified after creation. 
Therefore, strings DO NOT have methods like reverse() that would alter the 
order of characters in-place.

If you want to reverse a string, you can achieve it using slicing
"""
import string_reverse_module
import sys

def main(args: list=None) -> int:
  print(f'lengh of argument : {len(args)}')
  if len(args) < 2:
    print('usage:', args[0], 'google')
    exit(1)

  me = string_reverse_module.ReverseStringTester()

  # reverse strings
  me.reverse_data_using_slicing(args[1])
  me.reverse_data_manually(args[1])

if __name__ == '__main__':
  main(sys.argv)