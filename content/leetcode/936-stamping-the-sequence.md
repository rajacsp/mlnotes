---
title: 936-Stamping-The-Sequence
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/stamping-the-sequence


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
  def movesToStamp(self, stamp: str, target: str) -> List[int]:
    def stampify(s: int) -> int:
      stampified = len(stamp)

      for i, st in enumerate(stamp):
        if target[s + i] == '*':
          stampified -= 1
        elif target[s + i] != st:
          return 0

      for i in range(s, s + len(stamp)):
        target[i] = '*'

      return stampified

    ans = []
    target = list(target)
    stamped = [False] * len(target)
    stampedCount = 0

    while stampedCount < len(target):
      isStamped = False
      for i in range(len(target) - len(stamp) + 1):
        if stamped[i]:
          continue
        stampified = stampify(i)
        if stampified == 0:
          continue
        stampedCount += stampified
        isStamped = True
        stamped[i] = True
        ans.append(i)
      if not isStamped:
        return []

    return ans[::-1]
```


```
new Solution().movesToStamp()
```


---
**Score: 5**