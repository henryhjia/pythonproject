#!/use/bin/python3
import pandas as pd
import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import common_module

class PandaTester:
  def __init__(self, filename):
    self._filename = filename

  def read_dataframe_from_csv(self):
    common_module.print_function(f'{self.read_dataframe_from_csv}, {self._filename}')
    df = pd.read_csv(self._filename)
    print(df.head())

    df = pd.read_csv(self._filename, index_col=0)
    print(df.head())

    print(df.columns)
     
    df_copy = df.rename(columns={'LOR ': 'Letter of Recommendation'})
    print(df_copy.head())

def main(args: list=None) -> int:
  """
  """
  print(f'lengh of argument : {len(args)}')
  if len(args) < 2:
    print('usage:', args[0], 'data.csv')
    exit(1)

  me = PandaTester(args[1])
  me.read_dataframe_from_csv()

if __name__ == "__main__":
  main(sys.argv) 