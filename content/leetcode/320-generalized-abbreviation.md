---
title: 320-Generalized-Abbreviation
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/generalized-abbreviation


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
  def generateAbbreviations(self, word: str) -> List[str]:
    ans = []

    def getCountString(count: int) -> str:
      return str(count) if count > 0 else ''

    def dfs(i: int, count: int, path: List[str]) -> None:
      if i == len(word):
        ans.append(''.join(path) + getCountString(count))
        return

      # Abbreviate word[i]
      dfs(i + 1, count + 1, path)
      # Keep word[i], so consume the count as a string
      path.append(getCountString(count) + word[i])
      dfs(i + 1, 0, path)  # Reset count to 0
      path.pop()

    dfs(0, 0, [])
    return ans
```


```
new Solution().generateAbbreviations()
```


---
**Score: 5**