"""
@sgroup
use census.csv
"""
import sys
from pathlib import Path
import numpy as np
import pandas as pd
from modules import common_module

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH  = BASE_DIR / 'data' / 'census.csv'

class PandaTester:
  def __init__(self, filename: str):
    self._filename = filename

  def read_csv(self):
    """
    census.csv
    """
    common_module.print_function(self.read_csv)
 
    print('++++++++++ data frame df')       
    df = pd.read_csv(self._filename)
    df = df[df['SUMLEV']==50]
    print(df.head())

    for state in df['STNAME'].unique():
        avg = np.average(df.where(df['STNAME']==state).dropna()['CENSUS2010POP'])
        print('Counties in state ' + state + 
              ' have an average population of ' + str(avg))

  def group_by(self):
    """
    census.csv
    """
    print('++++++++++ data frame df')       
    df = pd.read_csv(self._filename)
    df = df[df['SUMLEV']==50]
    print(df.head())

    for group, frame in df.groupby('STNAME'):
        avg = np.average(frame['CENSUS2010POP'])
        print('Counties in state ' + group + 
              ' have an average population of ' + str(avg))
                

def main(args: list=None) -> None:
  print(f'length of argument : {len(args)}')
  if len(args) < 2:
    print('usage:', args[0], 'some.csv')
    args.append(DATA_PATH)
    print(args)

  try:
    me = PandaTester(args[1])
    me.read_csv()
    me.group_by()


  except Exception as e:
    print(e)

if __name__ == '__main__':
  main(sys.argv)  