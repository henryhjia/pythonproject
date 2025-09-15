"""
default dictionay practice
"""
from collections import defaultdict

words = ['apple','banana','apple','orange','banana', 'apple', 'pear']
word_count = defaultdict(int)

for word in words:
    word_count[word] += 1

for key, value in word_count.items():
    print(key, value)

for i, value in enumerate(word_count.items()):
    print(i, value)

print(word_count['grape'])
