import copy

# check is set and list are in same memory space
a=(1,2,3,4,5)
b=(1,2,3,4,5)
c=[1,2,3,4,5]
d=[1,2,3,4,5]

print('a is b=', a is b)
print('c is d=', c is d)

a=[1,1,2,2,2,3,4,4,4,4,5]
b=set(a)
print('list a=', a)

# find length of uniq element
print('length of uniq elem=',len(b))

# find histogram of list a
my_dict = {}

for elem in a:
  print('elem=', elem, end=" ")
  if elem in my_dict:
    my_dict[elem] += 1
  else:
    my_dict[elem] = 1

print()
print('histogram=', my_dict)
print()

# copy vs not copy
# b=list(a)
# b=a.copy()

# not copy, both point to the same memory space
a=[1,2,3,4]
b=a
a[0]=10

print('a=',a)
print('b=',b)
print('list a is list b=', a is b)
print()

# copy, a and b are in different memory space
c=list(a)
a[0]=20
print('list a=', a)
print('list c=', c)
print('list a is list c=', a is c)
print()

# for set, a and b is the same, for list c and d is different
a=(1,2,3,4)
b=(1,2,3,4)
c=[1,2,3,4]
d=[1,2,3,4]

print(a is b)
print(c is d)

# for tuple, you can not change it's value.  however, if the value is a  mutable data, you can change it.
aa=(1,2,[1,2],3)
print('original tuple=', aa)
aa[2][0]=100
print('changed list inside a tuple=', aa)
print()


# copy list of list case
print('copy list: shadow copy.  Changes in the nested part will affect the other')
a=[1,2,[1,2,3],3]
b=a.copy()
print('a=',a)
a[0]=100
a[2][0]=99
print('a=',a)
print('b=',b)
print()

# deep copy
print('deep copy: any change to one list does not affect the other')
a=[1,2,[1,2,3],3]
b=copy.deepcopy(a)
a[0]=12
a[2][0]=300
print('a=',a)
print('b=',b)


