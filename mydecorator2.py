# decorator with arguments

def smart_divide(func):
  def inner(a,b):
    if b == 0:
      print('oops, cannot divide')
      return
    
    return func(a,b)
  return inner

@smart_divide
def divide(a,b):
  print(a/b)


divide(2,5)

divide(2,0)
  