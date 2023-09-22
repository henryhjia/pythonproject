#!/use/bin/python3
"""
Sort dictionary
@sortdictionary

"""
import dictionary_sort_module

def main() -> int:

  me = dictionary_sort_module.SortDictionaryTester()

  # Sort dictionary by value
  me.sort_dictionary_by_value()

  # Sort dictionary by key
  me.sort_dictionary_by_key()


if __name__ == '__main__':
  main()