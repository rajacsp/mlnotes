---
title: 983-Minimum-Cost-For-Tickets
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/minimum-cost-for-tickets


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
  def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    ans = 0
    last7 = deque()
    last30 = deque()

    for day in days:
      while last7 and last7[0][0] + 7 <= day:
        last7.popleft()
      while last30 and last30[0][0] + 30 <= day:
        last30.popleft()
      last7.append([day, ans + costs[1]])
      last30.append([day, ans + costs[2]])
      ans = min(ans + costs[0], last7[0][1], last30[0][1])

    return ans
```


```
new Solution().mincostTickets()
```


---
**Score: 5**