#!/use/bin/python3
"""
date time tester 
@datetime
"""
import datetime as dt
import time as tm


class Datetime_Tester:
  """
  """

  def __init__(self):
    """
    """

    pass

  def test_datetime(self):
      
    mydt = dt.datetime(2023,9,9,14,9,56,938518)
    print('my date from string=', mydt)

    print('time now in seconds=', tm.time())

    dtnow = dt.datetime.fromtimestamp(tm.time())
    print('time now=', dtnow)

    print(dtnow.year)
    print(dtnow.month)
    print(dtnow.day, dtnow.hour, dtnow.minute, dtnow.second)

    delta = dt.timedelta(days=100)
    print('delta=', delta)

    print('today=', dt.date.today())
    print('100 day ago=', dt.date.today() - delta)



def main() -> int:

  me = Datetime_Tester()

  me.test_datetime()


if __name__ == '__main__':
  main()