#!/use/bin/python3
# @numpy
# @elementwiseproduct
# @matrixproduct
import numpy as np
import math
from PIL import Image


class NpTester:
  def __init__(self):
    pass

  def test1(self):
    a = np.array([1,2,3])

    print(a)
    print(a.ndim)
    print(a**2)
    print(a>2)
    print(a%2 == 0)

    b = np.array([[1,2,3],[4,5,6]])
    print('b=', b)
    print('b ndim=', b.ndim)

    print('b shape=', b.shape)
    print(b.dtype)

    a = np.array([[1,1],[0,1]])
    b = np.array([[2,0],[3,4]])
    print('a=', a)
    print('b=', b)
    print('a@b=', a@b)

    print('sum a=', a.sum())
    print('max a =', a.max())
    print('min a =', a.min())
    print('mean a=', a.mean())

    b = np.arange(1,16,1).reshape(3,5)
    print(b)

  def test2(self):
    """
    """
    mask = np.full((200,200),255)
    print(mask)

    print(np.__version__)

def main():
  me = NpTester()
  me.test1()
  me.test2()

if __name__ == '__main__':
  main()