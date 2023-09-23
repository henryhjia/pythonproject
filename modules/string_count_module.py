"""
@brief process string
@processstring

This class contains various string processing methods
"""

class StringTester:
  """
  """
  def __init__(self):
     pass
     
  def count_occurrence(self, to_search, stream) -> int:
    """
    @param: to_search: (String) The text to search for
    @param: stream: (StringIO) An in-memory stream for text I/O
    @return: (int) The number of lines that contain to_search
    """
    count = 0
    for str in stream:
      if to_search in str:
        count += 1
      
    return count     

if __name__ == '__main__':
    print('module only, not main')