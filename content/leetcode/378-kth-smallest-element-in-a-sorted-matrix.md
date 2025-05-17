---
title: 378-Kth-Smallest-Element-In-A-Sorted-Matrix
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix


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
  def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    minHeap = []  # (matrix[i][j], i, j)

    i = 0
    while i < k and i < len(matrix):
      heapq.heappush(minHeap, (matrix[i][0], i, 0))
      i += 1

    while k > 1:
      k -= 1
      _, i, j = heapq.heappop(minHeap)
      if j + 1 < len(matrix[0]):
        heapq.heappush(minHeap, (matrix[i][j + 1], i, j + 1))

    return minHeap[0][0]
```


```
new Solution().kthSmallest()
```


---
**Score: 5**