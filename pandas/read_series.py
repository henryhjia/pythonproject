#!/use/bin/python3
import pandas as pd
import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import common_module

class PandaTester:
  def __init__(self):
    pass

  def create_series(self):
    common_module.print_function(self.create_series)

    # create Series from a list
    name = ['Alice', 'Jack', 'Molly']
    print('+++++++++ create Series using list of strings')
    print(pd.Series(name))
    numbers = [1,2,3]
    print('+++++++++ create Series using list of integers')
    print(pd.Series(numbers))

    name = ['Alice', 'Jack', None]
    print('+++++++++ create Series using list of strings with None element')
    print(pd.Series(name))

    numbers = [1,2,None]
    print('+++++++++ create Series using list of integers with None element')
    print(pd.Series(numbers))    

    print(np.isnan(np.nan))

    # create a Series from a dictionary
    students_cores = {'Alice': 'Physics',
                      'Jack': 'Chemistry',
                      'Molly': 'English'}
    s = pd.Series(students_cores)
    print('+++++++++ create Series using list of dictionary')
    print(s)
    print('s index=', s.index)

    # create a Series using index
    print('+++++++++ create Series using list and index')
    s = pd.Series(['Physics', 'Chemistry', 'english'], index=['Alice','Jack', 'Molly'])
    print(s)

    # query Series using iloc and loc
    print('+++++++++ access element using loc and iloc')
    print('s.loc jack=', s.loc['Jack'])
    print('s.iloc[2]=', s.iloc[2])

    # use class and class code
    class_code = { 99: 'Physics',
                  100: 'Chemistry',
                  101: 'English',
                  102: 'History'}
    s= pd.Series(class_code)
    print('+++++++++ use classcode')
    print(s)
    print(s.iloc[0])

    # do math calculation
    print('+++++++++ do math')
    grade = pd.Series([90,80,70,60])
    total = np.sum(grade)
    print('total=', total)
    print('ave=', total/len(grade))

    numbers = pd.Series(np.random.randint(0,1000,10000))
    print('number.head=')
    print(numbers.head())
    print('len=', len(numbers))
    numbers += 2
    print('numbers+=2 using broadcast:')
    print(numbers.head())

  def create_dataframe(self):
    common_module.print_function(self.create_dataframe)

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
    print('\n')

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
    print('dateframe from list of dictionaries-----')
    df = pd.DataFrame(students)
    print(df)
    print('\n')

    df = pd.DataFrame(students, index=['school1', 'school2', 'school1'])
    print('dateframe from list of dictionaries with index-----')
    print(df)
    print('\n')

    print('school1-----')
    d = df.loc['school1']
    print('d.loc[\'school1\']')
    print(d)
    print(type(d))
    print('\n')

    print('school1 with names-----')
    print('df.loc[\'school1\',\'Name\']')
    d = df.loc['school1', 'Name']
    print(d)
    print(type(d))
    print('\n')

    print('school1 with names, score-----')
    print('df.loc[\'school1\', [\'Name\', \'Score\']]')
    print(df.loc['school1', ['Name', 'Score']])
    print('\n')

    print('df.loc[\'school1\'][\'Name\'] -- chaining---')
    d = df.loc['school1']['Name']
    print(d)
    print(type(d))
    print('\n')

    print('df[\'Name\']-----')
    d = df['Name']
    print(d)
    print('type=', type(d))
    print('\n')

    d = df['Class']
    print('df[\'Class\']')
    print(d)
    print('\n')

    d = df.loc[:,['Name','Score']]
    print('df.loc[:,[\'Name\',\'Score\']')
    print(d)


def main():
  """
  """
  me = PandaTester()
  me.create_series()
  me.create_dataframe()

if __name__ == "__main__":
  main()    