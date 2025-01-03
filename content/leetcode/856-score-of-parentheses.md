---
title: 856-Score-Of-Parentheses
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/score-of-parentheses


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
  def scoreOfParentheses(self, S: str) -> int:
    ans = 0
    layer = 0

    for a, b in zip(S, S[1:]):
      if a + b == '()':
        ans += 1 << layer
      layer += 1 if a == '(' else -1

    return ans
```


```
new Solution().scoreOfParentheses()
```


---
**Score: 5**