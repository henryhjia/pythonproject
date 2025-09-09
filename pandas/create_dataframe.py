#!/use/bin/python3
import pandas as pd

from modules import common_module


class PandaTester:
  def __init__(self):
    pass

  def create_dataframe(self):
    common_module.print_function(self.create_dataframe)

    # create a dataframe from a dictionary - the value has to be list,array, series
    mydict = {
      "henry":[10,20,30],
      "david":["a", "b", "c"]
    }
    mydf = pd.DataFrame(mydict)
    print('dataframe from a dictionary:')
    print(mydf)

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
    mydf = pd.read_csv('../../data/data.csv')
    print('whole dataframe from data.csv')
    print(mydf.to_string())

    print('beginning 5 rows and last 5 rows dataframe from data.csv')
    print(mydf)
    print()

    # create dataframe from json (data.json) file
    mydf = pd.read_json('../../data/data.json')
    print('partial dataframe from data.json')
    print(mydf)
    print('mydf.info():')
    print(mydf.info())
    print()

    print('column names')
    print(df.columns)
    print()
    
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
  me = PandaTester()
  me.create_dataframe()

if __name__ == "__main__":
  main()    