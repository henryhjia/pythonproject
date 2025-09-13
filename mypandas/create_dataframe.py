# if run in terminal:
# in pythonproject/
# python3 -m mypandas.create_dataframe

from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from modules import common_module
import os

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH1  = BASE_DIR / 'data' / 'data.csv'
DATA_PATH2  = BASE_DIR / "data" / "data.json"
DATA_PATH3  = BASE_DIR / "data" / "data_missing_data.csv"

class PandaTester:
  def __init__(self):
    pass

  def create_dataframe(self):
    common_module.print_function(self.create_dataframe)

    # create a dataframe from a list
    mylist = [10,20,30,40,50]
    mydf = pd.DataFrame(mylist)
    print('dataframe from a list:')
    print(mydf)
    print()

    # create a dataframe from a numpy array
    mydata = np.array([[1,2,3],[4,5,6],[7,8,9]])
    mydf = pd.DataFrame(mydata)
    print('dataframe from a numpy array:')
    print(mydf)
    print()

    # create a dataframe from a dictionary - the value has to be a list,array, series
    mydict = {
      "henry":[10,20,30,40,50,60],
      "david":["a", "b", "c",'d','e','f']
    }
    mydf = pd.DataFrame(mydict)
    print('dataframe from a dictionary:')
    print(mydf)

    print('df index:')
    print(mydf.index)
    print()

    print('dataframe with filter:')
    filter_df = mydf[mydf['henry'] > 30]
    print(filter_df)
    print()

    print('access row 0')
    print(mydf.loc[0])
    print()

    mydf_with_index = mydf.set_index("henry")
    print('index changed to henry')
    print(mydf_with_index)
    print()
    print('locate df with new index at label 10: loc[10]')
    print(mydf_with_index.loc[10])
    print()

    print('locate df with new index at position 1: loc[1]')
    print(mydf_with_index.iloc[1])
    print()


    print('access column henry')
    print(mydf['henry'])
    print()

    mydict = {
      "A": range(20),
      "B": range(20,40)
    }
    mydf = pd.DataFrame(mydict)
    print('dataframe from a dictionary 2:')
    print(mydf)
    print()

    # create a dataframe with list of series
    series1 = pd.Series({'Name': 'Alice', 'Class': 'Physics', 'Score': 85})
    series2 = pd.Series({'Name': 'Jack', 'Class': 'Chemistry', 'Score': 82})
    series3 = pd.Series({'Name': 'Helen', 'Class': 'Biology', 'Score': 90})

    print('series1-----\n', series1)
    print('series2-----\n', series2)
    print('series3-----\n', series3)

    df = pd.DataFrame([series1, series2, series3], index=['school1', 'school2', 'school1'])
    print('dataframe from list of series-----')
    print(df)
    print()

    # create a dataframe from a list of list
    mydata = [['tom',10],['nick',15], ['juli', 14]]
    mydf = pd.DataFrame(mydata)
    print('dataframe from list of list:')
    print(mydf)
    print()

    # create a dataframe with list of dictionaries
    students = [ {'Name': 'Alice',
                  'Class': 'Physics',
                  'Score': 85},
                 {'Name': 'Jack',
                  'Class': 'Chemistry',
                  'Score': 82},
                 {'Name': 'Helen',
                  'Class': 'Biology',
                  'Score': 90}]
    print('dataframe from list of dictionaries-----')
    df = pd.DataFrame(students)
    print(df)
    print()

    df = pd.DataFrame(students, index=['school1', 'school2', 'school1'])
    print('dataframe from list of dictionaries with index-----')
    print(df)
    print()

    # create dataframe from csv (data.csv) file
    mydf = pd.read_csv(DATA_PATH1)
    print('whole dataframe from data.csv')
    # print(mydf.to_string())

    print('beginning 5 rows and last 5 rows dataframe from data.csv')
    print(mydf)
    print()

    # create dataframe from json (data.json) file
    mydf = pd.read_json(DATA_PATH2)
    print('partial dataframe from data.json')
    print(mydf)
    print('mydf.info():')
    print(mydf.info())
    print()

    # process missing data in dataframe from csv (data_missing_data.csv) file
    mydf = pd.read_csv(DATA_PATH3, skipinitialspace=True)
    print('missing dataframe from data_missing_data.csv')
    print(mydf)
    new_df = mydf.dropna()
    print()
    print('drop na:')
    print(new_df.to_string())
    print()

    print('fill empty with 1300:')
    new_df = mydf.fillna(1300)
    print(new_df.to_string())
    print()
    print('mean() value of column Calories:')
    print(mydf["Calories"].mean())
    print()

    print('plotting:')
    mydf = pd.read_csv(DATA_PATH1)
    mydf.plot()
    plt.show()
    print()

    mydf.plot(kind='scatter', x='Duration', y='Calories')
    plt.show()

    mydf['Duration'].plot(kind='hist')
    plt.show()

    print('head():')
    print(mydf.head())
    print()

    print('column names')
    print(mydf.columns)
    print(df.columns)
    print()

    print('df:')
    print(df)
    print('school1-----')
    d = df.loc['school1']
    print('d.loc[\'school1\']')
    print(d)
    print(type(d))
    print()

    print('school1 with names-----')
    print('df.loc[\'school1\',\'Name\']')
    d = df.loc['school1', 'Name']
    print(d)
    print(type(d))
    print()

    print('school1 with names, score-----')
    print('df.loc[\'school1\', [\'Name\', \'Score\']]')
    print(df.loc['school1', ['Name', 'Score']])
    print()

    print('df.loc[\'school1\'][\'Name\'] -- chaining---')
    d = df.loc['school1']['Name']
    print(d)
    print(type(d))
    print()

    print('df[\'Name\']-----')
    d = df['Name']
    print(d)
    print('type=', type(d))
    print()

    d = df['Class']
    print('df[\'Class\']')
    print(d)
    print()

    d = df.loc[:,['Name','Score']]
    print('df.loc[:,[\'Name\',\'Score\']')
    print(d)


def main():
  """
  """
  print('CWD:', os.getcwd())
  print('__file__:', __file__)

  me = PandaTester()
  me.create_dataframe()

if __name__ == "__main__":
  main()    