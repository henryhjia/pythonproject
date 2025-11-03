#!/use/bin/python3
import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __sub__(self, no):
        new_x = self.x - no.x
        new_y = self.y - no.y
        new_z = self.z - no.z
        return Points(new_x, new_y, new_z)
    
    def dot(self, no):
      result = self.x * no.x + self.y* no.y + self.z *no.z      
      return result
    
    def cross(self, no):
      result = [
          self.y * no.z - self.z * no.y,
          self.z * no.x - self.x * no.z,
          self.x * no.y - self.y * no.x
      ]
      print('cross result=', result)
      return Points(result[0], result[1], result[2])
    
    def absolute(self):
      return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
    