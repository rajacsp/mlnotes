---
title: 357-Count-Numbers-With-Unique-Digits
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/count-numbers-with-unique-digits


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
  def countNumbersWithUniqueDigits(self, n: int) -> int:
    if n == 0:
      return 1

    ans = 10
    uniqueDigits = 9
    availableNum = 9

    while n > 1 and availableNum > 0:
      uniqueDigits *= availableNum
      ans += uniqueDigits
      n -= 1
      availableNum -= 1

    return ans
```


```
new Solution().countNumbersWithUniqueDigits()
```


---
**Score: 5**