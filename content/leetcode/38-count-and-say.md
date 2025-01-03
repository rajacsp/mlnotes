---
title: 38-Count-And-Say
date: 2025-01-03
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/count-and-say


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
  def countAndSay(self, n: int) -> str:
    ans = '1'

    for _ in range(n - 1):
      nxt = ''
      i = 0
      while i < len(ans):
        count = 1
        while i + 1 < len(ans) and ans[i] == ans[i + 1]:
          count += 1
          i += 1
        nxt += str(count) + ans[i]
        i += 1
      ans = nxt

    return ans
```


```
new Solution().countAndSay()
```


---
**Score: 5**