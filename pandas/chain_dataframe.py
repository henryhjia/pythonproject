"""
@booleanmask
@mask
@chain
@apply
@lambda
@displaycolumns
use census.csv
"""
import pandas as pd
import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import common_module
from os.path import exists
import timeit

class PandaTester:
  def __init__(self, filename: str):
    self._filename = filename

  def get_state_region(self, x: str) -> str:
      northeast = ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 
                  'Rhode Island','Vermont','New York','New Jersey','Pennsylvania']
      midwest = ['Illinois','Indiana','Michigan','Ohio','Wisconsin','Iowa',
                'Kansas','Minnesota','Missouri','Nebraska','North Dakota',
                'South Dakota']
      south = ['Delaware','Florida','Georgia','Maryland','North Carolina',
              'South Carolina','Virginia','District of Columbia','West Virginia',
              'Alabama','Kentucky','Mississippi','Tennessee','Arkansas',
              'Louisiana','Oklahoma','Texas']
      west = ['Arizona','Colorado','Idaho','Montana','Nevada','New Mexico','Utah',
              'Wyoming','Alaska','California','Hawaii','Oregon','Washington']
      
      if x in northeast:
          return "Northeast"
      elif x in midwest:
          return "Midwest"
      elif x in south:
          return "South"
      else:
          return "West"
    
  def read_csv(self):
    common_module.print_function(self.read_csv)
 
    print('++++++++++ data frame df')
    df = pd.read_csv(self._filename)
    print(df.head())

    print('++++++++++ where SUMEV == 50')
    df = df.where(df['SUMLEV']==50)
    print(df.head())

    print('++++++++++ dropna')
    df = df.dropna()
    print(df.head())

    # df[df['SUMLEV']==50] is same as df.where(df['SUMLEV']==50).dropna()

    print('++++++++++ set_index STNAME, CTYNAME')
    df = df.set_index(['STNAME','CTYNAME'])
    print(df)

    print('++++++++++ rename column')
    df = df.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})
    print(df['Estimates Base 2010'])

  def chain_operation(self):
    common_module.print_function(self.chain_operation)
 
    print('++++++++++ data frame df with index column being the serial no')
    df = pd.read_csv(self._filename)
    print(df.head())

    df =(df.where(df['SUMLEV']==50)
        .dropna()
        .set_index(['STNAME','CTYNAME'])
        .rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'}))

    print(df)

  def test_apply_state_region(self):
    common_module.print_function(self.get_state_region)   

    print('++++++++++ original data frame df')  
    df = pd.read_csv(self._filename)
    print(df.head())

    df['state_region'] = df['STNAME'].apply(lambda x: self.get_state_region(x))
    print('++++++++++ column STNAME, and state_region')  
    print(df[['STNAME', 'REGION', 'state_region']].head())


def main(args: list=None) -> int:
  print(f'lengh of argument : {len(args)}')
  if len(args) < 2:
    print('usage:', args[0], 'some.csv')
    exit(1)

  try:
    me = PandaTester(args[1])
    me.read_csv()
    me.chain_operation()
    me.test_apply_state_region()

  except Exception as e:
    print(e)

if __name__ == '__main__':
  main(sys.argv)  