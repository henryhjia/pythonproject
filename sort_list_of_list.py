#!/use/bin/python3
"""
Sort list of list
"""

class SortTester:
  """
  """
  def sort_data(self) -> None:
    """
    1. Sort list of list
    """
    print('\n*********** sort_data()')   
    print('\n*********************** sort list of list')   
    my_list = [
      [1,2,3],
      [3,2,1],
      [2,5,5],
      [0,1,4]
    ]

    for i in my_list:
      print(i)

    sorted_list = sorted(my_list, key=lambda x:x[0])
    print('sort based on x[0]')
    for i in sorted_list:
      print(i)

    sorted_list = sorted(my_list, key=lambda x:x[1])
    print('sort based on x[1]')
    for i in sorted_list:
      print(i)

    sorted_list = sorted(my_list, key=lambda x:x[2])
    print('sort based on x[2]')
    for i in sorted_list:
      print(i)

def main() -> int:

  me = SortTester()

  # sort data from variables
  me.sort_data()


if __name__ == '__main__':
  main()