---
title: 239-Sliding-Window-Maximum
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/sliding-window-maximum


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
  def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    ans = []
    q = deque()  # Max queue

    for i, num in enumerate(nums):
      while q and q[-1] < num:
        q.pop()
      q.append(num)
      if i >= k and nums[i - k] == q[0]:  # Out of bound
        q.popleft()
      if i >= k - 1:
        ans.append(q[0])

    return ans
```


```
new Solution().maxSlidingWindow()
```


---
**Score: 5**