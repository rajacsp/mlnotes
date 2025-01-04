---
title: 439-Ternary-Expression-Parser
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/ternary-expression-parser


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
  def parseTernary(self, expression: str) -> str:
    c = expression[self.i]

    if self.i + 1 == len(expression) or expression[self.i + 1] == ':':
      self.i += 2
      return str(c)

    self.i += 2
    first = self.parseTernary(expression)
    second = self.parseTernary(expression)

    return first if c == 'T' else second

  i = 0
```


```
new Solution().parseTernary()
```


---
**Score: 5**