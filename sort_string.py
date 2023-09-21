#!/use/bin/python3
"""
Sort string
@sortstring

To sort the characters of the string 'google' in alphabetical order, you can use the sorted() 
function to create a sorted list of characters and then join() them back into a string.
"""
import sys
import string_sort_module

def main(args: list=None) -> int:
  print(f'lengh of argument : {len(args)}')
  if len(args) < 2:
    print('usage:', args[0], 'google')
    exit(1)

  me = string_sort_module.SortStringTester()

  # sort string
  result = me.sort_data(args[1])
  print(result)

  # sort both alphabet and digit string with these criterias:
  # 1. lower case letter before upper case letter
  # 2. alphebet before digit
  # 3. odd digit before even digit
  # an example: Sorted1234
  # result: deortS1324
  # 

  result = me.sort_alpha_digit(args[1])
  print(result)

if __name__ == '__main__':
  main(sys.argv)