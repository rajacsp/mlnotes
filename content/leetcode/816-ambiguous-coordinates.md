---
title: 816-Ambiguous-Coordinates
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/ambiguous-coordinates


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
  def ambiguousCoordinates(self, S: str) -> List[str]:
    def splits(S: str) -> List[str]:
      if not S or len(S) > 1 and S[0] == S[-1] == '0':
        return []
      if S[-1] == '0':
        return [S]
      if S[0] == '0':
        return [S[0] + '.' + S[1:]]
      return [S] + [S[:i] + '.' + S[i:] for i in range(1, len(S))]

    ans = []
    S = S[1:-1]

    for i in range(1, len(S)):
      for x in splits(S[:i]):
        for y in splits(S[i:]):
          ans.append('(%s, %s)' % (x, y))

    return ans
```


```
new Solution().ambiguousCoordinates()
```


---
**Score: 5**