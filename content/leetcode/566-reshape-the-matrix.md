---
title: 566-Reshape-The-Matrix
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/reshape-the-matrix


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
  def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    if nums == [] or r * c != len(nums) * len(nums[0]):
      return nums

    ans = [[0 for j in range(c)] for i in range(r)]
    k = 0

    for row in nums:
      for num in row:
        ans[k // c][k % c] = num
        k += 1

    return ans
```


```
new Solution().matrixReshape()
```


---
**Score: 5**