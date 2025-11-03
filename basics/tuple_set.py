"""
test tuple and set
"""

mytuple = (12,13,14,"jia")
print(type(mytuple), mytuple, mytuple[0])

myset = {12,13,14,"jia"}
print(type(myset), myset)
for i, elem in enumerate(myset):
    print(i, elem)