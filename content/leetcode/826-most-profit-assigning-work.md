---
title: 826-Most-Profit-Assigning-Work
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/most-profit-assigning-work


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
  def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
    ans = 0
    jobs = sorted(zip(difficulty, profit))
    worker.sort(reverse=1)

    i = 0
    maxProfit = 0

    for w in sorted(worker):
      while i < len(jobs) and w >= jobs[i][0]:
        maxProfit = max(maxProfit, jobs[i][1])
        i += 1
      ans += maxProfit

    return ans
```


```
new Solution().maxProfitAssignment()
```


---
**Score: 5**