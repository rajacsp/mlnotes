---
title: 457-Circular-Array-Loop
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/circular-array-loop


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
  def circularArrayLoop(self, nums: List[int]) -> bool:
    def advance(i: int) -> int:
      return (i + nums[i]) % len(nums)

    if len(nums) < 2:
      return False

    for i, num in enumerate(nums):
      if num == 0:
        continue

      slow = i
      fast = advance(slow)
      while num * nums[fast] > 0 and num * nums[advance(fast)] > 0:
        if slow == fast:
          if slow == advance(slow):
            break
          return True
        slow = advance(slow)
        fast = advance(advance(fast))

      slow = i
      sign = num
      while sign * nums[slow] > 0:
        next = advance(slow)
        nums[slow] = 0
        slow = next

    return False
```


```
new Solution().circularArrayLoop()
```


---
**Score: 5**