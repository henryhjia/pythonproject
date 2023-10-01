"""
@extract
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

  def read_csv_extract_data(self):
    common_module.print_function(self.read_csv_extract_data)    
    df=pd.read_csv(self._filename)
    print(df.head())

    # pattern="(^[\w]*)(?:.* )([\w]*$)"
    pattern="(?P<First>^[\w]*)(?:.* )(?P<Last>[\w]*$)"

    names = df["President"].str.extract(pattern)
    print(names.head())

    df["First"]=names["First"]
    df["Last"]=names["Last"]
    print(df.head())

    df["Born"]=df["Born"].str.extract("([\w]{3} [\w]{1,2}, [\w]{4})")
    print(df["Born"].head())

    df["Born"]=pd.to_datetime(df["Born"])
    print(df["Born"].head())

    df["Age"]=df["Age"].str.extract("^[\w]*")
    print(df["Age"].head())


def main(args: list=None) -> int:
  print(f'lengh of argument : {len(args)}')
  if len(args) < 2:
    print('usage:', args[0], 'some.csv')
    exit(1)

  try:
    me = PandaTester(args[1])
    me.read_csv_extract_data()

  except Exception as e:
    print(e)

if __name__ == '__main__':
  main(sys.argv)  