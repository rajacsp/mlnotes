---
title: 1018-Binary-Prefix-Divisible-By-5
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/binary-prefix-divisible-by-5


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
  def prefixesDivBy5(self, A: List[int]) -> List[bool]:
    ans = []
    num = 0

    for a in A:
      num = (num * 2 + a) % 5
      ans.append(num % 5 == 0)

    return ans
```


```
new Solution().prefixesDivBy5()
```


---
**Score: 5**