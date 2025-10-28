# dataclass
from dataclasses import dataclass

@dataclass
class Abc:
  name: str
  age: int
  city: str

person = Abc(name='Henry', age=35, city='Chicago')

print(person)
