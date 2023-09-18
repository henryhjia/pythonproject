#!/use/bin/python3
"""
test program
advanced sorting for list of complex dictionaries from dad_mom.json
"""
import json
import os
import sys
from os.path import exists

class JsonTester:
  """
  """

  def __init__(self):

    self._input_list_of_dict = []

  def read_json_config(self, json_file: str) -> None:
    """
    """
    print('\n*********** read_json_config(), json_file=', json_file)
    if os.path.isfile(json_file):      
      self._input_list_of_dict = json.load(open(json_file, 'r'))
    else:
      print(json_file, ' does not exit')
      exit(1)

  def sort_data_from_json_file(self) -> None:
    """
    """
    print('\n*********** sort_data_from_json_file()')   

    print('self._input_list_of_dict=', self._input_list_of_dict)

    try:
      sorted_list = sorted(self._input_list_of_dict, key=lambda x:x[list(x.keys())[0]][1])     
      print('sort by value 1:', sorted_list)

      sorted_list = sorted(self._input_list_of_dict, key=lambda x:x[list(x.keys())[0]][2])     
      print('sort by value 2:', sorted_list)

      sorted_list = sorted(self._input_list_of_dict, key=lambda x:x[list(x.keys())[0]][0])     
      print('sort by value 0:', sorted_list)

      sorted_list = sorted(self._input_list_of_dict, key=lambda d: list(d.keys())[0])     
      print('sort by key:    ', sorted_list)
    
    except Exception as err:
      print('Error happened:', err)


def main(args: list=None) -> int:
  print(f'lengh of argument : {len(args)}')
  if len(args) < 2:
    print('usage:', args[0], 'dad_mom.json')
    exit(1)

  json_file = args[1]

  file_exist = exists(json_file)

  if not file_exist:
    print(f'{json_file} does not exist, exiting')
    exit(1)

  me = JsonTester()
  # read json json_file
  me.read_json_config(json_file)

  # sort list of dictionary based on value
  me.sort_data_from_json_file()

if __name__ == '__main__':
  main(sys.argv)