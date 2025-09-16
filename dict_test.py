from typing import Any, Dict, List

import matplotlib.pyplot as plt


class DictTest:
  """
  data example:
    'jia': [{100.1: 10}, {100.2: 20}]
    'henry': [{222,2: 15}, {203.5: 10}, {200.6: 14}]
  """
  def __init__(self) -> None:
    self.input_list: List[Dict] = []
    self.master_dict: Dict[str, List[Dict[float, int]]] = {}
    self.output_file = open('dict_test.txt')

  def __del__(self) -> None:
    self.output_file.close()
    
  def add_data(self, name: str, msg: Any, timestamp: float) -> None:
    tmp_dict = { 'name': name, 'msg': msg, 'timestamp': timestamp }
    self.input_list.append(tmp_dict)
    out_str = f'{timestamp},{name},{len(msg)}'
    self.output_file.write(out_str)
    self.output_file.write('\n')

  def process(self) -> None:
    for item in self.input_list:
      tmp_dict = {}
      msg = item['msg']
      name = item['name']
      timestamp = item['timestamp']
      tmp_dict[timestamp] = len(msg)
      if name not in self.master_dict:
        self.master_dict[name] = [tmp_dict]
      else:
        self.master_dict[name].append(tmp_dict)

  def post_process(self) -> None:
    color = ['ro','go','bo']
    plt.figure(figsize=(8,8))
    plt.xlabel('time')
    plt.ylabel('length')
    plt.title('test title')
    plt.grid(True)

    count = 0
    for key, value in self.master_dict.items():
      x = []
      y = []
      for elem in value:
        x.append(list(elem.keys())[0])
        y.append(list(elem.values())[0])    
      plt.plot(x,y,color[count],label=key,markersize=1)
      plt.legend(loc='upper left')
      count += 1

    plt.show()

  if __name__ == '__main__':
    print('module only, not main')