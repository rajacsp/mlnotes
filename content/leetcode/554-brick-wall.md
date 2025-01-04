---
title: 554-Brick-Wall
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/brick-wall


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
  def leastBricks(self, wall: List[List[int]]) -> int:
    maxFreq = 0
    count = defaultdict(int)

    for row in wall:
      prefix = 0
      for i in range(len(row) - 1):
        prefix += row[i]
        count[prefix] += 1
        maxFreq = max(maxFreq, count[prefix])

    return len(wall) - maxFreq
```


```
new Solution().leastBricks()
```


---
**Score: 5**