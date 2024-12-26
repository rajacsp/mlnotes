---
title: 1087-Brace-Expansion
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/brace-expansion


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
  def expand(self, s: str) -> List[str]:
    ans = []

    def dfs(i: int, path: List[str]) -> None:
      if i == len(s):
        ans.append(''.join(path))
        return
      if s[i] == '{':
        nextRightBraceIndex = s.find('}', i)
        for c in s[i + 1:nextRightBraceIndex].split(','):
          path.append(c)
          dfs(nextRightBraceIndex + 1, path)
          path.pop()
      else:  # s[i] != '{'
        path.append(s[i])
        dfs(i + 1, path)
        path.pop()

    dfs(0, [])
    return sorted(ans)
```


```
new Solution().expand()
```


---
**Score: 5**