#!/use/bin/python3
"""
Sort list
@sortlist

Two methods:
l2 = sorted(l1) - create a new list that is sorted
l1.sort() - in place sort

"""
import list_sort_module

def main() -> int:

  me = list_sort_module.SortListTester()

  # Use sorted() method
  me.sort_sorted()

  # Use .sort() inplace sort
  me.sort_in_place_sort()

  # Sort integers in a mixed data list, and keep unique
  me.sort_integer_unique_mixed_data_type_in_list()

if __name__ == '__main__':
  main()