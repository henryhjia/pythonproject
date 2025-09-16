import pdfplumber
import pandas as pd

mydict = {}
mylist = []

with pdfplumber.open('./data/python_data_pdf.pdf') as pdf:
  for i, page in enumerate(pdf.pages):
    text = page.extract_text()
    text_list = text.split('\n')
    print(i, text_list)

  for item in text_list:
    # print(item)
    item_list = item.split(' ')
    print(item_list)
    mydict[item_list[0]] = item_list[1:]
    mylist.append(item_list)


  for key, value in mydict.items():
    print(key, value)

  for item in mylist:
    print(item)

  df = pd.DataFrame(mylist[1:], columns=mylist[0])
  print(df)

  print(df.columns)

  print(df['TPSA'].dtype)
  print(type(df['TPSA'].iloc[0]))

  print('average tpsa:')
  average = pd.to_numeric(df['TPSA'], errors='coerce').mean()
  print(f'{average:.2f}')