#!/use/bin/python3
"""
Finance tester
"""
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib import dates

class FinanceTester:
  """
  """
  def fix_cols(self, df):
    columns = df.columns
    outer = [col[0] for col in columns]
    df.columns = outer
    return df
  
  def tweak_data(self):
    raw = yf.download('SPY AAPL', start='2010-01-01', end='2019-12-31')

    return ( raw 
            .iloc[:,::2] 
            .pipe(self.fix_cols))

  def finance_test(self):
    """
    """
    raw = yf.download('SPY AAPL', start='2010-01-01', end='2019-12-31')

    print(raw)

  def my_plot(self):

    raw = yf.download('SPY AAPL', start='2010-01-01', end='2019-12-31')

    return ( raw 
            .iloc[:,-2:2] 
            .pipe(self.fix_cols)
            # .plot()
            )
    
def main() -> int:

  me = FinanceTester()

  # me.finance_test()
  print(me.tweak_data())
  # me.my_plot()


if __name__ == '__main__':
  main()