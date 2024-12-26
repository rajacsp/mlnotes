---
title: 150-Evaluate-Reverse-Polish-Notation
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/evaluate-reverse-polish-notation


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
  def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b),
    }

    for token in tokens:
      if token in operators:
        b = stack.pop()
        a = stack.pop()
        stack.append(operators[token](a, b))
      else:
        stack.append(int(token))

    return stack[0]
```


```
new Solution().evalRPN()
```


---
**Score: 5**