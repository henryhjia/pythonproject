#!/use/bin/python3
"""
@brief Reverse string
@reversestring

Two methods:
1. string slicing
2. manual

In Python, strings do not have a built-in reverse() method. Unlike lists, strings 
are immutable, which means their contents cannot be modified after creation. 
Therefore, strings DO NOT have methods like reverse() that would alter the 
order of characters in-place.

If you want to reverse a string, you can achieve it using slicing
"""

class ReverseStringTester:
  """
  """
  def reverse_data_using_slicing(self, in_str) -> str:
    """
    1. Reverse string
       NOTE: string does not have build-in reverse method
    """
    reversed_string = in_str[::-1]
    return reversed_string

  def reverse_data_manually(self, in_str) -> str:

    reverse_string=''
    str_len=len(in_str)
    for i in range(str_len):
      reverse_string += in_str[str_len-1-i]
    
    return reverse_string
  
if __name__ == '__main__':
    print('module only, not main')