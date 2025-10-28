#!/use/bin/python3
"""
string slicing
@string_slicing

Usage: in pythonproject/ run python -m basics.slice_string

"""
import logging
import os

from modules import string_slicing_module


def main() -> None:
  """
  """
  # Determine directory where the current script lives
  log_dir = os.path.dirname(__file__)
  log_file = os.path.join(log_dir, 'slice_string.log')

  # Configure logging
  logging.basicConfig(filename=log_file, level=logging.INFO, filemode='w')

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
