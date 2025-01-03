---
title: 918-Maximum-Sum-Circular-Subarray
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/maximum-sum-circular-subarray


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
  def maxSubarraySumCircular(self, A: List[int]) -> int:
    totalSum = 0
    currMaxSum = 0
    currMinSum = 0
    maxSum = -math.inf
    minSum = math.inf

    for a in A:
      totalSum += a
      currMaxSum = max(currMaxSum + a, a)
      currMinSum = min(currMinSum + a, a)
      maxSum = max(maxSum, currMaxSum)
      minSum = min(minSum, currMinSum)

    return maxSum if maxSum < 0 else max(maxSum, totalSum - minSum)
```


```
new Solution().maxSubarraySumCircular()
```


---
**Score: 5**