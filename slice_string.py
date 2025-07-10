#!/use/bin/python3
"""
string slicing
@string_slicing
"""
import logging

from modules import string_slicing_module


def main() -> None:
  """
  """
  logging.basicConfig(filename='slice_string.log', level=logging.INFO, filemode='w')

  me = string_slicing_module.StringSlicingModule()

  # find a string
  in_str = 'ABCCDCDCDCDC'
  pattern = 'CDC'

  logging.info(f'original string= {in_str}')
  logging.info(f'pattern= {pattern}')

  result = me.find_string_using_looping(in_str, pattern)
  logging.info(f'The total number of matching string is {result}')

  result = me.find_string_using_slicing(in_str, pattern)
  logging.info(f'The total number of matching string \'{pattern}\' is {result}')
  logging.shutdown()

if __name__ == '__main__':
  main()
