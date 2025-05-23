---
title: 772-Basic-Calculator-Iii
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/basic-calculator-iii


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
  def calculate(self, s: str) -> int:
    nums = []
    ops = []

    def calc():
      b = nums.pop()
      a = nums.pop()
      op = ops.pop()
      if op == '+':
        nums.append(a + b)
      elif op == '-':
        nums.append(a - b)
      elif op == '*':
        nums.append(a * b)
      else:  # Op == '/'
        nums.append(int(a / b))

    # Returns true if prevOp is a operator and
    # Priority(prevOp) >= priority(currOp)
    def precedes(prevOp: chr, currOp: chr) -> bool:
      if prevOp == '(':
        return False
      return prevOp in '*/' or currOp in '+-'

    i = 0
    hasPrevNum = False

    while i < len(s):
      c = s[i]
      if c.isdigit():
        num = ord(c) - ord('0')
        while i + 1 < len(s) and s[i + 1].isdigit():
          num = num * 10 + (ord(s[i + 1]) - ord('0'))
          i += 1
        nums.append(num)
        hasPrevNum = True
      elif c == '(':
        ops.append('(')
        hasPrevNum = False
      elif c == ')':
        while ops[-1] != '(':
          calc()
        ops.pop()  # Pop '('
      elif c in '+-*/':
        if not hasPrevNum:  # Handle input like "-1-(-1)"
          num.append(0)
        while ops and precedes(ops[-1], c):
          calc()
        ops.append(c)
      i += 1

    while ops:
      calc()

    return nums.pop()
```


```
new Solution().calculate()
```


---
**Score: 5**