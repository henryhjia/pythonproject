"""
1. Read input_dict.json, input_list_of_dict.json, input_list_of_list.json
   Take one file each run
2. Populate self._input_dict, self._input_list_of_dict, self._unput_list_of_list
3. Print
4. Write to new json files

Usage: python -m pythonproject.intermediate.populate_dict_list_from_json ../data/input_dict.json

"""
import json
import sys

from os.path import exists

class Person:
  """
  @brief
  """

  def __init__(self, filename: str) -> None:
    """
    @brief constructor
    """
    self._filename = filename

    # following data are read from input_dict.json, input_list_of_dict.json, input_list_of_list.json    
    self._input_dict = {}
    self._input_list_of_dict = []
    self._input_list_of_list = []

  def read_json_dict(self) -> None:
    """
    Read input_dict.json
    Populate self._input_dict
    """
    print('*********** read_json_dict()')
    self._input_dict = json.load(open(self._filename, 'r'))

  def read_json_list_of_dict(self) -> None:
    """
    Read input_list_of_dict.json
    Populate self._input_list_of_dict
    """
    print('*********** read_json_list_of_dict()')
    self._input_list_of_dict = json.load(open(self._filename, 'r'))

  def read_json_list_of_list(self) -> None:
    """
    Read input_list_of_list.json
    Populate self._input_list_of_list
    """
    print('*********** read_json_list_of_list()')
    self._input_list_of_list = json.load(open(self._filename, 'r'))

  def print_data(self) -> None:
    """
    print data:
    self._input_dict,
    self._input_list_of_list
    self._input_list_of_dict
    """
    print('*********** print_data()')

    print('+++++ formated self._input_dict read from input_dict.json file:')
    for key, value in self._input_dict.items():
      print('key=',
            format(key, '10s'),
            'value=',
            format(value[0], '10s'),
            format(value[1], '3d'),
            format(value[2], '8.3f'),
            format(value[3], '13.6'))

    print(f'\n+++++ formated self._input_list_of_list read from input_list_of_list.json file:')
    for i in self._input_list_of_list:
      print(format(i[0],'10s'),
            format(i[1], '3d'),
            format(i[2], '8.3f'),
            format(i[3], '13.6f'))

    print(f'\n+++++ formated self._input_list_of_dict read from input_list_dict.json file:')
    for i in self._input_list_of_dict:
      for key, value in i.items():
        print('key=',
              format(key, '10s'),
              'value=',
              format(value[0], '10s'),
              format(value[1], '3d'),
              format(value[2], '8.3f'),
              format(value[3], '13.6'))

  def write_json(self) -> None:
    """
    """
    print('\n*********** write_json()')
    with open('output_dict.json', 'w') as outfile:
      json.dump(self._input_dict, outfile)
    outfile.close()

    json_string = json.dumps(self._input_list_of_list)
    with open('output_list_of_list.json', 'w') as outfile:
      outfile.write(json_string)
    outfile.close()

    json_string = json.dumps(self._input_list_of_dict)
    with open('output_list_of_dict.json', 'w') as outfile:
      outfile.write(json_string)
    outfile.close()

def main(args=None) -> None:
  """
  """
  if args is None:
    args = []
  print(f'length of argument : {len(args)}')
  if len(args) < 2:
    print('usage:', args[0], '../data/input_dict.json')
    exit(1)

  config = args[1]

  file_exist = exists(config)

  if not file_exist:
    print(f'{config} does not exist, exiting')
    exit(1)

  me = Person(config)

  # read json dict input_dict.json files
  if 'input_dict.json' in config:
    me.read_json_dict()

  elif 'input_list_of_dict' in config:
    # read json list of dictionary file
    me.read_json_list_of_dict()

  elif 'input_list_of_list' in config:
    # read json dictionary file
    me.read_json_list_of_list()

  # print data _dict, _list_of_list, _list_of_dict (all read from test.txt)
  me.print_data()

  # write to json files
  me.write_json()

if __name__ == '__main__':
  main(sys.argv)
