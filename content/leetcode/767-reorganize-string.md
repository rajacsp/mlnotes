---
title: 767-Reorganize-String
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/reorganize-string


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
  def reorganizeString(self, s: str) -> str:
    count = Counter(s)
    if max(count.values()) > (len(s) + 1) // 2:
      return ''

    ans = []
    maxHeap = [(-freq, c) for c, freq in count.items()]
    heapq.heapify(maxHeap)
    prevFreq = 0
    prevChar = '@'

    while maxHeap:
      # Get the most freq letter
      freq, c = heapq.heappop(maxHeap)
      ans.append(c)
      # Add the previous letter back so that
      # Any two adjacent characters are not the same
      if prevFreq < 0:
        heapq.heappush(maxHeap, (prevFreq, prevChar))
      prevFreq = freq + 1
      prevChar = c

    return ''.join(ans)
```


```
new Solution().reorganizeString()
```


---
**Score: 5**