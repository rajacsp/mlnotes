---
title: 248-Strobogrammatic-Number-Iii
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/strobogrammatic-number-iii


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
  def strobogrammaticInRange(self, low: str, high: str) -> int:
    pairs = [['0', '0'], ['1', '1'], ['6', '9'], ['8', '8'], ['9', '6']]
    ans = 0

    def dfs(s: List[chr], l: int, r: int) -> None:
      nonlocal ans
      if l > r:
        if len(s) == len(low) and ''.join(s) < low:
          return
        if len(s) == len(high) and ''.join(s) > high:
          return
        ans += 1
        return

      for leftDigit, rightDigit in pairs:
        if l == r and leftDigit != rightDigit:
          continue
        s[l] = leftDigit
        s[r] = rightDigit
        if len(s) > 1 and s[0] == '0':
          continue
        dfs(s, l + 1, r - 1)

    for n in range(len(low), len(high) + 1):
      dfs([' '] * n, 0, n - 1)

    return ans
```


```
new Solution().strobogrammaticInRange()
```


---
**Score: 5**