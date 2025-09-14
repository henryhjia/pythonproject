"""
@booleanmask
@mask
use pythonproject/data/Admission_Predict.csv
Command usage: in pythonproject/
python3 -m mypandas.query_dataframe
"""
import sys
from pathlib import Path
import pandas as pd

from modules import common_module

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH  = BASE_DIR / 'data' / 'Admission_Predict.csv'

class PandaTester:
  def __init__(self, filename: str):
    self._filename = filename

  def read_csv(self):
    common_module.print_function(self.read_csv)
 
    print('++++++++++ data frame df with index column being the serial no')
    df = pd.read_csv(self._filename, index_col = 0)

    print('++++++++++ data frame df with column names all in lower case')
    df.columns = [x.lower().strip() for x in df.columns]
    print(df.head())

    print('++++++++++ chance of admit column > 0.7')
    admit_mask = df['chance of admit'] > 0.7
    print('mask=',admit_mask)

    print('++++++++++ isnull() mask')
    null_mask = df.isnull()
    print(null_mask.head(10))

    print('++++++++++ where value > 0.7')    
    print(df.where(admit_mask).head())

    print('++++++++++ where value > 0.7 with NaN removed method 1')       
    print(df.where(admit_mask).dropna().head())

    print('++++++++++ where value > 0.7 with NaN removed method 2') 
    print(df[df['chance of admit'] > 0.7].head())

    print('++++++++++ two bitmasks, chance of admit > 0.7 & change of admit < 0.9') 
    new_df = (df['chance of admit'] > 0.7) & (df['chance of admit'] < 0.9)
    print(new_df)

    print(df['chance of admit'].gt(0.7) & df['chance of admit'].lt(0.9))
    print(df['chance of admit'].gt(0.7).lt(.09))

    print('++++++++++ gre score > 320 & toefl score > 110, note: backticks is used for the column name')     
    result = df.query('(`gre score` > 320) & (`toefl score` > 110)')
    print(result)

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