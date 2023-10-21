#!/use/bin/python3
"""
Sort list of list
@sortlistoflist
"""
import list_sort_module

def main() -> None:

  me = list_sort_module.ListSortModule()

  # sort data from variables
  my_list = [
    [1,2,3],
    [3,2,1],
    [2,5,5],
    [0,1,4]
  ]

  result = me.sort_list_of_list(my_list, 0)


if __name__ == '__main__':
  main()