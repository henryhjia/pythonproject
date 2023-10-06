"""
@sgroup
use census.csv
"""
import pandas as pd
import sys
import numpy as np
import common_module
from os.path import exists

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
                

def main(args: list=None) -> int:
  print(f'lengh of argument : {len(args)}')
  if len(args) < 2:
    print('usage:', args[0], 'some.csv')
    exit(1)

  try:
    me = PandaTester(args[1])
    me.read_csv()
    me.group_by()


  except Exception as e:
    print(e)

if __name__ == '__main__':
  main(sys.argv)  