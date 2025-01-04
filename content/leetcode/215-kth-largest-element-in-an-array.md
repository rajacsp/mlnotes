---
title: 215-Kth-Largest-Element-In-An-Array
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/kth-largest-element-in-an-array


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
  def findKthLargest(self, nums: List[int], k: int) -> int:
    minHeap = []

    for num in nums:
      heapq.heappush(minHeap, num)
      if len(minHeap) > k:
        heapq.heappop(minHeap)

    return minHeap[0]
```


```
new Solution().findKthLargest()
```


---
**Score: 5**