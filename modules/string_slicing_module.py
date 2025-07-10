#!/use/bin/python3
"""
@brief string slicing module
@string_slicing
"""

class StringSlicingModule:
  """
  @brief
  """
  def __init__(self) -> None:
    """
    @brief constructor
    """
    pass

  @staticmethod
  def find_string_using_looping(in_str: str, pattern: str) -> int:
    """
    @brief find a string by using loop
    @param in_str: string
    @param pattern: string
    @return result: int, total number of matching string
    """
    result = 0
    pattern_len = len(pattern)
    for i in range(0, len(in_str)):
      word = ''
      if i + len(pattern) <= len(in_str):
        for j in range(i,i + pattern_len):
          word += in_str[j]
      if word == pattern:
        result +=1

    return result

  @staticmethod
  def find_string_using_slicing(in_str: str, pattern: str) -> int:
    """
    @brief find a string by using slicing
    @param in_str: string
    @param pattern: string
    @return result: int  , total number of matching string  
    """
    my_sum = 0
    pattern_len = len(pattern)
    for i in range(len(in_str) - pattern_len + 1):
      tmp_str = in_str[i:i+pattern_len]
      if tmp_str == pattern:
        my_sum += 1

    return my_sum
  
if __name__ == '__main__':
    print('module only, not main')
