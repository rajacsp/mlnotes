---
title: 301-Remove-Invalid-Parentheses
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/remove-invalid-parentheses


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
  def removeInvalidParentheses(self, s: str) -> List[str]:
    def getLeftAndRightCounts(s: str) -> tuple:
      l = 0
      r = 0

      for c in s:
        if c == '(':
          l += 1
        elif c == ')':
          if l == 0:
            r += 1
          else:
            l -= 1

      return l, r

    def isValid(s: str):
      count = 0  # Number of '(' - # Of ')'
      for c in s:
        if c == '(':
          count += 1
        elif c == ')':
          count -= 1
        if count < 0:
          return False
      return True  # Count == 0

    ans = []

    def dfs(s: str, start: int, l: int, r: int) -> None:
      if l == 0 and r == 0 and isValid(s):
        ans.append(s)
        return

      for i in range(start, len(s)):
        if i > start and s[i] == s[i - 1]:
          continue
        if r > 0 and s[i] == ')':  # Delete s[i]
          dfs(s[:i] + s[i + 1:], i, l, r - 1)
        elif l > 0 and s[i] == '(':  # Delete s[i]
          dfs(s[:i] + s[i + 1:], i, l - 1, r)

    l, r = getLeftAndRightCounts(s)
    dfs(s, 0, l, r)
    return ans
```


```
new Solution().removeInvalidParentheses()
```


---
**Score: 5**