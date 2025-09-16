"""
iteration test for various data type
"""

# list
print('list:')
a = [1,2,3,4,5,6]
for i in a:
  print(i, end=' ')
print()

# set
b = {1,2,3,4,5,6}
print('set:')
for i in b:
  print(i, end=' ')
print()

#tuple
c = (1,2,3,4,5,6)
print('tuple:')
for i in c:
  print(i, end=' ')
print()

#dictionary
d = {'name': 'henry',
     'age': '40',
     'job title': 'software engineer'}

print('dictionary key:')
for i in d:
  print(i, end=' ')
print()

for i in d.keys():
  print(i, end=' ')
print()

# print both key and value
print('dictionary with key and value:')
for i in d.keys():
  print(i, d[i])
print()

print('dictionary values:')
for i in d.values():
  print(i, end=' ')
print()

# dictionary key and values
print('dictionary key and values:')
for key, value in d.items():
  print(key, value)
print()

# iterate with index (enumeration)
print('dictionary with index:')
for i, (key, value) in enumerate(d.items()):
  print(i, key, value)
print()

# iterate in a sorted order by key
print('dictionary with sorted key:')
for i in sorted(d.keys()):
  print(i, d[i], type(d[i]))
print()

# iterate in a sorted order by value - values have to be the same data type
for key, value in sorted(d.items(), key=lambda item: item[1]):
  print(key, value)
print()