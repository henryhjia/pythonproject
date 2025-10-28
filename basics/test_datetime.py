#!/use/bin/python3
"""
date time tester 
@datetime

Usage: in pythonproject/ python -m basics.test_datetime

"""
from modules import datetime_module

def main() -> None:

  me = datetime_module.DatetimeModule()

  me.test_datetime()

if __name__ == '__main__':
  main()