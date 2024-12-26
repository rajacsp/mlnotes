---
title: 640-Solve-The-Equation
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/solve-the-equation


```
import pyutil as pyu
pyu.get_local_pyinfo()
```


```
print(pyu.ps2("python-dotenv"))
```


```
from typing import List
```


```
class Solution:
  def solveEquation(self, equation: str) -> str:
    def calculate(s: str) -> tuple:
      coefficient = 0
      constant = 0
      num = 0
      sign = 1

      for i, c in enumerate(s):
        if c.isdigit():
          num = num * 10 + ord(c) - ord('0')
        elif c in '+-':
          constant += sign * num
          sign = 1 if c == '+' else -1
          num = 0
        else:
          if i > 0 and num == 0 and s[i - 1] == '0':
            continue
          coefficient += sign if num == 0 else sign * num
          num = 0

      return coefficient, constant + sign * num

    lhsEquation, rhsEquation = equation.split('=')
    lhsCoefficient, lhsConstant = calculate(lhsEquation)
    rhsCoefficient, rhsConstant = calculate(rhsEquation)
    coefficient = lhsCoefficient - rhsCoefficient
    constant = rhsConstant - lhsConstant

    if coefficient == 0 and constant == 0:
      return "Infinite solutions"
    if coefficient == 0 and constant != 0:
      return "No solution"
    return "x=" + str(constant // coefficient)
```


```
new Solution().solveEquation()
```


---
**Score: 5**