# !/use/bin/python3
"""
@brief Sort string
@sortstring

To sort the characters of the string 'google' in alphabetical order, you can use the sorted() 
function to create a sorted list of characters and then join() them back into a string.
"""

class SortStringTester:
  """
  """
  def __init__(self):
     pass
  
  def sort_data(self, input_string: str) -> str:
    """
    1. Sort string
    """

    sorted_list = sorted(input_string)
    print(sorted_list)
    sorted_string = ''.join(sorted_list)
    print('sorted_string=', sorted_string)

    return sorted_string

  def sort_alpha_digit(self, input_string: str) -> str:
    # sort both alphabet and digit string with these criterias:
    # 1. lower case letter before upper case letter
    # 2. alphebet before digit
    # 3. odd digit before even digit
    # an example: Sorted1234
    # result: deortS1324
    l1 = []
    l2 = []
    l3 = []
    l4 = []

    for char in input_string:
        if char.isdigit():
          char_int = int(char)
          if char_int %2 == 0:
             l4.append(char_int)
          else:
             l3.append(char_int)
        elif char.islower():
           l1.append(char)
        elif char.isupper():
           l2.append(char)

    l1.sort()
    l2.sort()
    l3.sort()
    l4.sort()

    result = ''

    for elem in l1:
       result += elem
    
    for elem in l2:
       result += elem

    for elem in l3:
       result += str(elem)
      
    for elem in l4:
       result += str(elem)
      
    return result

if __name__ == '__main__':
    print('module only, not main')