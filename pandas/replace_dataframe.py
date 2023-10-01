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
  def __init__(self, filename):
    self._filename = filename
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

  def read_csv(self):
    common_module.print_function(self.read_csv)    
    df=pd.read_csv(self._filename)
    print(df.head())

    df["First"]=df['President']
    print(df.head())

    df["First"]=df["First"].replace("[ ].*", "", regex=True)
    print(df.head())

  def splitname(self, row: pd.Series) -> pd.Series:
    row['First']=row['President'].split(" ")[0]
    row['Last']=row['President'].split(" ")[-1]
    return row

  def splitage(self, row: pd.Series) -> pd.Series:
    row['Age'] = row['Age'].split(",")[0]
    return row

  def separate_first_last(self) -> None:
    common_module.print_function(self.separate_first_last)
    df=pd.read_csv(self._filename)
    df=df.apply(self.splitname, axis='columns')
    print(df.head())

  def clean_age(self) -> None:
    common_module.print_function(self.clean_age)
    df=pd.read_csv(self._filename)
    print(df.head())
    df=df.apply(self.splitage, axis='columns')
    print(df.head())


def main(args: list=None) -> int:
  print(f'lengh of argument : {len(args)}')
  if len(args) < 2:
    print('usage:', args[0], 'some.csv')
    exit(1)

  try:
    me = PandaTester(args[1])
    me.replace_element()
    me.read_csv()
    me.separate_first_last()
    me.clean_age()

  except Exception as e:
    print(e)

if __name__ == '__main__':
  main(sys.argv)  