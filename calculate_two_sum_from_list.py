"""
calculate two sum from a list and compare it with a target
@twosum
commandline: python3 calculate_two_sum_from_list.py [1,2,3] 5
"""
import sys
import two_sum_module
import ast

def main(args: list) -> None:
  """
  """
  print(f'lengh of argument : {len(args)}')
  if len(args) < 3:
    print('usage:', args[0], 'list of integers, target')
    exit(1)

  target = int(args[2])

  # Note: need to convert string form of a list to a list using ast
  in_list = ast.literal_eval(args[1])
  print('input list=', in_list)
  print('target=', target)
  me = two_sum_module.TwoSumModule()
  result = me.find_two_sum_equal_to_target(in_list, target)

  print(result)

if __name__ == '__main__':
  main(sys.argv)
