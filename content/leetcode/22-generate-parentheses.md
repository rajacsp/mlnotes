---
title: 22-Generate-Parentheses
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/generate-parentheses


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
  def generateParenthesis(self, n):
    ans = []

    def dfs(l: int, r: int, s: str) -> None:
      if l == 0 and r == 0:
        ans.append(s)
      if l > 0:
        dfs(l - 1, r, s + '(')
      if l < r:
        dfs(l, r - 1, s + ')')

    dfs(n, n, '')
    return ans
```


```
new Solution().generateParenthesis()
```


---
**Score: 5**