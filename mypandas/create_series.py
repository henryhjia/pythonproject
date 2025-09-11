import numpy as np
import pandas as pd

from modules import common_module


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
    print('+++++++++ create Series using a dictionary')
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

def main():
  """
  """
  me = PandaTester()
  me.create_series()

if __name__ == "__main__":
  main()    