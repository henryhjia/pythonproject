#!/use/bin/python3
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print('++++++++++++ 1-D array:')
print(arr)
print(np.__version__)
print(type(arr))

arr = np.array([[1,2,3],[4,5,6]])
print('++++++++++++ 2-D array:')
print(arr)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print('++++++++++++ 3-D array:')
print(arr)
print()

print('++++++++++++ Check dimentions of array:')
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

arr = np.array([1, 2, 3, 4], ndmin=5)
print('++++++++++++ 5-D array:')
print(arr)
print('number of dimensions:', arr.ndim)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print('++++++++++++ Accessing 3-D element  [0,1,2]:')
print(arr)
print(arr[0, 1, 2])


arr = np.array([1, 2, 3, 4, 5, 6, 7])
print('++++++++++++ 1-DSlicing [:4]:')
print(arr)
print(arr[:4])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('++++++++++++ 2-D Slicing [1,[1:4]]:')
print(arr)
print(arr[1, 1:4])

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print('++++++++++++ Copy array')
print(arr)
print(x)

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print('++++++++++++ View array')
print(arr)
print(x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print('++++++++++++ Shape of an array')
print(arr)
print(arr.shape)