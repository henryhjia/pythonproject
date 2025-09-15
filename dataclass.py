# dataclass
"""
1. mutable unless set frozen=True @dataclass(frozen=True)
2. does not have behavior
3. more concise and less boilerplate code
"""
from dataclasses import dataclass, field

@dataclass
class Exercise:
    name: str = field(default='henry')
    age: int = field(default=40)
    height: float = field(default=180.0)
    weight: float = field(default=170.0)

ex1 = Exercise('henry jia', 50, 170, 150)
ex2 = Exercise()

print(f'result={ex1}')
print(f'result={ex2}')

ex1.name = 'Jean'
print(f'result={ex1}')