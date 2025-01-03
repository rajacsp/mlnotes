---
title: 902-Numbers-At-Most-N-Given-Digit-Set
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/numbers-at-most-n-given-digit-set


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
  def atMostNGivenDigitSet(self, D: List[str], N: int) -> int:
    ans = 0
    num = str(N)

    for i in range(1, len(num)):
      ans += len(D)**i

    for i, c in enumerate(num):
      dHasSameNum = False
      for digit in D:
        if digit < c:
          ans += len(D)**(len(num) - i - 1)
        elif digit == c:
          dHasSameNum = True
      if not dHasSameNum:
        return ans

    return ans + 1
```


```
new Solution().atMostNGivenDigitSet()
```


---
**Score: 5**