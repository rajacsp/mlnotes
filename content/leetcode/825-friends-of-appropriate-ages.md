---
title: 825-Friends-Of-Appropriate-Ages
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/friends-of-appropriate-ages


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
  def numFriendRequests(self, ages: List[int]) -> int:
    ans = 0
    count = [0] * 121

    for age in ages:
      count[age] += 1

    for i in range(15, 121):
      ans += count[i] * (count[i] - 1)

    for i in range(15, 121):
      for j in range(i // 2 + 8, i):
        ans += count[i] * count[j]

    return ans
```


```
new Solution().numFriendRequests()
```


---
**Score: 5**