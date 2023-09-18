#!/use/bin/python3
import pandas as pd
import sys
import matplotlib
import matplotlib.pyplot as plt

def main():
  """
  """
  print('pandas test 2')

  mydataset = {'cars': ["BMW", "Volvo", "Ford"],'passings': [3,7,21] }

  myvar = pd.DataFrame(mydataset)

  print('+++++++++++++++ DataFrame:')
  print(myvar)

  df1 = pd.DataFrame({'Product ID': [1, 2, 3, 4], 'Product Name':['jia','hong','jie','cheng'], 'Color':['red','blue','yellow','pink']})
  print(df1)

  df2 = pd.DataFrame([
    [1, 'San Diego', 100],
    [2, 'Los Angeles', 120],
    [3, 'San Francisco', 90],
    [4, 'Sacramento', 115]
  ],
    columns=[
      #add column names here
      'Store ID', 'Location','Number of Employees'
    ])

  print(df2)
if __name__ == "__main__":
  main()    