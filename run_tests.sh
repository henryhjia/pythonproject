#!/bin/bash
# ./run_tests.sh > temp.txt 2>&1

python3 -m unittest calculate_two_sum_from_list_unittest.UnitTest -v
python3 -m unittest check_string_palindrome_unittest.UnitTest -v
python3 -m unittest count_occur_from_dict_unittest.UnitTest -v
python3 -m unittest get_list_moving_total_unittest.UnitTest -v
python3 -m unittest get_word_count_from_str_unittest.UnitTest -v
python3 -m unittest reverse_list_unittest.UnitTest -v
python3 -m unittest reverse_string_unittest.UnitTest -v
python3 -m unittest slice_string_unittest.UnitTest -v
python3 -m unittest sort_dictionary_unittest.UnitTest -v
python3 -m unittest sort_list_of_dict_unittest.UnitTest -v
python3 -m unittest sort_list_of_list_unittest.UnitTest -v
python3 -m unittest sort_list_unittest.UnitTest -v
python3 -m unittest sort_string_unittest.UnitTest -v