#!/use/bin/python3
"""
read json file 
@readjson
"""
import sys

import json_reader_module


def main(args: list=[]) -> None:
  print(f'lengh of argument : {len(args)}')
  if len(args) < 2:
    print('usage:', args[0], '../data/dad_mom.json')
    exit(1)

  me = json_reader_module.JsonReader(args[1])
  # me.read_json()
  # me.print_data()
  me.read_json_data()
  me.print_json_data()


if __name__ == '__main__':
  main(sys.argv)