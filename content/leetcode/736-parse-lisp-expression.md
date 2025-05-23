---
title: 736-Parse-Lisp-Expression
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/parse-lisp-expression


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
  def evaluate(self, expression: str) -> int:
    def evaluate(e: str, prevScope: dict) -> int:
      if e[0].isdigit() or e[0] == '-':
        return int(e)
      if e in prevScope:
        return prevScope[e]

      scope = prevScope.copy()
      nextExpression = e[e.index(' ') + 1:-1]
      tokens = parse(nextExpression)

      if e[1] == 'a':
        return evaluate(tokens[0], scope) + evaluate(tokens[1], scope)
      if e[1] == 'm':
        return evaluate(tokens[0], scope) * evaluate(tokens[1], scope)

      for i in range(0, len(tokens) - 2, 2):
        scope[tokens[i]] = evaluate(tokens[i + 1], scope)

      return evaluate(tokens[-1], scope)

    def parse(e: str):
      tokens = []
      s = ''
      parenthesis = 0

      for c in e:
        if c == '(':
          parenthesis += 1
        elif c == ')':
          parenthesis -= 1
        if parenthesis == 0 and c == ' ':
          tokens.append(s)
          s = ''
        else:
          s += c

      if len(s) > 0:
        tokens.append(s)
      return tokens

    return evaluate(expression, {})
```


```
new Solution().evaluate()
```


---
**Score: 5**