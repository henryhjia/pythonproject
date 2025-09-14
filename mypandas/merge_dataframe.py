"""
@replace
use presidents.csv
"""
import pandas as pd

from modules import common_module


class PandaTester:
  def __init__(self):
    self._staff = pd.DataFrame([
                         {'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}
                         ])

    self._student = pd.DataFrame([
                         {'Name': 'James', 'School': 'Business'},
                         {'Name': 'Mike', 'School': 'Law'},
                         {'Name': 'Sally', 'School': 'Engineering'}
                         ])

  def merge_dataframe(self):
    common_module.print_function(self.merge_dataframe)
    print('+++++++++++ staff:')
    self._staff = self._staff.set_index('Name')
    print(self._staff)
    print()

    print('+++++++++++ student:')    
    self._student = self._student.set_index('Name')
    print(self._student)
    print()

    merged = pd.merge(self._staff, self._student, how='outer', left_index=True, right_index=True)
    print('+++++++++++ outer join:')  
    print(merged)
    print()

    merged = pd.merge(self._staff, self._student, how='inner', left_index=True, right_index=True)
    print('+++++++++++ inner join:')      
    print(merged)
    print()

    self._staff = self._staff.reset_index()
    self._student = self._student.reset_index()

    # Now lets merge using the on parameter
    merged = pd.merge(self._staff, self._student, how='right', on='Name')
    print('+++++++++++ right join:')      
    print(merged)


def main() -> None:
  me = PandaTester()
  me.merge_dataframe()

if __name__ == '__main__':
  main()  