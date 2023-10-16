#!/use/bin/python3
"""
string slicing
@stringslicing
"""
import string_slicing_module
  
def main() -> int:
  """
  """
  me = string_slicing_module.StringSlicingTester()

  # find a string
  in_str = 'ABCCDCDCDCDC'
  pattern = 'CDC'

  print('original string=', in_str)
  print('pattern=', pattern)
  result = me.find_string_by_coding(in_str, pattern)
  print(f'The total number of matching string is {result}')

  result = me.find_string_using_slicing(in_str, pattern)
  print(f'The total number of matching string \'{pattern}\' is {result}')


if __name__ == '__main__':
  main()
