#!/use/bin/python3
"""
date time tester 
@datetime
"""
import datetime as dt
import time as tm


class DatetimeModule:
  """
  """

  def __init__(self):
    """
    """

    pass

  @staticmethod
  def test_datetime():
      
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

if __name__ == '__main__':
    print('module only, not main')