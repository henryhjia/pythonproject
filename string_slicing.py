#!/use/bin/python3
"""
Python practice
reverse string
July 2023
"""

class StringSlicingTester:
  """
  @brief
  """
  def __init__(self) -> None:
    """
    @brief constructor
    """
    pass

  def find_string_by_coding(self, in_str: str, pattern: str) -> int:
    print('\n*********** find_string_by_coding()')
    print('Input string:', in_str, ' pattern:', pattern)
    result = 0
    pattern_len = len(pattern)
    word = ''
    for i in range(0, len(in_str)):
      word = ''
      if i + len(pattern) <= len(in_str):
        for j in range(i,i + pattern_len):
          word += in_str[j]
      print(f'word= {word}')
      if word == pattern:
        result +=1

    return result

  def find_string_using_slicing(self, in_str: str, pattern: str) -> int:
    print('\n*********** find_string_using_slicing()')
    print('Input string:', in_str, ' pattern:', pattern)

    sum = 0
    pattern_len = len(pattern)
    for i in range(len(in_str) - pattern_len + 1):
      tmp_str = in_str[i:i+pattern_len]
      print(f'word= {tmp_str}')
      if tmp_str == pattern:
        sum += 1

    return sum
  
  def reverse_string_using_slicing(self, in_str: str) -> str:
    """
    NOTE: string does not have build-in reverse method
    """
    print('\n*********** reverse_string_using_slicing()')
    reverse_str = in_str[::-1]
    return reverse_str
  
def main() -> int:
  """
  """
  me = StringSlicingTester()

  # find a string
  in_str = 'ABCCDCDCDCDC'
  pattern = 'CDC'

  result = me.find_string_by_coding(in_str, pattern)
  print(f'The total number of matching string is {result}')

  result = me.find_string_using_slicing(in_str, pattern)
  print(f'The total number of matching string \'{pattern}\' is {result}')

  result = me.reverse_string_using_slicing(in_str)
  print('Original str=', in_str)
  print('Reversed str=', result)
  exit(0)

if __name__ == '__main__':
  main()
