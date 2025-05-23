---
title: 1063-Number-Of-Valid-Subarrays
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/number-of-valid-subarrays


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
  def validSubarrays(self, nums: List[int]) -> int:
    # For each num in nums, each element x in the stack can be the leftmost
    # Element s.t. [x, num] forms a valid subarray, so the len(stack) is
    # The # Of valid subarrays ending at curr num
    #
    # E.g. nums = [1, 3, 2]
    # Num = 1, stack = [1] . valid subarray is [1]
    # Num = 3, stack = [1, 3] . valid subarrays are [1, 3], [3]
    # Num = 2, stack = [1, 2] . valid subarrays are [1, 3, 2], [2]
    ans = 0
    stack = []

    for num in nums:
      while stack and stack[-1] > num:
        stack.pop()
      stack.append(num)
      ans += len(stack)

    return ans
```


```
new Solution().validSubarrays()
```


---
**Score: 5**