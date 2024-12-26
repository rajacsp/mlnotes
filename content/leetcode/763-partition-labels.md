---
title: 763-Partition-Labels
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/partition-labels


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
  def partitionLabels(self, S: str) -> List[int]:
    ans = []
    letterToRightmostIndex = {c: i for i, c in enumerate(S)}

    l = 0
    r = 0

    for i, c in enumerate(S):
      r = max(r, letterToRightmostIndex[c])
      if i == r:
        ans.append(r - l + 1)
        l = r + 1

    return ans
```


```
new Solution().partitionLabels()
```


---
**Score: 5**