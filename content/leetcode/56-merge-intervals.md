---
title: 56-Merge-Intervals
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/merge-intervals


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
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    ans = []

    for interval in sorted(intervals):
      if not ans or ans[-1][1] < interval[0]:
        ans.append(interval)
      else:
        ans[-1][1] = max(ans[-1][1], interval[1])

    return ans
```


```
new Solution().merge()
```


---
**Score: 5**