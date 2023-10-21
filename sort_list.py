#!/use/bin/python3
"""
Sort list
@sortlist

Two methods:
l2 = sorted(l1) - create a new list that is sorted
l1.sort() - in place sort

"""
import list_sort_module

def main() -> None:

  me = list_sort_module.ListSortModule()

  # Use sorted() method
  l1 = [10, 9,4,6,20,1]
  l2 = me.sort_sorted(l1)
  print('original list=', l1)
  print('sorted list=', l2)

  l1 = ['henry', 'bob', 'jack', 'kate']
  l2 = me.sort_sorted(l1)
  print('original list=', l1)
  print('sorted list=', l2)

  # Use .sort() inplace sort
  l1 = [10, 9,4,6,20,1]
  print('original list=', l1)  
  l2 = me.sort_in_place_sort(l1)
  print('original list changed to=', l1)
  print('sorted list=', l2)

  l1 = ['henry', 'bob', 'jack', 'kate']
  print('original list=', l1)  
  l2 = me.sort_in_place_sort(l1)
  print('original list changed to=', l1)
  print('sorted list=', l2)

  # Sort integers in a mixed data list, and keep unique
  mylist = [3,2,1,10,6,7,2,1,"jia",'c']
  result = me.sort_integer_unique_mixed_data_type_in_list(mylist)
  print('original list=', mylist)
  print('result=', result)

  # sort list of dictionary
  my_list_of_dict = [
    {'name':'Sam', 'number': 11}, 
    {'name':'Jan', 'number': 1},
    {'name':'Kate', 'number':9},
    {'name':'Bob', 'number':13}
  ]
  print(my_list_of_dict)
  result = me.sort_list_of_dictionary_by_value(my_list_of_dict)
  print(result)

  result = me.sort_list_of_dictionary_by_key(my_list_of_dict)
  print(result)

if __name__ == '__main__':
  main()