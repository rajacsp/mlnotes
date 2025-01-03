---
title: 667-Beautiful-Arrangement-Ii
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/beautiful-arrangement-ii


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
  def constructArray(self, n: int, k: int) -> List[int]:
    ans = list(range(1, n - k + 1))

    for i in range(k):
      if i % 2 == 0:
        ans.append(n - i // 2)
      else:
        ans.append(n - k + (i + 1) // 2)

    return ans
```


```
new Solution().constructArray()
```


---
**Score: 5**