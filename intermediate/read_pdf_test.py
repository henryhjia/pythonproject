import pdfplumber
import pandas as pd
from pathlib import Path

# Get the absolute path to the current script
CURRENT_DIR = Path(__file__).resolve().parent

# Go up one level to project root
PROJECT_ROOT = CURRENT_DIR.parent

# Point to the data directory
DATA_DIR = PROJECT_ROOT / "data"

# File path
file_path = DATA_DIR / "python_data_pdf.pdf"

mydict = {}
mylist = []

with pdfplumber.open(file_path) as pdf:
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