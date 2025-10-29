"""
Get sum of a sub list by slicing the list
Usage: pythonproject/ python -m advanced.get_list_moving_total

"""
import list_process_module
    
def main():
  me = list_process_module.ListProcessModule()
  print(me.list_moving_total_contains([1, 2, 3, 4], 3, 6))
  print(me.list_moving_total_contains([1, 2, 3, 4], 3, 9))
  print(me.list_moving_total_contains([1, 2, 3, 4], 3, 12))
  print(me.list_moving_total_contains([1, 2, 3, 4], 3, 7))
  
  print(me.list_moving_total_contains([1, 2, 3, 4, 5], 3, 6))
  print(me.list_moving_total_contains([1, 2, 3, 4, 5], 3, 9))
  print(me.list_moving_total_contains([1, 2, 3, 4, 5], 3, 12))
  print(me.list_moving_total_contains([1, 2, 3, 4, 5], 3, 7))

if __name__ == "__main__":
  main()