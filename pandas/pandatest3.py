#!/use/bin/python3
import pandas as pd
import sys
import matplotlib
import matplotlib.pyplot as plt

class PandaTester:
  def __init__(self):
    pass

  def create_series_dataframe(self):
    record1 = pd.Series({'Name': 'Alice', 'Class': 'Physics', 'Score': 85})
    record2 = pd.Series({'Name': 'Jack', 'Class': 'Chemistry', 'Score': 82})
    record3 = pd.Series({'Name': 'Helen', 'Class': 'Biology', 'Score': 90})

    print(record1)
    print(record2)
    print(record3)

    df = pd.DataFrame([record1, record2, record3], index=['school1', 'school2', 'school1'])

    print(df)
    # print(df.loc['school1'])
    print(df.loc['school1', ['Name', 'Score']])
    print(df.loc['school1']['Name'])
    print(df.loc[:,['Name','Score']])
    # print(df['Name'])

def main():
  """
  """
  me = PandaTester()
  me.create_series_dataframe()

if __name__ == "__main__":
  main()    