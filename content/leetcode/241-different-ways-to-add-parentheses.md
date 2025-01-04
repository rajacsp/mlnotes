---
title: 241-Different-Ways-To-Add-Parentheses
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/different-ways-to-add-parentheses


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
  @functools.lru_cache(None)
  def diffWaysToCompute(self, expression: str) -> List[int]:
    ans = []

    for i, c in enumerate(expression):
      if c in '+-*':
        for a in self.diffWaysToCompute(expression[:i]):
          for b in self.diffWaysToCompute(expression[i + 1:]):
            ans.append(eval(str(a) + c + str(b)))

    return ans or [int(expression)]
```


```
new Solution().diffWaysToCompute()
```


---
**Score: 5**