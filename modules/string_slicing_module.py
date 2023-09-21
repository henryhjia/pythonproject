#!/use/bin/python3
"""
@brief string slicing module
@stringslicing
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
  
if __name__ == '__main__':
    print('module only, not main')
