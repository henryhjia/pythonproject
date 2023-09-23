#!/usr/bin/python3
import io
import string_count_module

if __name__ == "__main__":
    stream = io.StringIO("Hey! How are you?\nI am good, how about you?\nI am good too.")

    me = string_count_module.StringTester()
    word = 'good'
    result = me.count_occurrence(word, stream)
    print('stream=', stream.getvalue())
    print(f'Occurrence of \'{word}\' = {result}')
    stream.close()