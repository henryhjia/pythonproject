"""
@sort
@sortindex
use log.csv
"""
import sys
from pathlib import Path
import pandas as pd
from modules import common_module

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH  = BASE_DIR / 'data' / 'log.csv'

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

    print('++++++++++ use time and user as indexes')    
    df = df.reset_index()
    df = df.set_index(['time', 'user'])
    print(df.head(20))
    
def main(args: list=None) -> None:
  print(f'length of argument : {len(args)}')
  if len(args) < 2:
    print('usage:', args[0], 'some.csv')
    args.append(DATA_PATH)
    print(args)


  try:
    me = PandaTester(args[1])
    me.read_csv()

  except Exception as e:
    print(e)

if __name__ == '__main__':
  main(sys.argv)  