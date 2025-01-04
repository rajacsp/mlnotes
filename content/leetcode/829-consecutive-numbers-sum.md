---
title: 829-Consecutive-Numbers-Sum
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/consecutive-numbers-sum


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
  def consecutiveNumbersSum(self, N: int) -> int:
    ans = 0
    i = 1
    triangleNum = 1

    while triangleNum <= N:
      if (N - triangleNum) % i == 0:
        ans += 1
      i += 1
      triangleNum += i

    return ans
```


```
new Solution().consecutiveNumbersSum()
```


---
**Score: 5**