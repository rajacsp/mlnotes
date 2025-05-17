---
title: 247-Strobogrammatic-Number-Ii
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/strobogrammatic-number-ii


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
  def findStrobogrammatic(self, n: int) -> List[str]:
    def helper(n: int, k: int) -> List[str]:
      if n == 0:
        return ['']
      if n == 1:
        return ['0', '1', '8']

      ans = []

      for inner in helper(n - 2, k):
        if n < k:
          ans.append('0' + inner + '0')
        ans.append('1' + inner + '1')
        ans.append('6' + inner + '9')
        ans.append('8' + inner + '8')
        ans.append('9' + inner + '6')

      return ans

    return helper(n, n)
```


```
new Solution().findStrobogrammatic()
```


---
**Score: 5**