#!/use/bin/python3
"""
@brief calculate two concecutive numbers and check if it is the same as a target,
if so, return the two numbers

@twosum
@target
"""

class TwoSumTester:
  """
  @brief
  """
  def __init__(self) -> None:
    """
    @brief constructor
    """
    pass

  def find_two_sum_equal_to_target(self, in_list: list, target: int) -> list:
    """
    """
    print(in_list, target, len(in_list))

    for i in range(len(in_list)-1):
       if (in_list[i] + in_list[i+1]) == target:
          return [in_list[i], in_list[i+1]]

    return [-1,-1]


if __name__ == '__main__':
    print('module only, not main')
