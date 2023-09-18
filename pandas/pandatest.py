#!/use/bin/python3
import pandas as pd
import sys
import matplotlib
import matplotlib.pyplot as plt

def main():
  """
  """
  print('pandas test')

  mydataset = {'cars': ["BMW", "Volvo", "Ford"],'passings': [3,7,2] }

  myvar = pd.DataFrame(mydataset)

  print('+++++++++++++++ DataFrame:')
  print(myvar)
  print('+++++++++++++++ pandas version:', pd.__version__)

  a = [1,7,2]
  myvar = pd.Series(a)
  print('+++++++++++++++ Series:')
  print(myvar)

  calories = {"day1":420, "day2": 380, "day3": 390}
  myvar = pd.Series(calories)
  print('+++++++++++++++ key/value objects as Series:')
  print(myvar)

  calories = {"day1":420, "day2": 380, "day3": 390}
  myvar = pd.Series(calories, index = ["day1", "day2"])
  print('+++++++++++++++ Some key/value objects as Series using only data from indexes:')
  print(myvar)

  data = {"calories": [420,380,390], "duration": [50, 40, 45]}
  df = pd.DataFrame(data)
  print('+++++++++++++++ DataFrame:')  
  print(df)

  df = pd.DataFrame(data, index = ["day1", "day2", "day3"])  
  print('+++++++++++++++ DataFrame locate row:')   
  print(df)  
  print(df.loc["day2"])

  df = pd.read_csv('data.csv')
  print('+++++++++++++++ csv file:')
  print(df)
  print(pd.options.display.max_rows) 
  
  df = pd.read_json('data.json')
  print('+++++++++++++++ Json File:')
  print(df.to_string())

  print('+++++++++++++++ Json head:')
  print(df.head(10))

  print('+++++++++++++++ Json tail:')
  print(df.tail())

  print('+++++++++++++++ Json info:')
  print(df.info())

  data = {
    "Duration":{
      "0":60,
      "1":60,
      "2":60,
      "3":45,
      "4":45,
      "5":60
    },
    "Pulse":{
      "0":110,
      "1":117,
      "2":103,
      "3":109,
      "4":117,
      "5":102
    },
    "Maxpulse":{
      "0":130,
      "1":145,
      "2":135,
      "3":175,
      "4":148,
      "5":127
    },
    "Calories":{
      "0":409,
      "1":479,
      "2":340,
      "3":282,
      "4":406,
      "5":300
    }
  }

  df = pd.DataFrame(data)
  print('+++++++++++++++ Dictionary as Json:')
  print(df) 

  df = pd.read_csv('baddata.csv')
  print('+++++++++++++++ Bad data:')  
  print(df.to_string()) 

  print('+++++++++++++++ Remove bad data:')
  df_new = df.dropna()  
  print(df_new.to_string())

  # df['Date'] = pd.to_datetime(df['Date'])
  # print(df.to_string())

  # df.loc[7, 'Duration'] = 45
  print('+++++++++++++++ Remove duplicates:')  
  df.drop_duplicates(inplace = True)
  print(df.to_string())
  # df.dropna(subset=['Date'], inplace = True)
  # print(df.to_string())
  # x = df["Calories"].mean()
  # print('men=', x)

  df = pd.read_csv('data_corr.csv')
  print('+++++++++++++++ Corrolation:')    
  print(df.corr())

  df.plot()
  plt.show()

  df = pd.read_csv('data_scatter.csv')
  df.plot(kind = 'scatter', x= 'Duration', y='Calories')
  plt.show()

  df["Duration"].plot(kind = 'hist')
  plt.show()
  

if __name__ == "__main__":
  main()    