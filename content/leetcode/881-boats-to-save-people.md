---
title: 881-Boats-To-Save-People
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/boats-to-save-people


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
  def numRescueBoats(self, people: List[int], limit: int) -> int:
    ans = 0
    i = 0
    j = len(people) - 1

    people.sort()

    while i <= j:
      remain = limit - people[j]
      j -= 1
      if people[i] <= remain:
        i += 1
      ans += 1

    return ans
```


```
new Solution().numRescueBoats()
```


---
**Score: 5**