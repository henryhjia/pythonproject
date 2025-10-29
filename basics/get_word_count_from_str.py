import io
import string_process_module

stream = io.StringIO("Hey! How are you?\nI am good, how about you?\nI am good too.")
print(type(stream))
me = string_process_module.StringProcessModule()
word = 'good'
result = me.count_occurrence(word, stream)
print('stream=', stream.getvalue())
print(f'Occurrence of \'{word}\' = {result}')
stream.close()