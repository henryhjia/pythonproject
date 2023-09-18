#!/use/bin/python3
"""
Sort list
@sortlist

Two methods:
l2 = sorted(l1) - create a new list that is sorted
l1.sort() - in place sort

"""

class SortListTester:
  """
  """
  def sort_data(self) -> None:
    """
    1. sorted()
    """

    l1 = [10, 9,4,6,20,1]

    l2 = sorted(l1)
    print('original list=', l1)
    print('sorted list  =', l2)

    l1 = ['henry', 'claire', 'jean', 'maggie']
    l2 = sorted(l1)
    print('original list=', l1)
    print('sorted list  =', l2)

    """
    2. sort()
    """
    l1 = [10, 9,4,6,20,1]
    print('original list=', l1)
    l1.sort()
    print('sorted list  =', l1)

    l1 = ['henry', 'claire', 'jean', 'maggie']
    print('original list=', l1)
    l1.sort()
    print('sorted list  =', l1)

def main() -> int:

  me = SortListTester()

  # sort data from variables
  me.sort_data()


if __name__ == '__main__':
  main()