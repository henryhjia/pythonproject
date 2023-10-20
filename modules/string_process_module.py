"""
@brief process string
@processstring

This class contains various string processing methods
"""
import common_module

class StringProcessModule:
  """
  """
  def __init__(self):
     pass
     
  def count_occurrence(self, to_search, stream) -> int:
    """
    @param to_search: (String) The text to search for
    @param stream: (StringIO) An in-memory stream for text I/O
    @return count: (int) The number of lines that contain to_search
    """
    count = 0
    for str in stream:
      if to_search in str:
        count += 1
      
    return count     

  def is_string_palindrome(self, s: str) -> bool:
    """
    """
    common_module.print_function(self.is_string_palindrome)

    lower_str = ''

    for c in s:
      if c.isalnum():
        lower_str += c.lower()
    print(s)
    print(lower_str)

    if lower_str == lower_str[::-1]:
      return True
    else:
      return False

  def is_string_palindrome_method2(self, s: str) -> bool:
    """
    """
    common_module.print_function(self.is_string_palindrome_method2)

    lower_str = ''
    for c in s:
      if c.isalnum():
        lower_str += c.lower()

    len_lower_str = len(lower_str)
    print(lower_str)
    print('len_lower_str=',len_lower_str)
    half = len_lower_str // 2
    print('half=',half)

    for i in range(half):
      print('i=',i, lower_str[i], lower_str[len_lower_str - i - 1])
      if lower_str[i] != lower_str[len_lower_str - i - 1]:
        return False
      
    return True

if __name__ == '__main__':
    print('module only, not main')