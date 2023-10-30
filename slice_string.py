#!/use/bin/python3
"""
string slicing
@stringslicing
"""
import string_slicing_module
import logging

def main() -> None:
  """
  """
  logging.basicConfig(filename='slice_string.log', level=logging.DEBUG, filemode='w')
  logger = logging.getLogger('my_logger')

  me = string_slicing_module.StringSlicingModule()

  # find a string
  in_str = 'ABCCDCDCDCDC'
  pattern = 'CDC'

  print('original string=', in_str)
  print('pattern=', pattern)
  logger.info(f'original string= {in_str}')
  logger.info(f'pattern= {pattern}')

  result = me.find_string_using_looping(in_str, pattern)
  print(f'The total number of matching string is {result}')
  logger.info(f'The total number of matching string is {result}')

  result = me.find_string_using_slicing(in_str, pattern)
  print(f'The total number of matching string \'{pattern}\' is {result}')
  logger.info(f'The total number of matching string \'{pattern}\' is {result}')
  logging.shutdown()

if __name__ == '__main__':
  main()
