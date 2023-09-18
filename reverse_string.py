#!/use/bin/python3
"""
Reverse string
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
  def reverse_data(self) -> None:
    """
    1. Reverse string
    """

    my_string = 'google'

    reversed_string = my_string[::-1]
    print('original string=', my_string)
    print('reversed string=', reversed_string)

  def reverse_data2(self) -> None:
    my_string = 'google'
    reverse_string=''

    str_len=len(my_string)
    for i in range(str_len):
      reverse_string += my_string[str_len-1-i]
    
    print('reversed string=', reverse_string)

def main() -> int:

  me = ReverseStringTester()

  # reverse data from variables
  me.reverse_data()
  me.reverse_data2()

if __name__ == '__main__':
  main()