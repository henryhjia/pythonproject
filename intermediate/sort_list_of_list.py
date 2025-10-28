#!/use/bin/python3
"""
Sort list of list
@sortlistoflist

Usage: in pythonproject/ run python -m intermediate.sort_list_of_list

"""
from modules import list_sort_module

def main() -> None:

  me = list_sort_module.ListSortModule()

  # sort data from variables
  my_list = [
    [1,2,3],
    [3,2,1],
    [2,5,5],
    [0,1,4]
  ]

  print(my_list)

  # Sort the list based on the index 0 of the sublist
  result = me.sort_list_of_list(my_list, 0)
  print(result)

  # Sort the list based on the index 1 of the sublist
  result = me.sort_list_of_list(my_list, 1)
  print(result)

  # Sort the list based on the index 2 of the sublist
  result = me.sort_list_of_list(my_list, 2)
  print(result)


if __name__ == '__main__':
  main()