# Get sum of a sub list by slicing the list

import list_process_module
    
def main():
  me = list_process_module.ProcessList()
  print(me.list_moving_total_contains([1, 2, 3, 4], 6))
  print(me.list_moving_total_contains([1, 2, 3, 4], 9))
  print(me.list_moving_total_contains([1, 2, 3, 4], 12))
  print(me.list_moving_total_contains([1, 2, 3, 4], 7))
  
  print(me.list_moving_total_contains([1, 2, 3, 4, 5], 6))
  print(me.list_moving_total_contains([1, 2, 3, 4, 5], 9))
  print(me.list_moving_total_contains([1, 2, 3, 4, 5], 12))
  print(me.list_moving_total_contains([1, 2, 3, 4, 5], 7))

if __name__ == "__main__":
  main()