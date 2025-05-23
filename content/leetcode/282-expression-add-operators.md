---
title: 282-Expression-Add-Operators
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/expression-add-operators


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
  def addOperators(self, num: str, target: int) -> List[str]:
    ans = []

    # Start index, prev value, current evaluated value
    def dfs(start: int, prev: int, eval: int, path: List[str]) -> None:
      if start == len(num):
        if eval == target:
          ans.append(''.join(path))
        return

      for i in range(start, len(num)):
        if i > start and num[start] == '0':
          return
        s = num[start:i + 1]
        curr = int(s)
        if start == 0:
          path.append(s)
          dfs(i + 1, curr, curr, path)
          path.pop()
        else:
          for op in ['+', '-', '*']:
            path.append(op + s)
            if op == '+':
              dfs(i + 1, curr, eval + curr, path)
            elif op == '-':
              dfs(i + 1, -curr, eval - curr, path)
            else:
              dfs(i + 1, prev * curr, eval - prev + prev * curr, path)
            path.pop()

    dfs(0, 0, 0, [])
    return ans
```


```
new Solution().addOperators()
```


---
**Score: 5**