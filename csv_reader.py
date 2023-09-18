#!/use/bin/python3
"""
csv reader 
@csvreader
"""
import csv_reader_module

def main() -> int:

  me = csv_reader_module.CsvReader('mpg.csv')
  me.read_csv()

if __name__ == '__main__':
  main()