---
title: 942-Di-String-Match
date: 2025-01-04
author: Your Name
cell_count: 6
score: 5
---

https://leetcode.com/problems/di-string-match


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
  def diStringMatch(self, S: str) -> List[int]:
    ans = []
    mini = 0
    maxi = len(S)

    for c in S:
      if c == 'I':
        ans.append(mini)
        mini += 1
      else:
        ans.append(maxi)
        maxi -= 1
    ans.append(mini)

    return ans
```


```
new Solution().diStringMatch()
```


---
**Score: 5**