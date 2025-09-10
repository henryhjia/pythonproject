"""
@booleanmask
@mask
@index
@multilevelindex
use census.csv
"""
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
 
    print('++++++++++ data frame df with index column being the serial no')       
    df = pd.read_csv(self._filename, index_col = 0)
    print(df.head())

    # copy indexed data into its own column
    print('++++++++++ copy serial no, then set chance of admit as index')
    df['Serial Number'] = df.index
    df = df.set_index('Chance of Admit ')
    print(df.head())

    # reset index
    print('++++++++++ reset index')    
    df = df.reset_index()
    print(df.head())

  def read_census_csv(self):
    df = pd.read_csv(self._filename)
    print(df.head())

    print('++++++++++ SUMLEV unique')  
    print(df['SUMLEV'].unique())
    print('++++++++++ REGION unique')  
    print(df['REGION'].unique())

    print('++++++++++ df=df[df[\'SUMLEV\'] == 50')
    df = df[df['SUMLEV'] == 50]
    print(df.head())

    columns_to_keep = ['STNAME','CTYNAME','BIRTHS2010', 'BIRTHS2011', 'BIRTHS2012', 'BIRTHS2013', 
                       'BIRTHS2014', 'BIRTHS2015', 'POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2011',
                       'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']

    print('++++++++++ keep certain columns')
    df = df[columns_to_keep]
    print(df.head())
    
    print('++++++++++ set_index[STNAME, CTYNAME]')    
    df = df.set_index(['STNAME','CTYNAME'])
    print(df.head())

    print('++++++++++ result from Michigan state and Washtenaw county as due index') 
    print(df.loc['Michigan','Washtenaw County'])

    print('++++++++++ result from Michigan state') 
    print(df.loc['Michigan'])

def main(args: list=None) -> int:
  print(f'lengh of argument : {len(args)}')
  if len(args) < 2:
    print('usage:', args[0], 'some.csv')
    exit(1)

  try:
    me = PandaTester(args[1])
    # me.read_csv()
    me.read_census_csv()

  except Exception as e:
    print(e)

if __name__ == '__main__':
  main(sys.argv)  