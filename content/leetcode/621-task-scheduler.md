---
title: 621-Task-Scheduler
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/task-scheduler


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
  def leastInterval(self, tasks: List[str], n: int) -> int:
    count = Counter(tasks)
    maxFreq = max(count.values())
    # Put the most frequent task in the slot first
    maxFreqTaskOccupy = (maxFreq - 1) * (n + 1)
    # Get # Of tasks with same frequency as maxFreq,
    # we'll append them after maxFreqTaskOccupy
    nMaxFreq = sum(value == maxFreq for value in count.values())
    # Max(
    #   the most frequent task is frequent enough to force some idle slots,
    #   the most frequent task is not frequent enough to force idle slots
    # )
    return max(maxFreqTaskOccupy + nMaxFreq, len(tasks))
```


```
new Solution().leastInterval()
```


---
**Score: 5**