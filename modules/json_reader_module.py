#!/use/bin/python3
"""
json reader 
@jsonreader
"""
import json
import os

class JsonReader:
  """
  """

  def __init__(self, filename):
    """
    """
    self._filename = filename

    self._input_dict = {}
    self._input_list_of_dict = []
    self._input_list_of_list = []

    self._data_list = []
    self._data_dict = {}
    self._data_type = None

    self._data = None

    print(self._filename)
    pass

  def read_json_dict(self) -> None:
    """
    Read input_dict.json
    Populate self._input_dict
    """
    print('*********** read_json_dict()')  
    self._input_dict = json.load(open('input_dict.json', 'r'))

  def read_json_list_of_dict(self) -> None:
    """
    Read input_list_of_dict.json
    Populate self._input_list_of_dict
    """
    print('*********** read_json_list_of_dict()')     
    self._input_list_of_dict = json.load(open('input_list_of_dict.json', 'r'))

  def read_json_list_of_list(self) -> None:
    """
    Read input_list_of_list.json
    Populate self._input_list_of_list
    """
    print('*********** read_json_list_of_list()')
    self._input_list_of_list = json.load(open('input_list_of_list.json', 'r'))

  def read_json_data(self):
    if os.path.isfile(self._filename):      
      self._data = json.load(open(self._filename, 'r'))

    else:
      print(self._filename, ' does not exit')
      exit(1)

  def read_json(self):

    print('\n*********** read_json(), json_file=', self._filename)
    if os.path.isfile(self._filename):      
      data = json.load(open(self._filename, 'r'))
      if type(data) == list:
        print('list')
        self._data_list = data
        self._data_type = list
      elif type(data) == dict:
        print('dict')
        self._data_dict = data
        self._data_type = dict
    else:
      print(self._filename, ' does not exit')
      exit(1)

  def print_json_data(self):
    print(self._data)
    
  def print_data(self):
    if self._data_type == list:
      for item in self._data_list:
        print(item)
    elif self._data_type == dict:    
      for key, value in self._data_dict.items():
        print(key, value)

  def print_formated_data(self):
    if self._data_type == list:
      for item in self._data_list:
        for key, value in item.items():
          print(f'{key:10s} {value[0]:10s} {value[1]:5d} {value[2]:4d}')
    elif self._data_type == dict:
      for key, value in self._data_dict.items():
        print(f'{key:10s} {value[0]:8s} {value[1]:6d} {value[2]:10.2f} {value[3]:10.2f}')

if __name__ == '__main__':
    print('module only, not main')