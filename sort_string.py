#!/use/bin/python3
"""
Sort string
@sortstring

To sort the characters of the string 'google' in alphabetical order, you can use the sorted() 
function to create a sorted list of characters and then join() them back into a string.
"""

class SortStringTester:
  """
  """
  def sort_data(self) -> None:
    """
    1. Sort string
    """

    my_string = 'google'

    sorted_list = sorted(my_string)
    print(sorted_list)

    sorted_string = ''.join(sorted_list)

    print('sorted_string=', sorted_string)

def main() -> int:

  me = SortStringTester()

  # sort data from variables
  me.sort_data()


if __name__ == '__main__':
  main()