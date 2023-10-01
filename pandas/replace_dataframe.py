"""
@replace
"""
import pandas as pd
import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import common_module
from os.path import exists

class PandaTester:
  def __init__(self):
    self._mydata = pd.DataFrame({
                  'A': [1, 1, 2, 3, 4],
                   'B': [3, 6, 3, 8, 9],
                   'C': ['a', 'b', 'c', 'd', 'e']
                   })


  def replace_element(self):
    print('+++++++++++ original dataframe')
    print(self._mydata)

    print('+++++++++++ replace 1 with 100')
    print(self._mydata.replace(1, 100))

    print('+++++++++++ replace 1, 3 with 100, 300')
    print(self._mydata.replace([1,3], [100,300]))



    pass
    
def main() -> int:

  me = PandaTester()
  me.replace_element()


if __name__ == '__main__':
  main()  