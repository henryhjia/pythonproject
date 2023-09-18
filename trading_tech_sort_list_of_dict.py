#!/usr/bin/python3
# sort list of dictionaries, the list data is populated using json.loads() or ast.literal_eval() 
# from string representation of a list of dictionary
#
# two print formats:
# 1. format: print(format(order, '3d'))
# 2. f notation: print(f'{order: 3d}')
#
# July 2023
import ast
import json

def sort_by_price_ascending_by_price_ast_literal_eval(json_string):
    # convert to a list of dictionaries from a string json_string
    # method 1:
    list_of_dictionaries = ast.literal_eval(json_string)

    # sort the list of dictionaires by the value 'price' in the dictionary
    sorted_list = sorted(list_of_dictionaries, key=lambda x:x['price'])

    return sorted_list

def sort_by_price_ascending_by_price_json_loads(json_string):
    # convert to a list of dictionaries from a string json_string
    # method 2:
    list_of_dictionaries = json.loads(json_string)

    # sort the list of dictionaires by the value 'price' in the dictionary
    sorted_list = sorted(list_of_dictionaries, key=lambda x:x['price'])

    return sorted_list

def sort_by_price_ascending_by_name_ast_literal_eval(json_string):
    # convert to a list of dictionaries from a string json_string
    # method 1:
    list_of_dictionaries = ast.literal_eval(json_string)

    # sort the list of dictionaires by the value 'price' in the dictionary
    sorted_list = sorted(list_of_dictionaries, key=lambda x:x['name'])

    return sorted_list

def sort_by_price_ascending_by_name_json_loads(json_string):
    # convert to a list of dictionaries from a string json_string
    # method 2:
    list_of_dictionaries = json.loads(json_string)

    # sort the list of dictionaires by the value 'price' in the dictionary
    sorted_list = sorted(list_of_dictionaries, key=lambda x:x['name'])

    return sorted_list

def sort_by_price_descending_by_name(json_string):
    # convert to a list of dictionaries from a string json_string
    # method 2:
    list_of_dictionaries = json.loads(json_string)

    # sort the list of dictionaires by the value 'price' in the dictionary
    sorted_list = sorted(list_of_dictionaries, key=lambda x:x['name'], reverse=True)

    return sorted_list

def sort_by_price_descending_by_price(json_string):
    # convert to a list of dictionaries from a string json_string
    # method 2:
    list_of_dictionaries = json.loads(json_string)

    # sort the list of dictionaires by the value 'price' in the dictionary
    sorted_list = sorted(list_of_dictionaries, key=lambda x:x['price'], reverse=True)

    return sorted_list

def sort_by_price_ascending_by_key(json_string):
    # convert to a dictionaries from a string json_string, then sort dictionary by key

    mydic = json.loads(json_string)
    mysorted_list = sorted(mydic.items())
    sorted_dict = dict(mysorted_list)

    return sorted_dict

def sort_by_price_ascending_by_value(json_string):
    # convert to a dictionaries from a string json_string, then sort dictionary by value

    mydic = json.loads(json_string)
    mysorted_list = sorted(mydic.items(), key=lambda x:x[1])
    sorted_dict = dict(mysorted_list)

    return sorted_dict

def sort_by_price_descending_by_key(json_string):
    # convert to a dictionaries from a string json_string, then sort dictionary by value

    mydic = json.loads(json_string)
    mysorted_list = sorted(mydic.items(), reverse=True)
    sorted_dict = dict(mysorted_list)

    return sorted_dict

def sort_by_price_descending_by_value(json_string):
    # convert to a dictionaries from a string json_string, then sort dictionary by value

    mydic = json.loads(json_string)
    mysorted_list = sorted(mydic.items(), key=lambda x:x[1], reverse=True)
    sorted_dict = dict(mysorted_list)

    return sorted_dict

order = 1
# for string data ''[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]')'
str1 = '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'
print(format(order, '3d'), sort_by_price_ascending_by_price_ast_literal_eval(str1))
order += 1

print(format(order, '3d'), sort_by_price_ascending_by_price_json_loads(str1))
order += 1

print(f'{order: 3d}', sort_by_price_ascending_by_name_ast_literal_eval(str1))
order += 1

print(f'{order: 3d}', sort_by_price_ascending_by_name_json_loads(str1))
order += 1

print(f'{order: 3d}', sort_by_price_descending_by_name(str1))
order += 1

print(f'{order: 3d}', sort_by_price_descending_by_price(str1))
order += 1

# for string data '{"eggs":1, "coffee":9.99, "rice":4.04}'
str2 = '{"eggs":1, "coffee":9.99, "rice":4.04}'
print(f'{order: 3d}', sort_by_price_ascending_by_key(str2))
order += 1

print(f'{order: 3d}', sort_by_price_ascending_by_value(str2))
order += 1

print(f'{order: 3d}', sort_by_price_descending_by_key(str2))
order += 1

print(f'{order: 3d}', sort_by_price_descending_by_value(str2))
