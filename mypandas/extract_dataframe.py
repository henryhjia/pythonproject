"""
@extract
use presidents.csv
"""
import sys
from pathlib import Path

import pandas as pd

from modules import common_module

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH  = BASE_DIR / 'data' / 'presidents.csv'

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


def main(args: list=None) -> None:
  print(f'length of argument : {len(args)}')
  if len(args) < 2:
    print('usage:', args[0], 'some.csv')
    args.append(DATA_PATH)
    print(args)

  try:
    me = PandaTester(args[1])
    me.read_csv_extract_data()

  except Exception as e:
    print(e)

if __name__ == '__main__':
  main(sys.argv)  