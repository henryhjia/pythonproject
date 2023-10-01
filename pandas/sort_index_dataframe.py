"""
@sort
@sortindex
"""
import pandas as pd
import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import common_module
from os.path import exists

class PandaTester:
  def __init__(self, filename: str):
    self._filename = filename

  def read_csv(self):
    common_module.print_function(self.read_csv)
 
    print('++++++++++ data frame df')       
    df = pd.read_csv(self._filename)
    print(df.head(20))

    print('++++++++++ set time as index and then sort index')     
    df = df.set_index('time')
    df = df.sort_index()         
    print(df.head(20))


def main(args: list=None) -> int:
  print(f'lengh of argument : {len(args)}')
  if len(args) < 2:
    print('usage:', args[0], 'some.csv')
    exit(1)

  try:
    me = PandaTester(args[1])
    me.read_csv()

  except Exception as e:
    print(e)

if __name__ == '__main__':
  main(sys.argv)  