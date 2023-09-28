#!/use/bin/python3
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
 
    print('++++++++++ original data frame df')
    df = pd.read_csv(self._filename)
    print(df.head())

    print('++++++++++ data frame df with index column being the serial no')
    df = pd.read_csv(self._filename, index_col = 0)
    print(df.head())

    print('++++++++++ replace column name')
    new_df=df.rename(columns={'SOP':'new sop'})
    print(new_df.head())
    print(new_df.columns)

    print('++++++++++ remove space from column name')
    new_df = df.rename(mapper=str.strip, axis = 'columns')
    print(new_df.head())
    print(new_df.columns)

    print('++++++++++ make all column names to be lower case')
    cols = list(df.columns)
    cols = [x.lower().strip() for x in cols]
    df.columns = cols
    print(df.head())


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