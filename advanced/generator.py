"""
generator practice
"""

def infinite_sequence():
    num = 0
    while num < 30:
        yield num
        num += 1

for i in infinite_sequence():
    print(i, end=' ')

print()
print()

def my_generator(n):
    value = 0
    while value < n:
        yield value
        value += 1

for value in my_generator(30):
    print(value, end=' ')
print()