---
title: 202-Happy-Number
date: 2024-12-26
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/happy-number


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
  def isHappy(self, n: int) -> bool:
    def squaredSum(n: int) -> bool:
      summ = 0
      while n:
        summ += pow(n % 10, 2)
        n //= 10
      return summ

    slow = squaredSum(n)
    fast = squaredSum(squaredSum(n))

    while slow != fast:
      slow = squaredSum(slow)
      fast = squaredSum(squaredSum(fast))

    return slow == 1
```


```
new Solution().isHappy()
```


---
**Score: 5**