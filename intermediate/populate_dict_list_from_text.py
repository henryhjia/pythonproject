"""
1. Read family.txt file and populate _dict, _list_of_dict, _list_of_list
2. Print these data structures

Usage: in pythonproject/ python -m intermediate.populate_dict_list_from_text ../data/family.txt

"""
import sys

from os.path import exists

class Family:
  """
  @brief
  """

  def __init__(self, filename) -> None:
    """
    @brief constructor
    """
    self._filename = filename

    # following data are read from test.txt file
    self._dict = {}           # dictionary {key, list}    
    self._list_of_list = []   # list of list
    self._list_of_dict = []   # list of dictionary {key, list}

  def read_text_data(self) -> None:
    """
    read a text file:
      henry,100,20.68,128.29384
      jean,20,10.56,235.893455
      claire,25,56.446,1335.124567
      maggie,13,89.123,2235.345512     
      
    populate three data structures:
      self._dict
      self._list_of_list
      self._list_of_dict
    """
    print('\n*********** read_text_data()', self._filename)    
    input_file = open(self._filename,'r')
    item_list = []
    item_list2 = []
    temp_dict = {}
    for line in input_file:
      line_no_newline = line.strip()
      item_list = line_no_newline.split(',')
      print(item_list)
      for me in item_list:
        if me.isdigit():
          item_list2.append(int(me))
        elif me.replace('.','').isdigit():
          item_list2.append(float(me))
        else:
          item_list2.append(me)

      value_list = item_list2[1::]

      # self._dict
      daughter_list = []
      key = item_list2[0]
      if key in self._dict:
        daughter_list.append(self._dict[key])
        del(self._dict[key])
        daughter_list.append(value_list.copy())
        self._dict[key] = daughter_list
      else:
        self._dict[key] = value_list

      # self._list_of_list
      self._list_of_list.append(item_list2.copy())

      # self._list_of_dict
      temp_dict[key] = value_list.copy()
      self._list_of_dict.append(temp_dict.copy())    

      # cleaning
      temp_dict.clear()
      item_list2.clear()

    input_file.close()

  def print_data(self) -> None:
    """
    print data:
    _dict,
    _list_of_list
    _list_of_dict

    Check if an item is a list or a nested list by using 
      if any(isinstance(item, list) for item in value):
        print('list of list')
        
    """
    print('\n*********** print_data()')    

    print(f'+++++ formated self._dict read from {self._filename} file:')
    for key, value in self._dict.items():
      if any(isinstance(item, list) for item in value):
        for item in value:
          print('key=', 
              format(key, '10s'),           
              'value=',
              format(item[0], '10s'), 
              format(item[1], '3d'),
              format(item[2], '8.3f'),
              format(item[3], '13.6'))

      else:
        print('key=', 
              format(key, '10s'), 
              'value=',
              format(value[0], '10s'), 
              format(value[1], '3d'),
              format(value[2], '8.3f'),
              format(value[3], '13.6'))

    print(f'\n+++++ formated self._list_of_list read from {self._filename} file:')
    for i in self._list_of_list:
      print(format(i[0],'10s'), 
            format(i[1],'10s'), 
            format(i[2], '3d'), 
            format(i[3], '8.3f'),
            format(i[4], '13.6f'))

    print(f'\n+++++ formated self._list_of_dict read from {self._filename} file:')
    for i in self._list_of_dict:
      for key, value in i.items():
        print('key=', 
              format(key, '10s'),
              'value=',
              format(value[0], '10s'), 
              format(value[1], '3d'),
              format(value[2], '8.3f'),                            
              format(value[3], '13.6')) 


def main(args=None) -> None:
  """
  """
  if args is None:
    args = []
  print(f'length of argument : {len(args)}')
  if len(args) < 2:
    print('usage:', args[0], '../data/family.txt')
    exit(1)

  config = args[1]

  file_exist = exists(config)

  if not file_exist:
    print(f'{config} does not exist, exiting')
    exit(1)

  me = Family(config)

  # read test.txt and populate _dict, _list_of_list, _list_of_dict
  me.read_text_data()

  # print data _dict, _list_of_list, _list_of_dict (all read from test.txt)
  me.print_data()


if __name__ == '__main__':
  main(sys.argv)
