---
title: 89-Gray-Code
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/gray-code


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
  def grayCode(self, n: int) -> List[int]:
    ans = [0]

    for i in range(n):
      for j in reversed(range(len(ans))):
        ans.append(ans[j] | 1 << i)

    return ans
```


```
new Solution().grayCode()
```


---
**Score: 5**