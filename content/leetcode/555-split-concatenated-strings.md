---
title: 555-Split-Concatenated-Strings
date: 2025-05-17
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/split-concatenated-strings


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
  def splitLoopedString(self, strs: List[str]) -> str:
    ans = ''
    sortedStrs = [max(s, s[::-1]) for s in strs]

    for i, sortedStr in enumerate(sortedStrs):
      for s in (sortedStr, sortedStr[::-1]):
        for j in range(len(s) + 1):
          ans = max(
              ans, s[j:] + ''.join(sortedStrs[i + 1:] + sortedStrs[:i]) + s[:j])

    return ans
```


```
new Solution().splitLoopedString()
```


---
**Score: 5**