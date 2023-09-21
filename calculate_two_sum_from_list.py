#!/use/bin/python3
"""
string slicing
@stringslicing
@argsconverstion
"""
import sys
import two_sum_module
import ast

def main(args: list=None) -> int:
  """
  """
  print(f'lengh of argument : {len(args)}')
  if len(args) < 3:
    print('usage:', args[0], 'list of integers, target')
    exit(1)

  target = int(args[2])

  # Note: need to convert string form of a list to a list using ast
  in_list = ast.literal_eval(args[1])

  me = two_sum_module.TwoSumTester()
  result = me.find_two_sum_equal_to_target(in_list, target)

  print(result)

if __name__ == '__main__':
  main(sys.argv)
