---
title: 781-Rabbits-In-Forest
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/rabbits-in-forest


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
  def numRabbits(self, answers: List[int]) -> int:
    ans = 0
    count = Counter()

    for answer in answers:
      if count[answer] % (answer + 1) == 0:
        ans += answer + 1
      count[answer] += 1

    return ans
```


```
new Solution().numRabbits()
```


---
**Score: 5**