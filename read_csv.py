#!/use/bin/python3
"""
read csv file 
@readcsv
"""
from modules import csv_reader_module

def main() -> None:

  me = csv_reader_module.CsvReader('data/mpg.csv')
  me.read_csv()

if __name__ == '__main__':
  main()